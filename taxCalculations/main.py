from taxCalculator import TaxCalculator
from filingStatus import FilingStatus
from user import User


# Function to validate numeric input
def validate_numeric_input(prompt):
    validated = False
    while not validated:
        value = input(prompt)
        try:
            value = float(value)
            validated = True
        except ValueError:
            print('Invalid numeric value')
    return value


# Function to validate filing status input
def validate_filing_status():
    validated = False
    while not validated:
        print(
            "\nFor filing status:\nsingle = 1\nmarried jointly = 2\nmarried separately = 3\nhead of household = 4\nqualifying widow(er) = 5")
        filing_status = input("\nPlease enter your filing status: ")
        try:
            filing_status = int(filing_status)
            if 0 < filing_status < 6:
                validated = True
            else:
                print("Please enter 1, 2, 3, 4, or 5 to declare filing status")
        except ValueError:
            print("Please enter 1, 2, 3, 4, or 5 to declare filing status")
    return filing_status


# Function to create a User instance
def create_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email_address = input("Enter your email address: ")
    password = input("Enter your password: ")
    filing_status = validate_filing_status()  # Assuming validate_filing_status is still available
    income = validate_numeric_input('Enter your net annual income: ')

    return User(first_name, last_name, email_address, password, filing_status, income)


# Example usage:
# create user with user prompts
user = create_user()

# Create an instance of TaxCalculator
tax_calculator = TaxCalculator(user.income, FilingStatus(user.filing_status))

# Calculate tax liability
state_tax = tax_calculator.calculate_state_tax()
fed_tax = tax_calculator.calculate_federal_tax()
total_tax = state_tax + fed_tax

# Print results
print("")
print(f"State tax liability: ${state_tax:.2f}")
print("---------------------------")
print(f"Federal tax liability: ${fed_tax:.2f}")
print("---------------------------")
print(f"Total tax liability: ${total_tax:.2f}")
print("")
