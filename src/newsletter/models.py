from django.db import models

# Create your models here.


class ADDRESS_INDEX(object):
    city = 0
    state = 1

TOP100 = ['New York ,NY,"8,363,710"',
          'Los Angeles ,CA,"3,833,995"',
          'Chicago ,IL,"2,853,114"\r\n',
          'Houston ,TX,"2,242,193"\r\n',
          'Phoenix ,AZ,"1,567,924"\r\n',
          'Philadelphia ,PA,"1,447,395"\r\n',
          'San Antonio ,TX,"1,351,305"\r\n',
          'Dallas ,TX,"1,279,910"\r\n',
          'San Diego ,CA,"1,279,329"\r\n',
          'San Jose ,CA,"948,279"\r\n',
          'Detroit ,MI,"912,062"\r\n',
          'San Francisco ,CA,"808,976"\r\n',
          'Jacksonville ,FL,"807,815"\r\n',
          'Indianapolis,IN,"798,382"\r\n',
          'Austin ,TX,"757,688"\r\n',
          'Columbus ,OH,"754,885"\r\n',
          'Fort Worth ,TX,"703,073"\r\n',
          'Charlotte ,NC,"687,456"\r\n',
          'Memphis ,TN,"669,651"\r\n',
          'Baltimore ,MD,"636,919"\r\n',
          'El Paso ,TX,"613,190"\r\n',
          'Boston ,MA,"609,023"\r\n',
          'Milwaukee ,WI,"604,477"\r\n',
          'Denver ,CO,"598,707"\r\n',
          'Seattle ,WA,"598,541"\r\n',
          'Nashville,TN,"596,462"\r\n',
          'Washington ,DC,"591,833"\r\n',
          'Las Vegas ,NV,"558,383"\r\n',
          'Portland ,OR,"557,706"\r\n',
          'Louisville,KY,"557,224"\r\n',
          'Oklahoma City ,OK,"551,789"\r\n',
          'Tucson ,AZ,"541,811"\r\n',
          'Atlanta ,GA,"537,958"\r\n',
          'Albuquerque ,NM,"521,999"\r\n',
          'Fresno ,CA,"476,050"\r\n',
          'Sacramento ,CA,"463,794"\r\n',
          'Long Beach ,CA,"463,789"\r\n',
          'Mesa ,AZ,"463,552"\r\n',
          'Kansas City ,MO,"451,572"\r\n',
          'Omaha ,NE,"438,646"\r\n',
          'Cleveland ,OH,"433,748"\r\n',
          'Virginia Beach ,VA,"433,746"\r\n',
          'Miami ,FL,"413,201"\r\n',
          'Oakland ,CA,"404,155"\r\n',
          'Raleigh ,NC,"392,552"\r\n',
          'Tulsa ,OK,"385,635"\r\n',
          'Minneapolis ,MN,"382,605"\r\n',
          'Colorado Springs ,CO,"380,307"\r\n',
          'Honolulu,HI,"374,676"\r\n',
          'Arlington ,TX,"374,417"\r\n',
          'Wichita ,KS,"366,046"\r\n',
          'St. Louis ,MO,"354,361"\r\n',
          'Tampa ,FL,"340,882"\r\n',
          'Santa Ana ,CA,"339,130"\r\n',
          'Anaheim ,CA,"335,288"\r\n',
          'Cincinnati ,OH,"333,336"\r\n',
          'Bakersfield ,CA,"321,078"\r\n',
          'Aurora ,CO,"319,057"\r\n',
          'New Orleans ,LA,"311,853"\r\n',
          'Pittsburgh ,PA,"310,037"\r\n',
          'Riverside ,CA,"295,357"\r\n',
          'Toledo ,OH,"293,201"\r\n',
          'Stockton ,CA,"287,037"\r\n',
          'Corpus Christi ,TX,"286,462"\r\n',
          'Lexington,KY,"282,114"\r\n',
          'St. Paul ,MN,"279,590"\r\n',
          'Anchorage,AK,"279,243"\r\n',
          'Newark ,NJ,"278,980"\r\n',
          'Buffalo ,NY,"270,919"\r\n',
          'Plano ,TX,"267,480"\r\n',
          'Henderson ,NV,"252,064"\r\n',
          'Lincoln ,NE,"251,624"\r\n',
          'Fort Wayne ,IN,"251,591"\r\n',
          'Glendale ,AZ,"251,522"\r\n',
          'Greensboro ,NC,"250,642"\r\n',
          'Chandler ,AZ,"247,140"\r\n',
          'St. Petersburg ,FL,"245,314"\r\n',
          'Jersey City ,NJ,"241,114"\r\n',
          'Scottsdale ,AZ,"235,371"\r\n',
          'Norfolk ,VA,"234,220"\r\n',
          'Madison ,WI,"231,916"\r\n',
          'Orlando ,FL,"230,519"\r\n',
          'Birmingham ,AL,"228,798"\r\n',
          'Baton Rouge ,LA,"223,689"\r\n',
          'Durham ,NC,"223,284"\r\n',
          'Laredo ,TX,"221,659"\r\n',
          'Lubbock ,TX,"220,483"\r\n',
          'Chesapeake ,VA,"220,111"\r\n',
          'Chula Vista ,CA,"219,318"\r\n',
          'Garland ,TX,"218,577"\r\n',
          'Winston-Salem ,NC,"217,600"\r\n',
          'North Las Vegas ,NV,"217,253"\r\n',
          'Reno ,NV,"217,016"\r\n',
          'Gilbert,AZ,"216,449"\r\n',
          'Hialeah ,FL,"210,542"\r\n',
          'Arlington,VA,"209,969"\r\n',
          'Akron ,OH,"207,510"\r\n',
          'Irvine ,CA,"207,500"\r\n',
          'Rochester ,NY,"206,886"\r\n',
          'Boise City ,ID,"205,314"\r\n']

PLACE_CHOICES = [(None, '')] + [(i, data.split(',')[ADDRESS_INDEX.city] + ', '
                                 + data.split(',')[ADDRESS_INDEX.state])
                                for i, data in enumerate(TOP100,1)]


class Subscriber(models.Model):
    email = models.EmailField(null=False, blank=False, db_index=True)
    first_name = models.CharField(null=True, max_length=255)
    last_name = models.CharField(null=True, max_length=255)
    city = models.CharField(null=True, max_length=255)
    state = models.CharField(null=True, max_length=255)
    gender = models.CharField(default='', choices=((None, ''), ('F', 'Female'),
                                                   ('M', 'Male'), ('O', 'Other')), max_length=255)
    # city_name = models.CharField(null=True, max_length=255)
    # zipcode = models.IntegerField(null=False, blank=False)
    time_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # __str__ for python3
    def __unicode__(self):
        return self.email
