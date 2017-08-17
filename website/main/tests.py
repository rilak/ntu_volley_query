from django.test import TestCase
from query import query

import datetime

def get_this_week():
    today = datetime.date.today()
    weekday = (today.weekday()+1)%7
    sun = today + datetime.timedelta(days = -weekday)
    sat = today + datetime.timedelta(days = 6-weekday)
    return sun, sat

class TestHomePage(TestCase):
    
    def test_home_page_show_the_basic_info(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')

        sun, sat = get_this_week()
        self.assertIn('<title>台大排球場地查詢</title>', html)
        #self.assertIn(f'<h1>{sun.month}/{sun.day}~{sat.month}/{sat.day}</h1>', html)