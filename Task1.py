"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

phone_numbers =[]

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for num in texts:
        if num[0] not in phone_numbers:
            phone_numbers.append(num[0])
        if num[1] not in phone_numbers:
            phone_numbers.append(num[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for number in calls:
        if number[0] not in phone_numbers:
            phone_numbers.append(number[0])
        if number[1] not in phone_numbers:
            phone_numbers.append(number[1])

print("There are {} different telephone numbers in the records.".format(len(phone_numbers)))



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
