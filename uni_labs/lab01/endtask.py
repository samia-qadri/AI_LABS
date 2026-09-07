app_name= "Personal Expense Tracker"
total_expenses =0
running = True
monthly_budget= 50000         # fixed budget for comparision

print("Welcome to ",app_name," !\n")
expenses = []
allowed_categories=("Food","Transport","Bills","Shopping","Other")
print("Allowed expense categories:", allowed_categories, "\n")

#to add expenses
def add_expense():
    global total_expenses
    category= input(f"Enter category{allowed_categories}: ").title().strip()

    if category not in allowed_categories:
        print("Invalid category! Including in category 'Other'.\n")
        category="Other"
    try:
        amount=float(input("Enter amount spent in Rs: "))
    except ValueError:
        print("Invalid amount entered. Expense not added.\n")
        return

    note= input("Add a short note: ").strip()
    entry = {"category": category,"amount": amount,"note": note}
    expenses.append(entry)

    total_expenses= total_expenses + amount          # addition operator
    remaining_budget= monthly_budget - total_expenses  # subtraction operator

    if (amount >15000):                                   # comparison operator
        print("That's a big expense! Make sure to budget carefully.")
    elif (amount == 0):                                    # comparison operator
        print("Zero amount recorded.")
    else:
        print("Expense added successfully!")
        
    # checking budget status
    if remaining_budget< 0 and total_expenses >monthly_budget:
        print("Warning: You have exceeded your budget by Rs", abs(remaining_budget))
    else:
        print("You have Rs ",remaining_budget, " left in your budget.")
    print("")
    
# to view/check expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    average= total_expenses/len(expenses)   

    print("\n---- All Recorded Expenses ----")
    for index, entry in enumerate(expenses, start=1):
        # flag expense above the average
        flag = " (above average)" if entry["amount"] > average else ""

        print(index,". ", entry['category'], " | Rs", entry['amount'], " | ", entry['note'], flag)

    print("--------------------------------")
    print("TOTAL SPENT: Rs ", total_expenses)
    print("AVERAGE per expense: Rs ", round(average, 2))     
    print("BUDGET STATUS:")
    if(total_expenses >monthly_budget):
        print("   Over budget")
    else:
        print("   Within budget")

while running:
    print(" === MENU === ")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Quit")
    
    choice=input("Enter your choice (1-3): ").strip()

    if choice== "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice =="3":
        print("\nThank you for using the Expense Tracker.Exiting the program!")
        running = False   
    else:
        print("Invalid choice, please enter 1, 2, or 3.\n")
        
        
        
        
        
