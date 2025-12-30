import csv
import os

FILENAME = "expenses.csv"
expenses = []


def load_expenses():
    """Load expenses from CSV file into memory"""
    if not os.path.exists(FILENAME):
        return

    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            amount, category, note = row
            expenses.append({
                "amount": float(amount),
                "category": category,
                "note": note
            })


def save_expenses():
    """Save all expenses from memory to CSV file"""
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        for exp in expenses:
            writer.writerow([exp["amount"], exp["category"], exp["note"]])


def add_expense():
    """Add a new expense"""
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    category = input("Enter category: ")
    note = input("Enter note: ")

    expenses.append({
        "amount": amount,
        "category": category,
        "note": note
    })

    save_expenses()
    print("✅ Expense added successfully.")


def view_expenses():
    """Display all expenses"""
    if not expenses:
        print("📭 No expenses found.")
        return

    print("\n📋 Expense List:")
    for i, exp in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']}"
        )


def calculate_total():
    """Calculate total expense"""
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Expense: ₹{total}")


def show_menu():
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")


def main():
    load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
