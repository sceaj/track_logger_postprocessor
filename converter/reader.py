'''
Created on May 20, 2019

@author: jeff
'''

class DataReader(object):
    '''
    classdocs
    '''


    def __init__(self, paths):
        '''
        Constructor
        '''
        self.paths = paths
        
    def process(self):
        for path in self.paths:
            print "Processing {0}".format(path)
            with open(path, "r") as f:
                for data_line in f:
                    print data_line.strip()
