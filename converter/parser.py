'''
Created on May 20, 2019

@author: sceaj
'''
from parsers.accelerometer_parser import AccelerometerParser
from parsers.can_frame_parser import CanFrameParser
from parsers.nmea_parser import NmeaParser

class Parser(object):
    '''
    classdocs
    '''

    def __init__(self, state):
        '''
        Constructor
        '''
        self.state = state
        
    def parse(self, sentence):
        sentence_type = sentence.split(",")[0]
        parser = ParserFactory.getParser(sentence_type, self.state)
        if parser is not None:
            parser.parse(sentence)
        
class ParserFactory:
    
    @staticmethod
    def getParser(sentence_type, state):
        parser = None
        if sentence_type.startswith('$GP'):
            parser = NmeaParser(state)
        elif sentence_type == '$AC001':
            parser = AccelerometerParser(state)
        elif sentence_type == '$CNDRV':
            parser = CanFrameParser(state)
#        else:
        return parser
        
        