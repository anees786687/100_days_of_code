print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

amt_to_pay = (total + (total * tip / 100)) / people

print(f"Each person should pay: ${"{:.2f}".format(amt_to_pay)}")