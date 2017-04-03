#### Functionalities
Achieved basic requirements and extra functionalities(marked by bold)
1. user can enter their email address and choose their location from a list of the top 100 cities in the US by population. user information is stored in postgres in production, sqllite in dev
    * Standard email format check
    * prevent @klayvio to signup
    * Duplicated email address check

2. (**extra**) *upon successfully signing up, a welcome to family email will be sent to user*

3. Customized management option
    *  python src/manage.py send_newsletters* will send out newsletters to every subscribed user
        * required temperature info in body and subject
        * customized template to each type of weather
        * (**extra**) send out pick of the day best restaurant (clickable link)
        * (**extra**) send random generated coupon code
    * (**extra**) *python src/manage.py send_newsletters --demo*
        * send out all template to admin (me) for demo purpose

#### Approach
Technologies used are
1. Backend
    * Django
    * Postgres
2. Middleware
    * WhiteNoise
3. Frontend
    * Materialize
4. External API
    * send-grid
    * WounderGround
    * Zomato
4. Hosting
    * Heroku

Detailed docuemnt for the code are in the file. Also more than happy to go through
with you
#### Demo
I have used a Heroku dyno to serve the webiste

**[Klayvio Weather](https://demo-klayvio-weather.herokuapp.com/)**
