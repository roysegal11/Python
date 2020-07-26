from unittest import TestCase
from Unit_Test.Worker import Worker
import datetime


class TestWorker(TestCase):

    def setUp(self):
        print("Setup")
        self.roy = Worker('Roy', 'Segal', 1998, 7, 26, "ness-ziona", 'il')

    def tearDown(self):
        print("TearDown")

    def test_full_name(self):
        pass

    def test_age(self):
        if self.assertGreaterEqual(self.roy.birth_month, datetime.datetime.now().month):
            self.assertGreater(self.roy.birth_day, datetime.datetime.now().day)
        # self.assertEqual(self.roy.birth_year, 2020)
        # self.assertGreater(self.roy.birth_year, 2020)

    def test_days_to_birthday(self):
        pass

    def test_greet(self):
        pass

    def test_location(self):
        pass
