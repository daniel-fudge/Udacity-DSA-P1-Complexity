"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
Run time analysis:
O(4) 
"""

sender, receiver, date = texts[0]
print(f"First record of texts, {sender} texts {receiver} at time {date}")

sender, receiver, date, duration = calls[-1]
print(f"Last record of calls, {sender} calls {receiver} at time {date}, lasting {duration} seconds")
