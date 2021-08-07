# Constants used throughout the app

from collections import OrderedDict 

# ditance to cost mapper 
# dist (m) : cost (paise)
DISTANCE_FEE_DICT = {
    10000 : 5000,
    20000 : 10000,
    50000 : 50000,
}

DISTANCE_FEE_BEYOND_THRESHOLD = 100000 # in paise