import unittest
from unittest import TestCase
import datetime
from school import timing


class WeekCtlTestCase(TestCase):
    def test_begin_of_week(self):
        date = datetime.date(year=2018, month=9, day=13)
        begin = timing.begin_of_week(date)
        compared = datetime.date(year=2018, month=9, day=10)
        self.assertEqual(begin, compared)

    def test_weakday(self):
        date = datetime.date(year=2018, month=9, day=13)
        self.assertEqual(timing.weekday(date), 5)

    def test_week_date_range(self):
        date = datetime.date(year=2018, month=9, day=13)
        a = datetime.date(year=2018, month=9, day=10)
        b = datetime.date(year=2018, month=9, day=16)
        (first, last) = timing.week_date_range(date)
        self.assertEqual(first, a)
        self.assertEqual(last, b)

    def test_from_date(self):
        date = datetime.date(year=2018, month=9, day=13)
        self.assertEqual(timing.from_date(date), "13.09.2018")

    def test_to_date(self):
        compared = datetime.date(year=2018, month=9, day=13)
        self.assertEqual(timing.to_date("13.09.2018",



if __name__ == '__main__':
    unittest.main()
