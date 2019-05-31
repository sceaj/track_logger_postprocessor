'''
Created on May 22, 2019

@author: sceaj
'''

class Enum(tuple): __getattr__ = tuple.index
