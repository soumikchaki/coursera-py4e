import re

try:
    file = open("regex_sum.txt")
except:
    print("Invalid File.")
    quit()

numbers = re.findall("([0-9]+)", file.read())
total = sum([int(item) for item in numbers])
print(total)