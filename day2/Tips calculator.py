print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: $"))
tip = int(input("What percentage tip would you like to give? Options are 10, 12, 15: "))
people = int(input("How many people to split the bill? : "))

sumPerPerson = (bill + (bill*tip/100) )/ people
print(f"Each person should pay: ${sumPerPerson}")