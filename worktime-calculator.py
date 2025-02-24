import datetime
import json


class Shift:
    lst_of_shifts : list = []
    def __init__(self, start_time, end_time, lst_of_breaks, weekday):
        self.start = None
        self.end = None
        self.breaks = None
        self.weekday = None

    def calcule_surcharges(self):
        pass

class Break:
    def __init__(self, start_time, end_time):
        self.start = None
        self.end = None


shifts : dict = None
with open('worktime.json', 'r') as f:
    shifts = json.loads(f.read())




for item in shifts:
    shift : dict = item
    start_timestamp_raw = shift['startTime']
    start_timestamp : datetime = datetime.datetime.fromtimestamp(int(start_timestamp_raw/1000))
    # print('Starttime:',start_timestamp, type(start_timestamp))

    end_timestamp_raw = shift['endTime']
    end_timestamp = datetime.datetime.fromtimestamp(int(end_timestamp_raw/1000))
    # print('Endtime:', end_timestamp, type(end_timestamp))

    breaks_raw = shift['breaks']
    lst_of_breaks : list = []
    for single_break in breaks_raw:
        single_break : dict = single_break
        brk = Break(datetime.datetime.fromtimestamp(int(single_break['start']/1000)), datetime.datetime.fromtimestamp(int(single_break['end']/1000)))
        lst_of_breaks.append(brk)
        # print('breaks:', single_break, single_break.values(), type(single_break))
    weekday = start_timestamp.weekday()
    print(weekday)
    break

