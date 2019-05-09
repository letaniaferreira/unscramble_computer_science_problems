"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

all_numbers_called = []
calls_to_bangalore = []
mobile_codes_called = []
telemarketers_called = []
area_code_called = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
num_calls_from_bangalore = 0

for line in calls:
    if line[0].startswith('(080)'):
        all_numbers_called.append(line[1])
        num_calls_from_bangalore += 1
        if line[1].startswith('(080)'):
          calls_to_bangalore.append(line[1])
        if line[1].startswith('7') or line[1].startswith('8') or line[1].startswith('9'):
          mobile_codes_called.append(line[1][:4])
        if line[1].startswith('('):
          area_code_called.append(re.findall(r'\(.*?\)', line[1]))
    

#clean extra characters and remove duplicates from area_code_called
set_area_code_called = []

for code in area_code_called:
  if code[0] not in set_area_code_called:
    set_area_code_called.append(code[0])

for area_code in mobile_codes_called:
  if area_code not in set_area_code_called:
    set_area_code_called.append(area_code)

codes_called_by_bangalore = []
for code in set_area_code_called:
  code = code.replace('(', '')
  code = code.replace(')', '')
  codes_called_by_bangalore.append(code)


#get percentage of calls made from and to Bangalore numbers
calls_within_bangalore = round((len(calls_to_bangalore)/num_calls_from_bangalore) * 100, 2)


print("The numbers called by people in Bangalore have codes:")
for code in sorted(codes_called_by_bangalore):
  print(code)
print('\n')
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(calls_within_bangalore))



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

