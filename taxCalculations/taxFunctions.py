# Group 12
# Feb 1st, 2024
# CSC.289.0001
# Functions to be used for tax estimation service

# function for login verification. (this part has not been completed so for now
# it will always return true
def login():
    return True


# function for creating account. feature will be implemented later so for now
# function will remain empty
def create_account():
    pass


# function collects annual income of user
def collect_income():
    annual_income = float(input("Please enter your annual income: "))
    return annual_income


def state_income_tax(annual_income):
    income_tax = annual_income * 0.0475
    return income_tax


# calculates federal income tax for single filing status
def federal_tax_rate_single(annual_income):
    income_tax = 0
    # Bracket 1
    if annual_income <= 11000:
        income_tax = annual_income * 0.10
    # Bracket 2
    elif 11001 <= annual_income <= 44725:
        income_tax = (annual_income - 11000) * 0.12 + 1100
    # Bracket 3
    elif 44726 <= annual_income <= 95375:
        income_tax = (annual_income - 44725) * 0.22 + 5147
    # Bracket 4
    elif 95376 <= annual_income <= 182100:
        income_tax = (annual_income - 95375) * 0.24 + 16290
    # Bracket 5
    elif 182101 <= annual_income <= 231250:
        income_tax = (annual_income - 182100) * 0.32 + 37104
    # Bracket 6
    elif 231251 <= annual_income <= 578125:
        income_tax = (annual_income - 231250) * 0.35 + 52832
    # Bracket 7
    elif 578126 <= annual_income:
        income_tax = (annual_income - 578125) * 0.37 + 174238.25

    return income_tax


# calculates federal income tax for married filing jointly
def federal_tax_rate_married_joint(annual_income):
    income_tax = 0
    # Bracket 1
    if annual_income <= 22000:
        income_tax = annual_income * 0.10
    # Bracket 2
    elif 22001 <= annual_income <= 89450:
        income_tax = (annual_income - 22000) * 0.12 + 2200
    # Bracket 3
    elif 89451 <= annual_income <= 190750:
        income_tax = (annual_income - 89450) * 0.22 + 10294
    # Bracket 4
    elif 190751 <= annual_income <= 364200:
        income_tax = (annual_income - 190750) * 0.24 + 32596.50
    # Bracket 5
    elif 364201 <= annual_income <= 462500:
        income_tax = (annual_income - 364200) * 0.32 + 74224.50
    # Bracket 6
    elif 462501 <= annual_income <= 693750:
        income_tax = (annual_income - 462500) * 0.35 + 105680.50
    # Bracket 7
    elif 693751 <= annual_income:
        income_tax = (annual_income - 578125) * 0.37 + 186618

    return income_tax


# calculates federal income tax for married filing separately
def federal_tax_rate_married_separate(annual_income):
    income_tax = 0
    # Bracket 1
    if annual_income <= 11000:
        income_tax = annual_income * 0.10
    # Bracket 2
    elif 11001 <= annual_income <= 44725:
        income_tax = (annual_income - 11000) * 0.12 + 1100
    # Bracket 3
    elif 44726 <= annual_income <= 95375:
        income_tax = (annual_income - 44725) * 0.22 + 5147
    # Bracket 4
    elif 95376 <= annual_income <= 182100:
        income_tax = (annual_income - 95375) * 0.24 + 16290
    # Bracket 5
    elif 182101 <= annual_income <= 231250:
        income_tax = (annual_income - 182100) * 0.32 + 37104
    # Bracket 6
    elif 231251 <= annual_income <= 346875:
        income_tax = (annual_income - 231250) * 0.35 + 52832
    # Bracket 7
    elif 346876 <= annual_income:
        income_tax = (annual_income - 346875) * 0.37 + 93300

    return income_tax


# calculates federal income tax for head of household filing status
def federal_tax_rate_head(annual_income):
    pass
