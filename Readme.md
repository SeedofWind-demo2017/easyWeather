## Klayvio Weather APP

#### Configuration
-----------
1. Download and unzip the [new_klayvio_weahter](https://www.dropbox.com/s/fwy0cb9c794713v/klayvio_weather.zip?dl=0)
2. create a virtual env 
   ```
   virtualenv -p <PATH TO PYTHON2.7> <PATH TO VIRTUAL_ENV PATH>
   if you have python2.7 and want to create the virtualenv at current project folder DO
   
   virtualenv . (following step will assume you did this)
   ```
3. activate virtualenv
   ```
   source bin/activate
   ```
4. install all needed packages
   ```
   pip install -r requirements.txt
   ```
5. migrate and create database schema
   ```
   python src/manage.py migrate
   ```
6. finally runserver
   ```
   python src/manage.py runserver
   ```
7. now you can also test the newsletter command locally
   ```
   python src/manage.py send_newsletters
   &
   python src/manage.py send_newsletters --demo
   ```
8. Credentials for admin page
   ```
   user:   klayvio
   password:   klayvio
   ```
#### Functionalities
---------
Achieved basic requirements and extra functionalities(marked by bold)
1. user can enter their email address and choose their location from a list of the top 100 cities in the US by population. user information is stored in postgres in production, sqllite in dev
    * Standard email format check
    * prevent @smg to signup
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
-----------
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
    * Dropbox for static files hosting

Detailed docuemnt for the code are in the file. Also more than happy to go through
with you
#### Demo
-------
I have used a Heroku dyno to serve the webiste

**[Klayvio Weather](https://demo-klayvio-weather.herokuapp.com/)**

Following are some email demo the app is able to send out (including sign-up welcome and weather daily newsletter)   
Notice that the msg and template will not match since it's generated using the --demo flag   
Also, it's not all the templates 


![alt text](https://www.dropbox.com/s/70z4hmprl2q71mn/3.png?raw=1 "Logo Title Text 1")



![alt text](https://www.dropbox.com/s/vhne7ixix2e42sg/1.png?raw=1 "Logo Title Text 1")



![alt text](https://www.dropbox.com/s/dr2lw35ky67ij09/2.png?dl=1 "Logo Title Text 1")



![alt text](https://www.dropbox.com/s/odq9bt35zprzvw2/4.png?raw=1 "Logo Title Text 1")



![alt text](https://www.dropbox.com/s/mlhohruwmpuqtz7/5.png?raw=1 "Logo Title Text 1")



![alt text](https://www.dropbox.com/s/l2zbglxb75akrl1/7_new.png?raw=1 "Logo Title Text 1")


When click on the restaurant link, it will go to page like this
![alt text](https://www.dropbox.com/s/5r5zwppl1yqyzun/6.png?raw=1 "Logo Title Text 1")


#### Improvements
Quite a few improvements can be made
1. rabbitMQ + celery to queue up the task
2. better templatize the email building

I would love the chance to go into more detail to discuss
