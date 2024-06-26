def money_buckets(): #Money Buckets Function
    income = float(input("What is your income? "))
    blow = round(income * 0.6, 2)        #60% of income
    dailyexpenses = round(blow * 0.6, 2) #60% of blow
    splurge = round(blow * 0.1, 2)       #10% of blow
    smile = round(blow * 0.1, 2)         #10% of blow
    firex = round(blow * 0.2, 2)         #20% of blow
    grow = round(income * 0.2, 2)        #20% of income
    mojo = round(income * 0.2, 2)        #20% of income
    print(f"Blow: ${blow}")
    print(f"Daily Expenses: ${dailyexpenses}")
    print(f"Splurge: ${splurge}")
    print(f"Smile: ${smile}")
    print(f"Fire Extinguisher: ${firex}")
    print(f"Grow: ${grow}")
    print(f"Mojo: ${mojo}")              #Printing out all of the values
    choices()              #shows feature options at the end
    return

def compound_interest():
    savings = 0                         #Starts savings at 0
    age = int(input("What age did you start investing? "))
    rate = float(input("What is the average annual return? "))
    investment = float(input("Amount you invest every year: "))

    print("Age      Rate     Savings")
    while age <= 60:
        savings = savings + investment + (savings + investment) * (rate/100)
        print(f"{age}       {rate}%      ${round(savings, 2)}") #Prints in a table format
        age += 1 #increase age for every year
    choices()    #shows feature options at the end
    return

def choices():
    print("Another Feature?")
    print("1 - MoneyBuckets")
    print("2 - CompoundInterest")
    print("3 - Finish")
    return

print("***********************************************")
print("$                Money Maneger                $")
print("***********************************************")
print("Choose Feature")
print("1 - Money Buckets")
print("2 - Compound Interest")
print("3 - Finish App")
choice = input("Feature: ")         #Gets users feature choice

while choice != "":
    if choice == "1" or choice == "Money Buckets":
        money_buckets()             #if choice is 1 play money buckets
        choice = input("Feature: ")
    elif choice == "2" or choice == "Compound Interest":
        compound_interest()         #if choice is 2 play compound interest
        choice = input("Feature: ")
    elif choice == "3" or choice == "Finish App":
        choice = ""                 #ends the loop
    else:
        print("Invalid - Try again") #makes sure input is valid
        choice = input("Feature: ")
print("Thank you for using Money Manger.")