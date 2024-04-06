def money_buckets():
    income = int(input("What is your income? "))
    blow = round(income * 0.6, 2)
    dailyexpenses = round(blow * 0.6, 2)
    splurge = round(blow * 0.1, 2)
    smile = round(blow * 0.1, 2)
    firex = round(blow * 0.2, 2)
    grow = round(income * 0.2, 2)
    mojo = round(income * 0.2, 2)
    print(f"Blow: ${blow}")
    print(f"Daily Expenses: ${dailyexpenses}")
    print(f"Splurge: ${splurge}")
    print(f"Smile: ${smile}")
    print(f"Fire Extinguisher: ${firex}")
    print(f"Grow: ${grow}")
    print(f"Mojo: ${mojo}")
    return

def compound_interest():
    savings = 0
    age = int(input("What age did you start investing? "))
    rate = int(input("What is the average annual return? "))
    investingamount = int(input("Amount you invest every year: "))

    print("Age      Rate     Savings")
    while age <= 60:
        savings = savings + investingamount + (savings + investingamount) * (rate/100)
        print(f"{age}       {rate}%      ${round(savings, 2)}")
        age += 1
    return

print("***********************************************")
print("$                Money Maneger                $")
print("***********************************************")


print("Choose Feature")
print("1 - MoneyBuckets")
print("2 - CompoundInterest")
choice = input("Feature: ")

def choose():
    print("Another Feature?")
    print("1 - MoneyBuckets")
    print("2 - CompoundInterest")
    print("3 - Finish")
    choice = input("Feature: ")
    return

while choice != "":
    if choice == "1":
        money_buckets()
        choose()
    elif choice == "2":
        compound_interest()
        choose()
    elif choice == "3":
        choice = ""
    else:
        print("Invalid - Try again")
        choice = input("App: ")
print("Thank you for using Money Manger.")