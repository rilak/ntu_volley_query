from django.shortcuts import render
from query import query

import datetime

def get_recent_7_days_range_str():
    day0 = datetime.date.today()
    day6 = day0 + datetime.timedelta(days = 6)
    return f"{day0.month}/{day0.day}~{day6.month}/{day6.day}"

def get_this_week_range_str():
    today = datetime.date.today()
    weekday = (today.weekday()+1)%7
    sun = today + datetime.timedelta(days = -weekday)
    sat = today + datetime.timedelta(days = 6-weekday)
    return f"{sun.month}/{sun.day}~{sat.month}/{sat.day}"

def get_record_table():
    times = ["08:00~10:00",
         "10:00~12:00",
         "12:00~13:00",
         "13:00~15:00",
         "15:00~17:00",
         "17:00~18:00",
         "18:00~20:00",
         "20:00~22:00"]
    today = datetime.date.today()
    records = []
    for i in range(4, 8):
        records.append(query.query_recent_7_days(today, i))

    html = ["""<table class="table table-bordered table-responsive">
        <thead>
            <tr>
                <th> # </th>
    """]
                
    html.extend( f'<th colspan="4"> {i.day} </th>' for i in records[0] )

    html.append( """</tr>
        </thead>
        <tbody>
            <tr>
                <th scope="row"> 場地 </th>
    """ )
                
    for i in records[0]:
        html.append("<td>場四</td><td>場五</td><td>場六</td><td>場七</td>")

    html.append("</tr>")

    for t in range(8):
        html.append('<tr>')
        html.append(f'<th scope="row">  { times[t] } </th>')
        for day in range(7):
            for place in range(4):
                x = records[place][day].record[t]
                if x == "":
                    html.append('<td> &nbsp; </td>')
                elif "資訊工程" in x or "資訊網路" in x:
                    html.append(f'<td class="info" title="{x}"> &nbsp; </td>')
                else:
                    html.append(f'<td class="danger" title="{x}"> &nbsp; </td>')
        html.append('</tr>')

    html.append("""</tbody> </table>""")

    return "".join(html).replace("\n", "")

def home_page(request):
    return render(request, 'home_page.html', {
            "big_title" : get_recent_7_days_range_str(),
            "table" : get_record_table(),
        })


