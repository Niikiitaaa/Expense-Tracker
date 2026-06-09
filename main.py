import csv
import os

FILE_NAME = "transactions.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Category", "Amount"])

while True:

    print("\n" + "=" * 40)
    print("          EXPENSE TRACKER")
    print("=" * 40)

    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Show Net Balance Report")
    print("4. Category-wise Spending Report")
    print("5. Clear All Transactions")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # -----------------------------------
    # ADD TRANSACTION
    # -----------------------------------

    if choice == "1":

        print("\nTransaction Type")
        print("1. Expense")
        print("2. Refund / Cash Inflow")

        transaction_choice = input("Choose type: ")

        if transaction_choice == "1":
            transaction_type = "Expense"

        elif transaction_choice == "2":
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

        category_choice = input("Choose category: ")

        categories = {
            "1": "Food",
            "2": "Travel",
            "3": "Shopping",
            "4": "Bills",
            "5": "Other"
        }

        if category_choice not in categories:
            print("Invalid category!")
            continue

        category = categories[category_choice]

        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

        except ValueError:
            print("Invalid amount!")
            continue

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([transaction_type, category, amount])

        print("Transaction saved successfully!")

    # -----------------------------------
    # VIEW TRANSACTIONS
    # -----------------------------------

    elif choice == "2":

        print("\nTRANSACTION HISTORY")
        print("-" * 50)

        count = 0

        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)
            next(reader)

            for row in reader:

                print(
                    f"Type: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]}"
                )

                count += 1

        if count == 0:
            print("No transactions found.")

    # -----------------------------------
    # NET BALANCE REPORT
    # -----------------------------------

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
        print("-" * 40)

        print(f"Total Expenses : ₹{total_expenses}")
        print(f"Total Refunds  : ₹{total_refunds}")
        print(f"Net Balance    : ₹{net_balance}")

    # -----------------------------------
    # CATEGORY-WISE SPENDING REPORT
    # -----------------------------------

    elif choice == "4":

        category_totals = {}

        with open(FILE_NAME, "r") as file:

            reader = csv.reader(file)
            next(reader)

            for row in reader:

                transaction_type = row[0]
                category = row[1]
                amount = float(row[2])

                if transaction_type == "Expense":

                    if category not in category_totals:
                        category_totals[category] = 0

                    category_totals[category] += amount

        print("\nCATEGORY-WISE SPENDING REPORT")
        print("-" * 40)

        if len(category_totals) == 0:
            print("No expense records found.")

        else:

            for category, amount in category_totals.items():
                print(f"{category:<12}: ₹{amount}")

    # -----------------------------------
    # CLEAR ALL TRANSACTIONS
    # -----------------------------------

    elif choice == "5":

        confirm = input(
            "Are you sure you want to delete all transactions? (yes/no): "
        )

        if confirm.lower() == "yes":

            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Type", "Category", "Amount"])

            print("All transactions cleared.")

        else:
            print("Operation cancelled.")

    # -----------------------------------
    # EXIT
    # -----------------------------------

    elif choice == "6":

        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")