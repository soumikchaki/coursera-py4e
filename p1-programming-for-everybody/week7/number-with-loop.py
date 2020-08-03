# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except
# and put out an appropriate message and ignore the number.

ln = 0
sn = 5
fm = 0

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    else :
        try:
            fm = int(num)
            if (fm>ln) :
                ln = fm
            if (fm<sn) :
                sn = fm
        except:
            print("Invalid input")
            continue

print("Maximum is", ln)
print("Minimum is", sn)