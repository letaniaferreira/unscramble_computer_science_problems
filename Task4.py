"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

received_calls = []
sent_texts = []
received_texts = []
telemarketers = set()


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

for line in calls:
    received_calls.append(line[1])

for line in texts:
    received_texts.append(line[1])

for line in texts:
    sent_texts.append(line[0])

for line in calls:
    if line[0] not in sent_texts and line[0] not in received_texts and line[0] not in received_calls:
        telemarketers.add(line[0])

sorted_telemarketers = sorted(telemarketers)
print("These numbers could be telemarketers: ")
for number in sorted_telemarketers:
    print(number + '\n')


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

