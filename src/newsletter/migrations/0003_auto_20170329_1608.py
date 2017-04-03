# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20170329_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='full_name',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='city',
            field=models.TextField(default=1, max_length=255, choices=[(0, b'New York , NY'), (1, b'Los Angeles , CA'), (2, b'Chicago , IL'), (3, b'Houston , TX'), (4, b'Phoenix , AZ'), (5, b'Philadelphia , PA'), (6, b'San Antonio , TX'), (7, b'Dallas , TX'), (8, b'San Diego , CA'), (9, b'San Jose , CA'), (10, b'Detroit , MI'), (11, b'San Francisco , CA'), (12, b'Jacksonville , FL'), (13, b'Indianapolis, IN'), (14, b'Austin , TX'), (15, b'Columbus , OH'), (16, b'Fort Worth , TX'), (17, b'Charlotte , NC'), (18, b'Memphis , TN'), (19, b'Baltimore , MD'), (20, b'El Paso , TX'), (21, b'Boston , MA'), (22, b'Milwaukee , WI'), (23, b'Denver , CO'), (24, b'Seattle , WA'), (25, b'Nashville, TN'), (26, b'Washington , DC'), (27, b'Las Vegas , NV'), (28, b'Portland , OR'), (29, b'Louisville, KY'), (30, b'Oklahoma City , OK'), (31, b'Tucson , AZ'), (32, b'Atlanta , GA'), (33, b'Albuquerque , NM'), (34, b'Fresno , CA'), (35, b'Sacramento , CA'), (36, b'Long Beach , CA'), (37, b'Mesa , AZ'), (38, b'Kansas City , MO'), (39, b'Omaha , NE'), (40, b'Cleveland , OH'), (41, b'Virginia Beach , VA'), (42, b'Miami , FL'), (43, b'Oakland , CA'), (44, b'Raleigh , NC'), (45, b'Tulsa , OK'), (46, b'Minneapolis , MN'), (47, b'Colorado Springs , CO'), (48, b'Honolulu, HI'), (49, b'Arlington , TX'), (50, b'Wichita , KS'), (51, b'St. Louis , MO'), (52, b'Tampa , FL'), (53, b'Santa Ana , CA'), (54, b'Anaheim , CA'), (55, b'Cincinnati , OH'), (56, b'Bakersfield , CA'), (57, b'Aurora , CO'), (58, b'New Orleans , LA'), (59, b'Pittsburgh , PA'), (60, b'Riverside , CA'), (61, b'Toledo , OH'), (62, b'Stockton , CA'), (63, b'Corpus Christi , TX'), (64, b'Lexington, KY'), (65, b'St. Paul , MN'), (66, b'Anchorage, AK'), (67, b'Newark , NJ'), (68, b'Buffalo , NY'), (69, b'Plano , TX'), (70, b'Henderson , NV'), (71, b'Lincoln , NE'), (72, b'Fort Wayne , IN'), (73, b'Glendale , AZ'), (74, b'Greensboro , NC'), (75, b'Chandler , AZ'), (76, b'St. Petersburg , FL'), (77, b'Jersey City , NJ'), (78, b'Scottsdale , AZ'), (79, b'Norfolk , VA'), (80, b'Madison , WI'), (81, b'Orlando , FL'), (82, b'Birmingham , AL'), (83, b'Baton Rouge , LA'), (84, b'Durham , NC'), (85, b'Laredo , TX'), (86, b'Lubbock , TX'), (87, b'Chesapeake , VA'), (88, b'Chula Vista , CA'), (89, b'Garland , TX'), (90, b'Winston-Salem , NC'), (91, b'North Las Vegas , NV'), (92, b'Reno , NV'), (93, b'Gilbert, AZ'), (94, b'Hialeah , FL'), (95, b'Arlington, VA'), (96, b'Akron , OH'), (97, b'Irvine , CA'), (98, b'Rochester , NY'), (99, b'Boise City , ID')]),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
