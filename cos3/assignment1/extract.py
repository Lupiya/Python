import re

hand = open("haystack101.txt")
numlist = list()

for line in hand:
    line = line.rstrip()
    numstrings = re.findall(r"[0-9]+", line)  # Corrected regex pattern
    for numstring in numstrings:
        num = float(numstring)
        numlist.append(num)

print("Sum:", sum(numlist))



