from requests import ConnectionError

from django.core.management.base import BaseCommand, CommandError

from newsletter import SG_TEMPLATE_IDS
from newsletter.models import Subscriber
from newsletter.management.commands import get_message, get_weather_data, \
    get_template_id, get_restaurant, get_coupon
from newsletter.utils import sg_send_email


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--demo',
                            action='store_true',
                            dest='demo',
                            default=False,
                            help='send all demo templates to seed')

    def handle(self, *args, **options):
        subscribers = Subscriber.objects.all()
        if options['demo']:
            try:
                subscriber = Subscriber.objects.get(email='cdzengpeiyun@gmail.com')
            except Subscriber.DoesNotExist:
                raise CommandError('admin does not exist')

            try:
                weather_data = get_weather_data(subscriber)
            except ConnectionError:
                raise CommandError("cannot get this %s's weather data" % str(subscriber))
            all_template_ids = {key: value for key, value in SG_TEMPLATE_IDS.
                                __dict__.items() if not
                                key.startswith('__') and not callable(key)}.values()

            for template_id in all_template_ids:
                build_email = {}
                msg = get_message(**weather_data)
                build_email['subject'] = msg
                build_email['body'] = "Enjoy rest of your day!"
                build_email['to_email'] = subscriber.email
                build_email['template_id'] = template_id
                restaurtant, url = get_restaurant(subscriber.city)
                _restaurant = "<a href=%s>%s</a>" % (url.replace('\\', ''), restaurtant)
                build_email['sub_dic'] = {'-greeting-': "Dear %s" % subscriber.first_name,
                                          '-temperature-': weather_data['cur_temp'],
                                          '-detail-': weather_data['detail'],
                                          '-avg-': weather_data['average_temp'],
                                          '-restaurant_name-': _restaurant,
                                          '-coupon_code-': str(get_coupon())
                                          }
                try:
                    print build_email
                    sg_send_email(**build_email)

                except Exception as e:
                    print e
                    print "emailing eror for user %s (most likely due to\
                     SENDGRID is down)" % str(subscriber)
            print "send all the demo templates to admin"
            return
        for subscriber in subscribers:
            try:
                weather_data = get_weather_data(subscriber)
            except ConnectionError:
                print "cannot get this %s's weather data" % str(subscriber)
                continue
            except ValueError as e:
                print e
                print "cannot find cur_temp for this user %s" % subscriber
                continue
            build_email = {}
            print subscriber
            print "weatherdata %s" % weather_data
            msg = get_message(**weather_data)
            build_email['subject'] = msg
            build_email['body'] = "Enjoy rest of your day!"
            build_email['to_email'] = subscriber.email
            build_email['template_id'] = get_template_id(**weather_data)
            restaurtant, url = get_restaurant(subscriber.city)
            _restaurant = "<a href=%s>%s</a>" % (url.replace('\\', ''), restaurtant)
            build_email['sub_dic'] = {'-greeting-': "Dear %s" % subscriber.first_name,
                                      '-temperature-': weather_data['cur_temp'],
                                      '-detail-': weather_data['detail'],
                                      '-avg-': weather_data['average_temp'],
                                      '-restaurant_name-': _restaurant,
                                      '-coupon_code-': str(get_coupon())
                                      }
            try:
                print build_email
                sg_send_email(**build_email)

            except Exception as e:
                print e
                print "emailing eror for user %s (most likely due to\
                 SENDGRID is down)" % str(subscriber)
