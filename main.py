import csv
import os

FILE_NAME = "transactions.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Category", "Amount"])

while True:

    print("\n" + "=" * 40)
    print("         EXPENSE TRACKER")
    print("=" * 40)

    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Show Net Balance Report")
    print("4. Clear All Transactions")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # --------------------------
    # ADD TRANSACTION
    # --------------------------
    if choice == "1":

        print("\nTransaction Type")
        print("1. Expense")
        print("2. Refund / Cash Inflow")

        t_choice = input("Choose type: ")

        if t_choice == "1":
            transaction_type = "Expense"
        elif t_choice == "2":
            transaction_type = "Refund"
        else:
            print("Invalid transaction type!")
            continue

        print("\nCategories")
        print("1. Food")
        print("2. Travel")
        print("3. Shopping")
        print("4. Bills")
        print("5. Other")

        c_choice = input("Choose category: ")

        categories = {
            "1": "Food",
            "2": "Travel",
            "3": "Shopping",
            "4": "Bills",
            "5": "Other"
        }

        category = categories.get(c_choice)

        if not category:
            print("Invalid category!")
            continue

        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            with open(FILE_NAME, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([transaction_type, category, amount])

            print("Transaction saved successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    # --------------------------
    # VIEW TRANSACTIONS
    # --------------------------
    elif choice == "2":

        print("\nTRANSACTION HISTORY")
        print("-" * 55)

        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            next(reader)

            count = 0

            for row in reader:

                print(
                    f"Type: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]}"
                )

                count += 1

            if count == 0:
                print("No transactions found.")

    # --------------------------
    # NET BALANCE REPORT
    # --------------------------
    elif choice == "3":

        total_expenses = 0
        total_refunds = 0

        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                transaction_type = row[0]
                amount = float(row[2])

                if transaction_type == "Expense":
                    total_expenses += amount

                elif transaction_type == "Refund":
                    total_refunds += amount

        net_balance = total_refunds - total_expenses

        print("\nNET BALANCE REPORT")
        print("-" * 30)
        print(f"Total Expenses : ₹{total_expenses}")
        print(f"Total Refunds  : ₹{total_refunds}")
        print(f"Net Balance    : ₹{net_balance}")

    # --------------------------
    # CLEAR ALL TRANSACTIONS
    # --------------------------
    elif choice == "4":

        confirm = input(
            "\nWARNING! This will delete all transactions.\nAre you sure? (y/n): "
        )

        if confirm.lower() == "y":

            with open(FILE_NAME, "w", newline="") as file:

                writer = csv.writer(file)
                writer.writerow(["Type", "Category", "Amount"])

            print("All transactions cleared successfully!")

        else:
            print("Operation cancelled.")

    # --------------------------
    # EXIT
    # --------------------------
    elif choice == "5":

        print("\nThank you for using Expense Tracker!")
        break

    # --------------------------
    # INVALID CHOICE
    # --------------------------
    else:

        print("Invalid choice. Please try again.")