import csv
from datetime import datetime

monthly_income = 0
user_expenses = {
        "Food": {},
        "Transport": {},
        "Personal": {},
        "Entertainment": {},
        "Other": {}
    }
category_thresholds = {
    "Food": 0,
    "Transport": 0,
    "Personal": 0,
    "Entertainment": 0,
    "Other": 0
}

def display_menu():
    print("\n====== Budget planner =======")
    print(f"Your income: {monthly_income}")
    print("1. Add income")
    print("2. Add expenses")
    print("3. Set category thresholds")
    print("4. View expenses")
    print("5. Balance remaining")
    print("6. Search category")
    print("7. Generate report")
    print("8. Exit")

# Add income
def add_income():
    try:
        global monthly_income
        income = float(input("Enter your income: "))
        if income <= 0:
            print("Error: Income must be greater than 0")
            return
        monthly_income = income
        print(f"Income successfully updated to R{income:.2f}")
    except ValueError:
        print("Error: Invalid value")

# Add expenses
def add_expenses():
    try:
        num_expenses = int(input("Enter number of expenses: "))
        if num_expenses <= 0:
            print("Error: Number of expenses must be greater than 0")
            return
        for i in range(num_expenses):
            expense = input("Enter name of expense: ")
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Error: Amount must be greater than 0")
                return
            # User gets to pick category
            print("\n Pick category")
            print("1: Food")
            print("2: Transport")
            print("3: Personal")
            print("4: Entertainment")
            print("5: Other")

            category = input("Enter category: ")
            if category == "1":
                user_expenses["Food"][expense] = amount
            elif category == "2":
                user_expenses["Transport"][expense] = amount
            elif category == "3":
                user_expenses["Personal"][expense] = amount
            elif category == "4":
                user_expenses["Entertainment"][expense] = amount
            elif category == "5":
                user_expenses["Other"][expense] = amount
            else:
                print("Invalid category. Please try again.")
                return
            print(f"Expense added to category: {category}")

    except ValueError:
        print("Error: Invalid value")

# User can set threshold for each category
def set_category_threshold():
    print("\n=== Set Category Thresholds ===")
    for category in category_thresholds:
        try:
            threshold = float(input(f"Enter threshold for {category} (R): "))
            if threshold < 0:
                print("Threshold cannot be negative")
                continue
            category_thresholds[category] = threshold
            print(f"Threshold for {category} set to R{threshold:.2f}")
        except ValueError:
            print("Invalid input. Threshold not set for this category.")

def get_category_total(category):
    return sum(user_expenses[category].values())

# Checks if total expenses for a category exceeds threshold
def check_threshold(category):
    total = get_category_total(category)
    threshold = category_thresholds[category]
    if threshold > 0 and total > threshold:
        return (f"WARNING: {category} expenses (R{total:.2f}) exceed threshold (R{threshold:.2f})")
    return None

# Displays all expenses and total cost
def view():
    if not user_expenses:
        print("\n No expenses listed yet.")
        return 0

    grand_total = 0
    print("\nExpenses List")
    for category, expense in user_expenses.items():
        total_cost = 0
        if expense:
            print(f"--- Category: {category} ---")
            for expense_name, amount in expense.items():
                print(f" - {expense_name}: R{amount:.2f}")
                total_cost += amount
            print(f"\n {category} total cost: R{total_cost:.2f} ---")
            grand_total += total_cost
            warning = check_threshold(category)
            if warning:
                print(warning)
            print()

    print(f"Grand total: R{grand_total:.2f}")
    return grand_total

# Calculates grand total without printing anything
def get_grand_total():
    grand_total = 0
    for category, expense in user_expenses.items():
        grand_total += sum(expense.values())
    return grand_total

# Shows balance remaining
def balance(income, grand_total):
    print("\n--- Your balance ----")
    print(f"Your income is: R{income:.2f}")
    print(f"Your grand total is: R{grand_total:.2f}")
    balance_remaining = income - grand_total
    print(f"Your remaining balance is: R{balance_remaining:.2f}")

# User can search up category by name
def search():
    search_name = input("Enter name of category: ").strip().lower()
    if not search_name:
        print("Search name cannot be empty")
        return

    found = False
    for category, expenses in user_expenses.items():
        if search_name == category.lower():
            print(f"\nCategory: {category}")
            if not expenses:
                print("-- No expenses listed in this category")
            else:
                category_total = 0
                for expense_name, amount in expenses.items():
                    print(f" - {expense_name}: R{amount:.2f}")
                    category_total += amount
                print(f"\n--- {category} total cost: R{category_total:.2f} ---")

                warning = check_threshold(category)
                if warning:
                    print(warning)
            found = True
            break
    if not found:
        print("Category not found")

# Generates report in csv
def generate_report():
    with open("budget_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Expense", "Amount"])
        for category, expenses in user_expenses.items():
            if not expenses:
                continue
            for expense_name, amount in expenses.items():
                writer.writerow([category, expense_name, amount])
    print("Report generated successfully.")

# Menu screen
def main():
    while True:
        display_menu()
        choice = input("Enter your choice 1-8: ")  # FIX: was "1-6"
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expenses()
        elif choice == "3":
            set_category_threshold()
        elif choice == "4":
            view()
        elif choice == "5":
            # FIX: use get_grand_total() to avoid printing expenses twice
            if not monthly_income:
                print("No income added yet.")
            else:
                total = get_grand_total()
                balance(monthly_income, total)
        elif choice == "6":
            search()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("Exiting the program, Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

main()