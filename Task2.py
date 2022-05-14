"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

times = defaultdict(int)
for line in calls:
    times[line[0]] += int(line[3])
    times[line[1]] += int(line[3])
max_number = max(times, key=times.get)
print(f"{max_number} spent the longest time, {times[max_number]} seconds, on the phone during September 2016.")
