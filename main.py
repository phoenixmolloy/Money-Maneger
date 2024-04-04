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
    age = int(input("What age did you start investing? "))
    rate = int(input("What is the average annual return? "))
    investingamount = int(input("Amount you invest every year: "))

    while age <= 60:
        print(savings + )

# Ask user to input their start age when they begin investing
# Ask user for average annual return #(e.g 10%)
# Ask user for amount they will invest every year
#
# WHILE age <= 60
#     Print savings = (savings + investing amount) * (annual return + 100%)
#     age += 1
# ENDWHILE

print("Choose app")
print("1 - MoneyBuckets")
print("2 - CompoundInterest")
choice = input()

while choice != "":
    if choice == "1":
        money_buckets()
    elif choice == "2":
        compound_interest()
    else:
        print("hi")
    #elif choice == "go back":
choice = input("w")