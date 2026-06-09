transactions = []

while True:

    print("\n EXPENSE TRACKER")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Show Net Balance Change")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nTransaction Type")
        print("1. Expense")
        print("2. Refund / Cash Inflow")

        transaction_type = input("Choose type: ")

        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            if transaction_type == "1":
                transactions.append(-amount)
                print("Expense added successfully!")

            elif transaction_type == "2":
                transactions.append(amount)
                print("Refund/Cash inflow added successfully!")

            else:
                print("Invalid transaction type.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":

        if len(transactions) == 0:
            print("No transactions recorded.")

        else:
            print("\nTransactions:")

            for i, amount in enumerate(transactions, start=1):

                if amount < 0:
                    print(f"{i}. Expense: ₹{-amount}")

                else:
                    print(f"{i}. Refund/Cash Inflow: ₹{amount}")

    elif choice == "3":

        net_balance = sum(transactions)

        print(f"\nNet Balance Change: ₹{net_balance}")

        if net_balance < 0:
            print(f"Overall Spending: ₹{-net_balance}")

        elif net_balance > 0:
            print(f"Overall Gain: ₹{net_balance}")

        else:
            print("No net change.")

    elif choice == "4":

        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")