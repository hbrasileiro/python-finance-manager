class Transaction:
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.type = type  # 'income' or 'expense'


class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def calculate_balance(self):
        income = sum(transaction.amount for transaction in self.transactions if transaction.type == 'income')
        expenses = sum(transaction.amount for transaction in self.transactions if transaction.type == 'expense')
        return income - expenses

    def list_transactions(self):
        if self.transactions:
            print("Transaction List:")
            for transaction in self.transactions:
                print(f"- {transaction.description}: {transaction.type.capitalize()} of ${transaction.amount:.2f}")
        else:
            print("No transactions recorded.")


def main():
    manager = FinanceManager()

    while True:
        print("\n1. Add Transaction")
        print("2. Calculate Balance")
        print("3. List Transactions")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter transaction description: ")
            amount = float(input("Enter transaction amount: "))
            type = input("Transaction type (income or expense): ").lower()
            if type not in ['income', 'expense']:
                print("Invalid type. Use 'income' or 'expense'.")
                continue

            transaction = Transaction(description, amount, type)
            manager.add_transaction(transaction)
            print("Transaction added successfully!")
        elif choice == "2":
            balance = manager.calculate_balance()
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == "3":
            manager.list_transactions()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
