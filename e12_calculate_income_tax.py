income = 45000.0
tax = 0

if income <=10000:
    tax = 0
elif income > 10000 and income <= 20000:
    tax = (income - 10000) * .1
else:
    tax = 10000 * 0.1 + (income - 20000) * .2

print("Given Income is $",income) 
print("Total tax to pay is $",tax) 
