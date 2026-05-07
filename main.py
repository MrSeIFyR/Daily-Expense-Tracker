expenses = []

print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

while True:
    choice = int(input("Enter the number from the menu above: "))
    if choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    if choice == 1:
        expense = float(input("Add an expense: "))
        expenses.append(expense)
        print("Expense added successfully!")
    if choice == 2:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")
    if choice == 3:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            total_expense = 0
            average_expense = 0
            for index in expenses:
                total_expense += index
            average_expense = total_expense / len(expenses)
            print(f"Total expense: {total_expense}")
            print(f"Average expense: {average_expense}")