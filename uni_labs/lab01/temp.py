app_name = "Personal Expense Tracker"
total_expenses = 0
running = True
monthly_budget = 5000          # fixed budget we'll compare against

print("Welcome to ",app_name," !\n")

expenses = []
allowed_categories = ("Food", "Transport", "Bills", "Shopping", "Other")
print("Allowed expense categories:",allowed_categories,"\n")


def add_expense():
    global total_expenses
    category = input(f"Enter category {allowed_categories}: ").title().strip()

    if category not in allowed_categories:
        print("Invalid category! Including in category 'Other'.\n")
        category = "Other"
    try:
        amount = float(input("Enter amount spent in Rs : "))
    except ValueError:
        print("Invalid amount entered. Expense not added.\n")
        return

    note = input("Add a short note: ").strip()

    entry = {"category": category, "amount": amount, "note": note}
    expenses.append(entry)

    # Now we use some operators for calculations or comparisiions as in task 5
    total_expenses = total_expenses + amount          
    remaining_budget = monthly_budget - total_expenses  

    if amount > 5000:                                  
        print("That's a big expense! Make sure to budget carefully.")
    elif amount == 0:                                    
        print("Zero amount recorded.")
    else:
        print("Expense added successfully!")

    if remaining_budget < 0 and total_expenses >monthly_budget:
        print("Warning: You have exceeded your budget by Rs ", abs(remaining_budget)," !")
    else:
        print("You have Rs ",remaining_budget," left in your budget.")
    print()


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    average = total_expenses / len(expenses)   # division operator

    print("\n---- All Recorded Expenses ----")
    for index, entry in enumerate(expenses, start=1):
        # modulo operator: mark every 2nd entry with a small tag, just for style
        tag = " *" if index % 2 == 0 else ""

        # flag any expense above the average
        flag = " (above average)" if entry["amount"] > average else ""

        print(index, tag, "-", entry['category'], " | Rs", entry['amount'], " | ", entry['note'], flag)

    print("--------------------------------")
    print("TOTAL SPENT: Rs ", total_expenses)
    print("AVERAGE per expense: Rs ", round(average, 2))
    print("BUDGET STATUS:", "Over budget" if total_expenses > monthly_budget else "Within budget", "\n")


while running:
    print("MENU")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("\nThank you for using the Expense Tracker. Goodbye!")
        running = False   # this stops the while loop
    else:
        print("Invalid choice, please enter 1, 2, or 3.\n")