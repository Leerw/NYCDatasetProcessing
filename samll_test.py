import numpy as np
from GPSUtils import gps_to_xy, pgps_to_xy, gps_distance
from utils import generate_dates, get_timeslots
from stresnet import print_time, get_next, process

'''
time_slots = get_timeslots(2015, 10, 2016, 1, 2)
print(time_slots[0:48], time_slots[-48:])
'''

print_time()
print(get_next(2015, 12))

'''
orlon = -74.038971
orlat =  40.709279
tllon = -73.96834326
tllat =  40.81703286
brlon = -73.996317
brlat =  40.68132125
trlon = -73.92568926
trlat =  40.78907511

orcorner_g = tuple([round(ii, 4) for ii in gps_to_xy(orlon, orlat)])
tlcorner_g = tuple([round(ii, 4) for ii in gps_to_xy(tllon, tllat)])
brcorner_g = tuple([round(ii, 4) for ii in gps_to_xy(brlon, brlat)])
trcorner_g = tuple([round(ii, 4) for ii in gps_to_xy(trlon, trlat)])
orcorner_p = tuple([round(ii, 4) for ii in pgps_to_xy(orlon, orlat)])
tlcorner_p = tuple([round(ii, 4) for ii in pgps_to_xy(tllon, tllat)])
brcorner_p = tuple([round(ii, 4) for ii in pgps_to_xy(brlon, brlat)])
trcorner_p = tuple([round(ii, 4) for ii in pgps_to_xy(trlon, trlat)])


print(orcorner_g)
print(orcorner_p)

print(tlcorner_g)
print(tlcorner_p)

print(trcorner_g)
print(trcorner_p)

print(brcorner_g)
print(brcorner_p)
'''