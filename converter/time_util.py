'''
Created on Aug 15, 2019

@author: Jeffrey
'''

from datetime import datetime
from datetime import timedelta
from datetime import timezone

class TimeUtils(object):
    '''
    Utility class that provides various conversion of timestamps for the track logger data.
    Since different configurations of the track logger may provide different date/time capabilities,
    and also because GPS date/time capabilities can vary with conditions and specific GPS hardware, 
    real-time timestamps are supported by both GPS date/time or datum date/time values supplied at 
    conversion time, or a combination (we have encountered at least 1 GPS module that returns a valid
    time, but a fixed date of 1999-12-17 for some sentences)
    
    Date Datum Supplied    Time Datum Supplied    Timestamp Calculation
          Yes                    Yes              (Date_Datum,Time_Datum) + Elapsed_Time
          Yes                    No               (Date_Datum,GPS_Time) if GPS_Time rolls over midnight Date_Datum is incremented
          No                     Yes              Configuration Error
          No                     No               (GPS_Date,GPS_Time)
          
    Currently we only generate InfluxDB timestamps in millisecond resolution.  In the future, a nice enhancement
    would be to support variable precision of these timestamps, but that would also require changes in the 
    teensy_track_logger since it currently only generates the elapsed time date in 10ms resolution.
    '''

    @staticmethod 
    def influxDBTimestamp(ts_dt):
        # currently only millisecond precision supported
        return int(ts_dt.timestamp() * 1000.0)
    
    def __init__(self, start_date, start_time):
        '''
        Constructor
        '''
        self.date_datum = start_date
        self.time_datum = start_time
        self.last_gps_time = None
        
        
    def calculateTimestamp(self, gps_date, gps_time, time):
        calculation_date = self.date_datum
        calculation_timedelta = timedelta(0, 0)
        if calculation_date is None:
            calculation_date = gps_date
            calculation_time = gps_time
        else:
            if self.time_datum is None:
                calculation_time = gps_time
                if self.last_gps_time is not None and gps_time < self.last_gps_time:
                    self.date_datum += timedelta(1, 0)
                    calculation_date = self.date_datum
                self.last_gps_time = gps_time
            else:
                calculation_time = self.time_datum
                calculation_timedelta = timedelta(0, time)
        if calculation_date is None or calculation_time is None:
            return None
        return datetime.combine(calculation_date, calculation_time, timezone.utc) + calculation_timedelta
    