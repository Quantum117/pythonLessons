import json
import os
import csv

class Account:
    def __init__(self, account_number, name, balance):
        """Initialize an account with account number, name, and balance."""
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        """Convert account details to a dictionary for serialization."""
        return {
            'account_number': self.account_number,
            'name': self.name,
            'balance': self.balance
        }

    @staticmethod
    def from_dict(data):
        """Create an Account object from a dictionary."""
        return Account(data['account_number'], data['name'], data['balance'])

class Bank:
    def __init__(self):
        """Initialize the Bank with a dictionary to store accounts and load existing accounts from file."""
        self.accounts = {}
        # when instantiated load content from a file
        self.load_from_file()

    @staticmethod
    def initialize_bank():
        """Encapsulate bank initialization logic in a separate function."""
        bank = Bank()  # Try to create the Bank object
        if bank.accounts is None:
            return None
        return bank


    def create_account(self, name, initial_deposit):
        """Create a new account with a unique account number and initial deposit."""
        account_number = self.generate_account_number()
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be non-negative.")
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account

        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        """View details of an account given its account number."""
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        """Deposit a specified amount into an account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        account = self.accounts.get(account_number)
        if account:
            account.balance += amount

            print(f"Deposit successful! New balance: {account.balance}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        """Withdraw a specified amount from an account, ensuring sufficient funds."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        account = self.accounts.get(account_number)
        if account:
            if account.balance >= amount:
                account.balance -= amount

                print(f"Withdrawal successful! New balance: {account.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def save_to_file(self):
        """Save all account data to a CSV file."""
        with open("accounts.csv", mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['account_number', 'name', 'balance'])
            writer.writeheader()
            for account in self.accounts.values():
                writer.writerow(account.to_dict())

    def load_from_file(self):
        """Load account data from a CSV file into the application."""
        if os.path.exists("accounts.csv"):
            try:
                with open("accounts.csv", mode='r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        account = Account(int(row['account_number']), row['name'], float(row['balance']))
                        self.accounts[account.account_number] = account
            except Exception as e:
                print(f"An error occurred while loading accounts: {e}")
                self.accounts = None
        else:
            print("file not found found.")


    def generate_account_number(self):
        """Generate a truly unique account number."""
        existing_numbers = set(self.accounts.keys())
        account_number = len(self.accounts) + 1
        # increment to 1 until unique account number achieved and once achieved break the loop
        while True:
            if account_number not in existing_numbers:
                break
            account_number += 1

        return account_number

    def view_all_accounts(self):
        """View details of all accounts in the bank."""
        if not self.accounts:
            print("No accounts available.")
        else:
            print("All Accounts:")
            for account in self.accounts.values():
                print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")