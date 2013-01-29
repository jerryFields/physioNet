'''
Created on Jan 29, 2013

@author: JerrySoto
'''
import csv
import numpy as np
import math
#from separate_column import *

import sys
csv.field_size_limit(sys.maxint)

inputPath='C:\Users\JerrySoto\Desktop\VPS\physioNet_MIT_challenge2012\set-a'

fileName='132539.txt'

inFileName=inputPath+'\\'+fileName

InFile = open(inFileName,'rb')
csvRead = csv.reader(InFile,delimiter=',')

temp=csvRead.next()


