from taxCalculator import TaxCalculator, FilingStatus

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
        print("\nFor filing status:\nsingle = 1\nmarried jointly = 2\nmarried separately = 3\nhead of household = 4\nqualifying widow(er) = 5")
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

# Validate and collect income
income = validate_numeric_input('Enter your net annual income: ')

# Validate and collect filing status
filing_status = validate_filing_status()

# Create an instance of TaxCalculator
tax_calculator = TaxCalculator(income, FilingStatus(filing_status))

# Calculate federal and state tax
FedTax = tax_calculator.calculate_federal_tax()
StateTax = tax_calculator.calculate_state_tax()

# Sum of federal and state tax
tax = StateTax + FedTax

# Print results
print("")
print(f"State tax liability: ${StateTax:.2f}")
print("---------------------------")
print(f"Federal tax liability: ${FedTax:.2f}")
print("---------------------------")
print(f"Total tax liability: ${tax:.2f}")
print("")
