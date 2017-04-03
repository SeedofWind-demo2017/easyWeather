from django.shortcuts import render, HttpResponse

from .forms import SubscriberForm
from .utils import sg_send_email
from newsletter import SG_TEMPLATE_IDS


def home(request):
    signup_form = SubscriberForm()
    context = {
        'form': signup_form,
    }
    return render(request, 'newsletter/home.html', context)


def subscribe(request):
    if request.method == "POST":
        signup_form = SubscriberForm(request.POST)
        if signup_form.is_valid():
            # Get instance with normalized field
            subscriber = signup_form.save(commit=False)
            # Possible Extra checking, none right now
            subscriber.save()
            # Send out sign-up email
            # subject, body, to_email, template_id, from_email="Seed@klayvio.com"
            build_email = {}
            print subscriber.gender
            if subscriber.gender == "M":
                title = "Mr."
            elif subscriber.gender == "F":
                title = "Miss."
            else:
                title = ""
            build_email['subject'] = "Thanks for your subscription %s %s" \
            % (title, subscriber.last_name)
            build_email['body'] = "Have a nice day!"
            build_email['to_email'] = subscriber.email
            build_email['template_id'] = SG_TEMPLATE_IDS.SIGNUP
            build_email['sub_dic'] = {'-greeting-': "Dear %s" % subscriber.first_name}
            sg_send_email(**build_email)
            return HttpResponse("Congratulations! You have successfuly subscribed")
            # return render(request, "newsletter/success_response.html")
        else:
            # signup_form.errors.update(signup_form.error)
            context = {}
            signup_form.errors.update(signup_form.errors)
            context['form'] = signup_form
            # return HttpResponse(signup_form.as_p(), status=404)
            return render(request, "newsletter/ajax_modal.html", context, status=404)
