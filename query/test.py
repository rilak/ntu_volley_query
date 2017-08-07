import unittest
import datetime

import query

record_6_29 = ["105資工所女子排球隊",
               "105資工所女子排球隊",
               "",  "",   "",
               "105會計學系男子籃球隊",
               "104心理系女子排球隊",
               "105電機工程學系女子排球隊"]
record_6_30 = ["105資工所女子排球隊",
               "105資工所女子排球隊",
               "",  "",   "",
               "105會計學系男子籃球隊",
               "104農藝所女子排球隊",
               "105機械工程學研究所女子排球隊"]
record_7_6 = ["", "", "", "",
              "105法律研究所女子排球隊",
              "104法律系大學部女子排球隊",
              "105心理所女子排球隊",
              "104農藝所女子排球隊"]

days_6_25 = ['6/25(日)', '6/26(一)', '6/27(二)', '6/28(三)', '6/29(四)', '6/30(五)', '7/1(六)']
days_6_30 = ['6/30(五)', '7/1(六)', '7/2(日)',  '7/3(一)',  '7/4(二)',  '7/5(三)',  '7/6(四)']

class QueryTest(unittest.TestCase):

    #能不能抓到某一天的資料
    def test_one_day_data(self):
        day   = datetime.date(2017, 6, 30)
        place = 4

        result = query.query_one_day(day, place)

        self.assertEqual(result.place,  4)
        self.assertEqual(result.day,    "6/30(五)")
        self.assertEqual(result.record, record_6_30)

    def test_one_week_data(self):
        day   = datetime.date(2017, 6, 30)
        place = 4

        results = query.query_one_week(day, place)

        for index, result in enumerate(results):
            self.assertEqual(result.place, 4)
            self.assertEqual(result.day, days_6_25[index])

        self.assertEqual(results[4].record, record_6_29)
        self.assertEqual(results[5].record, record_6_30)

    def test_recent_7_data(self):
        day = datetime.date(2017, 6, 30)
        place = 4

        results = query.query_recent_7_days(day, place)

        for index, result in enumerate(results):
            self.assertEqual(result.place, 4)
            self.assertEqual(result.day, days_6_30[index])

        
        self.assertEqual(results[0].record, record_6_30)
        self.assertEqual(results[6].record, record_7_6)

if __name__ == '__main__':
    unittest.main()
