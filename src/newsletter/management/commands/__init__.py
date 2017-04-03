import requests
import urllib2
import ast
import os
import base64
import random
from datetime import datetime

from klayvio_weather.settings import WOUNDERGROUND_API_KEY, ZOMOTA_API_KEY
from newsletter import SG_TEMPLATE_IDS


WEATHER_PHRASE_BAD = set(["drizzle", "rain", "snow", "ice", "hail", "mist",
                          "ash", "dust", "sant", "haze", "spary", "sandstorm",
                          "showers", "thunderstorms", "freezing", "squalls"])
WEATHER_PHRASE_RAIN = set(["drizzle", "rain", "hail", "showers", "spray"])


def get_weather_data(subscriber):
    # return current_temp, smart_average
    # raise ConnectionError
    # deal with other error
    city, state = subscriber.city, subscriber.state
    url = 'http://api.wunderground.com/api/%s/conditions/almanac/q/%s/%s.json'\
        % (WOUNDERGROUND_API_KEY, city, state)

    r = requests.get(url)
    weather_dic = r.json()
    cur_temp = float(weather_dic['current_observation']['temp_f'])

    # if normal does not exist, set it to cur_temp
    if (weather_dic['almanac']['temp_high']['normal']['F']):
        normal_high = float(weather_dic['almanac']['temp_high']['normal']['F'])
    else:
        normal_high = cur_temp
    if (weather_dic['almanac']['temp_low']['normal']['F']):
        normal_low = float(weather_dic['almanac']['temp_low']['normal']['F'])
    else:
        normal_low = cur_temp
    normal_temp = get_smartavg(normal_high, normal_low)
    detail = weather_dic['current_observation']['weather']
    return {'cur_temp': cur_temp, 'average_temp': normal_temp, 'detail': detail.lower()}


def get_smartavg(high, low):
    # return the smart average
    cur_hour = datetime.now().time().hour
    increment_day = (high - low) / 8.0
    decrease_night = (low - high) / 16.0
    if cur_hour >= 15 and cur_hour <= 24:
        return high + (cur_hour - 15) * decrease_night
    if cur_hour >= 0 and cur_hour <= 7:
        midnight_temp = (9 * decrease_night + high)
        return midnight_temp + cur_hour * decrease_night
    else:
        return low + increment_day * (cur_hour - 7)


def get_message(cur_temp, average_temp, detail):
    """
    If it's nice outside, either sunny or 5 degrees warmer than the average
    temperature for that location at that time of year, the email's subject
    should be "It's nice out! Enjoy a discount on us." Or if's it's not so nice out
    either precipitating or 5 degrees cooler than the average temperature, the subject
    should be "Not so nice out? That's okay, enjoy a discount on us." If the weather doesn't
    meet either of those conditions, it's an average weather day and the email subject should
    read simply "Enjoy a discount on us." In all cases the email should be sent to the
    recipient's entered email address and come from your email address.
    """
    bad_detail = any(d in WEATHER_PHRASE_BAD for d in detail)
    promotion = "Enjoy a discount on us"
    if cur_temp >= average_temp + 5.0 or detail == "clear":
        msg = "It's nice out! %s" % (promotion)
    elif cur_temp <= average_temp - 5.0 or bad_detail:
        msg = "Not so nice out? That's okay, e%s" % (promotion[1:])
    else:
        msg = promotion
    return msg


def get_template_id(cur_temp, average_temp, detail):
    if any(d == "clear" for d in detail) and cur_temp > average_temp + 6:
        template_id = SG_TEMPLATE_IDS.SUPER
    elif any(d == "clear" for d in detail):
        template_id = SG_TEMPLATE_IDS.SUNNY
    elif any(d in WEATHER_PHRASE_RAIN for d in detail):
        template_id = SG_TEMPLATE_IDS.RAINY
    elif any(d == "thunderstorms" for d in detail):
        template_id = SG_TEMPLATE_IDS.THUNDERSTORM
    elif any(d == "snow" for d in detail):
        template_id = SG_TEMPLATE_IDS.SNOW
    elif any(d == "cloudy" for d in detail):
        template_id = SG_TEMPLATE_IDS.CLOUDY
    else:
        template_id = SG_TEMPLATE_IDS.NORMAL
    return template_id


def get_restaurant(city):
    """
    Pick one best rated restaurant according to city location using zomato API
    """
    req = urllib2.Request("https://developers.zomato.com/api/v2.1/locations?query=%s"
                          % city.encode('utf-8').replace(' ', '%20'))
    req.add_header('user-key', ZOMOTA_API_KEY)
    try:
        resp = urllib2.urlopen(req)
        dic = ast.literal_eval(resp.read())
        entity_type = dic['location_suggestions'][0]['entity_type']
        entity_id = dic['location_suggestions'][0]['entity_id']
        if entity_type != "city":
            return None, None
        req = urllib2.Request("https://developers.zomato.com/api/v2.1/location_details?entity_id=%d&entity_type=city"
                              % entity_id)
        req.add_header('user-key', ZOMOTA_API_KEY)
        resp = urllib2.urlopen(req)
        dic = ast.literal_eval(resp.read())
        # print dic
        restaurants = dic['best_rated_restaurant']
        # print restaurants
        index = random.randint(0, len(restaurants) - 1)
        print restaurants[index]
        return restaurants[index]['restaurant']['name'], restaurants[index]['restaurant']['url']
    except Exception as e:
        print e
        return None, None


def get_coupon(len=8):
    token = os.urandom(len)
    return base64.b64encode(token)
