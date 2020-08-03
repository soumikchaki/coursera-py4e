# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.

hours = input("Please enter hours worked: ")
rate = input("Please enter per hour rate: ")

if float(hours) > 40:
    gross_pay = (40 * float(rate)) + ((float(hours)-40) * float(rate) * 1.5)
else:
    gross_pay = float(hours) * float(rate)

print("Net Pay:", gross_pay)