'''
Created on Aug 15, 2019

@author: Jeffrey
'''
import unittest
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from datetime import timezone
from converter.time_util import TimeUtils


class Test(unittest.TestCase):


    def setUp(self):
        self.test_date = date(2019,8,15)
        self.test_time = time(20,10,15)


    def tearDown(self):
        pass


    def testCalculateTimestampInputDateAndTime1(self):
        time_utils = TimeUtils(self.test_date, self.test_time)
        actual = time_utils.calculateTimestamp(None, None, 140.320)
        expected = datetime.combine(self.test_date, self.test_time, tzinfo=timezone.utc) + timedelta(0,140.320)
        self.assertEqual(expected, actual, 'The calculated timestamp did not match the expected value.')
        
    def testCalculatedTimestampInputDateAndTime2(self):
        time_utils = TimeUtils(self.test_date, self.test_time)
        test_gps_date = date(1999,12,19)
        actual = time_utils.calculateTimestamp(test_gps_date, None, 1432.938)
        expected = datetime.combine(self.test_date, self.test_time, tzinfo=timezone.utc) + timedelta(0,1432.938)
        self.assertEqual(expected, actual, 'Time calculated timestamp did not match the expected value.')
        
    def testCalculatedTimestampInputDateAndTime3(self):
        time_utils = TimeUtils(self.test_date, self.test_time)
        test_gps_time = time(22,38,12)
        actual = time_utils.calculateTimestamp(None, test_gps_time, 2273.431)
        expected = datetime.combine(self.test_date, self.test_time, tzinfo=timezone.utc) + timedelta(0,2273.431)
        self.assertEqual(expected, actual, 'Time calculated timestamp did not match the expected value.')

    def testCalculatedTimestampInputDateAndTime4(self):
        time_utils = TimeUtils(self.test_date, self.test_time)
        test_gps_date = date(1999,12,19)
        test_gps_time = time(22,38,12)
        actual = time_utils.calculateTimestamp(test_gps_date, test_gps_time, 1174.835)
        expected = datetime.combine(self.test_date, self.test_time, tzinfo=timezone.utc) + timedelta(0,1174.835)
        self.assertEqual(expected, actual, 'Time calculated timestamp did not match the expected value.')

    def testCalculateTimestampInputDate1(self):
        time_utils = TimeUtils(self.test_date, None)
        actual = time_utils.calculateTimestamp(None, None, 140.320)
        self.assertIsNone(actual, 'The calculated timestamp was expected to be None.')
        
    def testCalculatedTimestampInputDate2(self):
        time_utils = TimeUtils(self.test_date, None)
        test_gps_date = date(1999,12,19)
        actual = time_utils.calculateTimestamp(test_gps_date, None, 1432.938)
        self.assertIsNone(actual, 'The calculated timestamp was expected to be None.')
        
    def testCalculatedTimestampInputDate3(self):
        time_utils = TimeUtils(self.test_date, None)
        test_gps_time = time(22,38,12)
        actual = time_utils.calculateTimestamp(None, test_gps_time, 2273.431)
        expected = datetime.combine(self.test_date, test_gps_time, tzinfo=timezone.utc)
        self.assertEqual(expected, actual, 'Time calculated timestamp did not match the expected value.')

    def testCalculatedTimestampInputDate4(self):
        time_utils = TimeUtils(self.test_date, None)
        test_gps_date = date(1999,12,19)
        test_gps_time = time(22,38,12)
        actual = time_utils.calculateTimestamp(test_gps_date, test_gps_time, 1174.835)
        expected = datetime.combine(self.test_date, test_gps_time, tzinfo=timezone.utc)
        self.assertEqual(expected, actual, 'Time calculated timestamp did not match the expected value.')

    def testCalculateTimestampNoInput1(self):
        time_utils = TimeUtils(None, None)
        actual = time_utils.calculateTimestamp(None, None, 140.320)
        self.assertIsNone(actual, 'The calculated timestamp was expected to be None.')
        
    def testCalculatedTimestampNoInput2(self):
        time_utils = TimeUtils(None, None)
        test_gps_date = date(1999,12,19)
        actual = time_utils.calculateTimestamp(test_gps_date, None, 1432.938)
        self.assertIsNone(actual, 'The calculated timestamp was expected to be None.')
        
    def testCalculatedTimestampNoInput3(self):
        time_utils = TimeUtils(None, None)
        test_gps_time = time(22,38,12)
        actual = time_utils.calculateTimestamp(None, test_gps_time, 2273.431)
        self.assertIsNone(actual, 'The calculated timestamp was expected to be None.')

    def testCalculatedTimestampNoInput4(self):
        time_utils = TimeUtils(None, None)
        test_gps_date = date(2019,8,19)
        test_gps_time = time(22,38,12)
        actual = time_utils.calculateTimestamp(test_gps_date, test_gps_time, 1174.835)
        expected = datetime.combine(test_gps_date, test_gps_time, timezone.utc)
        self.assertEqual(expected, actual, 'Time calculated timestamp did not match the expected value.')
        
    def testPosixTimestamp(self):
        test_datetime = datetime(1970, 7, 1, 0, 0, 0, tzinfo=timezone.utc)
        actual = test_datetime.timestamp()
        self.assertEqual(15638400, actual, 'Basic python conversion to Posix timestamp fails.')
         
    def testInfluxDbTimestamp(self):
        test_datetime = datetime(2019,8,15,23,21,30,tzinfo=timezone.utc)
        actual = TimeUtils.influxDBTimestamp(test_datetime)
        self.assertEqual(1565911290000, actual, 'The conversion to InfluxDB timestamp did not return the expected value.')
        
    def testInfluxDbTimestampMillisecond(self):
        test_datetime = datetime(2019,8,20,12,12,12,531000,tzinfo=timezone.utc)
        actual = TimeUtils.influxDBTimestamp(test_datetime)
        self.assertEqual(1566303132531, actual, 'The conversion to InfluxDB timestamp did not return the expected value.')

    def testInfluxDbTimestampMicrosecond(self):
        test_datetime = datetime(2019,8,20,12,12,12,531999,tzinfo=timezone.utc)
        actual = TimeUtils.influxDBTimestamp(test_datetime)
        # currently truncates, consider rounding
        self.assertEqual(1566303132531, actual, 'The conversion to InfluxDB timestamp did not return the expected value.')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()