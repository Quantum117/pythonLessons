class InvestApp:
    @staticmethod
    def invest(amount, rate, years):
        """
        Calculate and display the investment growth over time.

        Parameters:
        amount (float): The initial principal amount.
        rate (float): The annual rate of return (as a decimal).
        years (int): The number of years to calculate.
        """
        for year in range(1, years + 1):
            amount += amount * rate  # Increase the amount by the rate
            print(f"year {year}: ${amount:.2f}")


# Prompt the user for input
try:
    principal = float(input("Enter the initial amount: "))
    annual_rate = float(input("Enter the annual rate of return (as a decimal, e.g., 0.05 for 5%): "))
    num_years = int(input("Enter the number of years: "))

    print("\nInvestment growth:")
    # Call the static method using the class name
    InvestApp.invest(principal, annual_rate, num_years)
except ValueError:
    print("Invalid input. Please enter numeric values for amount, rate, and years.")
