import re

hand = open("haystack.txt")
numlist = list()

for line in hand:
    line = line.rstrip()
    numstring = re.findall("[0-9.]+", line)  # Corrected regex pattern
    if len(numstring) != 1:
        continue
    num = float(numstring[0])  # Corrected variable name
    numlist.append(num)

print("Sum:", sum(numlist))

