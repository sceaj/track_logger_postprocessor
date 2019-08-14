'''
Created on Aug 11, 2019

@author: Jeffrey
'''
from formatters.csv_formatter import CsvFormatter
from formatters.influxdb_formatter import InfluxDbFormatter

class FormatterFactory:
    
    @staticmethod
    def getFormatter(output_format, tags):
        formatter = None
        if output_format == 'CSV':
            formatter = CsvFormatter(tags)
        elif output_format == 'INFLUXDB':
            formatter = InfluxDbFormatter(tags)
#        else:
        return formatter
        
       