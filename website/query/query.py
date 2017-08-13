import bs4
import requests
import datetime

class Record():

    def __init__(self, day=None, place=None, record=None):
        self.day    = day
        self.place  = place
        self.record = record if record else []

def send_query(date, place):
    url = "http://ntusportscenter.ntu.edu.tw/ntu/front/order.aspx?"
    response = requests.get(url, params={
        "yearno": date.year,
        "monthno": date.month,
        "dayno": date.day,
        "acp2id":42 + place,
    })
    html   = response.content
    soup   = bs4.BeautifulSoup(html, "html.parser")
    table  = soup.find(id="cal")
    all_row = table.findAll('tr')

    records = [Record(place=place) for i in range(7)]

    all_row = table.findAll('tr')
    first_row = all_row[0].findAll('td')

    for i, grid in enumerate(first_row[1:]):
        records[i].day = grid.text
    
    for row in all_row[1:]:
        row = row.findAll('td')
        for i, grid in enumerate(row[1:]):
            records[i].record.append(grid.text)
    
    return records

def query_one_day(day, place):
    records  = send_query(day, place)
    day_text = f"{day.month}/{day.day}"
    for r in records:
        if day_text in r.day:
            return r
    return None

def query_one_week(day, place):
    return send_query(day, place)

def query_recent_7_days(start_day, place):
    if start_day.weekday() == 6:      #剛好一整週
        return send_query(start_day, place)


    days = []
    for i in range(7):
        date = start_day + datetime.timedelta(days=i)
        days.append( f"{date.month}/{date.day}" )

    end_day = start_day + datetime.timedelta(days=i)
    records = send_query(start_day, place) + send_query(end_day, place)
    records = [r for r in records if r.day[:-3] in days]
    return records
