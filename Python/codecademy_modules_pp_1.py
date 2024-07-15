import datetime
import time
time_string = "08/01/2011"

time_stamp = False
time_stamp = time.mktime(datetime.datetime.strptime(time_string, "%d/%m/%Y").timetuple())
print(time_stamp)