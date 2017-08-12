from django.shortcuts import render

import datetime

def get_this_week_range_str():
    today = datetime.date.today()
    weekday = (today.weekday()+1)%7
    sun = today + datetime.timedelta(days = -weekday)
    sat = today + datetime.timedelta(days = 6-weekday)
    return f"{sun.month}/{sun.day}~{sat.month}/{sat.day}"

def home_page(request):
    return render(request, 'home_page.html', {
            "big_title" : get_this_week_range_str(),
        })