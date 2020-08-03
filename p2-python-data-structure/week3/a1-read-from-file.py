# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.

filename = input("Please enter filename: ")
try:
    file = open(filename)
except:
    print("Invalid file name.")
    quit()

for line in file:
    print(line.strip().upper())