# Group 12
# Feb 1st, 2024
# CSC.289.0001

from taxFunctions import *

# Validation loop to avoid ValueError when collecting income
validated = False
while validated == False:
    income = input('Enter your net annual income: ')
    try:
        income = float(income)
        validated = True
    except:
        print('Invalid numeric value')

# Validation loop to avoid ValueError when collecting filing status
validated = False
while validated == False:
    print("\nFor filing status:\nsingle = 1\nmarried jointly = 2\nmarried seperately = 3\nhead of household = 4")
    filing_status = input("\nPlease enter your filing status: ")
    try:
        filing_status = int(filing_status)
        if 0 < filing_status < 5:
            validated = True
        else:
            print("Please enter 1, 2, 3, or 4 to declare filing status")
    except:
        print("Please enter 1, 2, 3, or 4 to declare filing status")

# calls correct federal tax calculator function based on filing status input
if filing_status == 1:
    FedTax = federal_tax_rate_single(income)
elif filing_status == 2:
    FedTax = federal_tax_rate_married_joint(income)
elif filing_status == 3:
    FedTax = federal_tax_rate_married_separate(income)
elif filing_status == 4:
    FedTax = federal_tax_rate_head(income)

# calls state tax function (flat tax so no bracket filter needed)
StateTax = state_income_tax(income)

# sum of federal and state tax
tax = StateTax + FedTax

print("")
print(f"State tax owed: ${StateTax:.2f}")
print("---------------------------")
print(f"Federal tax owed: ${FedTax:.2f}")
print("---------------------------")
print(f"Total tax owed: ${tax:.2f}")
print("")