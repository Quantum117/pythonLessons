from Bank import Bank


def main():
    """Main function to provide a command-line interface for the banking application."""
    bank = Bank.initialize_bank()
    if not bank:
        print("Exiting program...")
        return  # Exit if the bank could not be created

    print("\nBanking Application")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. View all Accounts")
    print("6. Exit")

    while True:

            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    # Create a new account
                    name = input("Enter your name: ")
                    if  name.strip():
                        initial_deposit = float(input("Enter initial deposit: "))
                        bank.create_account(name, initial_deposit)
                    else:
                        raise ValueError("Name cannot be empty.")
                elif choice == "2":
                    # View account details
                    account_number = int(input("Enter account number: "))
                    bank.view_account(account_number)
                elif choice == "3":
                    # Deposit money into an account
                    account_number = int(input("Enter account number: "))
                    amount = float(input("Enter deposit amount: "))
                    bank.deposit(account_number, amount)
                elif choice == "4":
                    # Withdraw money from an account
                    account_number = int(input("Enter account number: "))
                    amount = float(input("Enter withdrawal amount: "))
                    bank.withdraw(account_number, amount)
                elif choice == "5":
                    # view all created accounts
                    bank.view_all_accounts()
                elif choice == "6":
                    # Exit the application
                    print("Thank you for using the banking application.")
                    bank.save_to_file()
                    break
                else:
                    print("Invalid choice. Please try again.")

            except ValueError as ve:
                print(f"Input Error: {ve}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
