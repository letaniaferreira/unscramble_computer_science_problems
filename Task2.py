"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
phone_dict = {}
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for num in calls:
        if num[0] not in phone_dict:
            phone_dict[num[0]] = int(num[-1])
        else:
            phone_dict[num[0]] += int(num[-1])
        if num[1] not in phone_dict:
            phone_dict[num[1]] = int(num[-1])
        else:
            phone_dict[num[1]] += int(num[-1])

values = []

for key, value in phone_dict.items():
    values.append(value)

max_value = max(values)

for key, value in phone_dict.items():
    if value == max_value:
        print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key, max(values)))




"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

