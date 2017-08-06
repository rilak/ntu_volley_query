import unittest
import datetime

import query

class QueryTest(unittest.TestCase):

    #能不能抓到某一天的資料
    def test_one_day_data(self):
        day   = datetime.date(2017, 6, 30)
        place = 4

        result = query.QueryOneDay(day, place)

        self.assertEqual(result.place,  4)
        self.assertEqual(result.day,    "6/30(五)")
        self.assertEqual(result.record, ["105資工所女子排球隊",
                                        "105資工所女子排球隊",
                                        "",  "",   "",
                                        "105會計學系男子籃球隊",
                                        "104農藝所女子排球隊",
                                        "105機械工程學研究所女子排球隊"])

if __name__ == '__main__':
    unittest.main()
