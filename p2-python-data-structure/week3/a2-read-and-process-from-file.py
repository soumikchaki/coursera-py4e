# Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

filename = input("Please enter filename: ")
try:
    file = open(filename)
except:
    print("Invalid file name.")
    quit()

counter = 0
spam = 0.0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        value = line
        value = value.replace("X-DSPAM-Confidence:", "").strip()
        spam = spam + float(value)
        counter = counter + 1

print("Average spam confidence:", (spam/counter))