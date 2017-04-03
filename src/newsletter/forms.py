from django import forms
from django.utils.translation import ugettext as _
from material import Layout, Row, Fieldset

from newsletter import BLACKLIST_DOMAINS, BLACKLIST_EXTENSIONS, DATA_STRING
from .models import Subscriber, PLACE_CHOICES, ADDRESS_INDEX


def _email_validator(email):
    """
    Extra email validation
    """
    email_base, provider = email.split("@")
    prov = provider.split(".")
    domain, extension = prov[0], prov[-1]
    if domain in BLACKLIST_DOMAINS or extension in BLACKLIST_EXTENSIONS:
        raise forms.ValidationError(_("Sorry, you cannot enjoy our service"))
    if Subscriber.objects.filter(email=email).exists():
        raise forms.ValidationError(_("You have already subscribed"))


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['first_name', 'last_name', 'email', 'gender']
    address = forms.ChoiceField(required=True, choices=PLACE_CHOICES)

    _receive = forms.BooleanField(required=True, label='I want to receive\
                                      weather notification from Klayvio Weather Service')
    _agree = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')
    # gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'),
    #                                     ('M', 'Male'), ('O', 'Other')))
    layout = Layout(Fieldset('Subscribtion Form', 'email', Row('first_name', 'last_name'),
                    Row('address', 'gender'), '_receive', '_agree'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        _email_validator(email)
        return email

    def save(self, commit=True, *args, **kwargs):
        """
        override save method
        """
        instance = super(SubscriberForm, self).save(commit=False)
        city_state = int(self.cleaned_data.get('address'))
        _city = PLACE_CHOICES[city_state][DATA_STRING].split(',')[ADDRESS_INDEX.city]
        _state = PLACE_CHOICES[city_state][DATA_STRING].split(',')[ADDRESS_INDEX.state]
        instance.city = _city.strip()
        instance.state = _state.strip()
        if commit:
            instance.save()
        return instance
