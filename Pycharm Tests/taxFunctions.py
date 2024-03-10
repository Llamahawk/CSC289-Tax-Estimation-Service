class TaxCalculator:
    # Class variable for income
    annual_income = 0

    # function for login verification. (this part has not been completed so for now
    # it will always return true
    @staticmethod
    def login():
        return True

    # function for creating account. feature will be implemented later so for now
    # function will remain empty
    @staticmethod
    def create_account():
        pass

    # function collects annual income of user
    @classmethod
    def collect_income(cls):
        cls.annual_income = float(input("Please enter your annual income: "))

    @staticmethod
    def state_income_tax():
        income_tax = TaxCalculator.annual_income * 0.0475
        return income_tax

    # calculates federal income tax for single filing status
    @staticmethod
    def federal_tax_rate_single():
        income_tax = 0
        annual_income = TaxCalculator.annual_income
        if annual_income <= 11000:
            income_tax = annual_income * 0.10
        elif 11001 <= annual_income <= 44725:
            income_tax = (annual_income - 11000) * 0.12 + 1100
        elif 44726 <= annual_income <= 95375:
            income_tax = (annual_income - 44725) * 0.22 + 5147
        elif 95376 <= annual_income <= 182100:
            income_tax = (annual_income - 95375) * 0.24 + 16290
        elif 182101 <= annual_income <= 231250:
            income_tax = (annual_income - 182100) * 0.32 + 37104
        elif 231251 <= annual_income <= 578125:
            income_tax = (annual_income - 231250) * 0.35 + 52832
        elif 578126 <= annual_income:
            income_tax = (annual_income - 578125) * 0.37 + 174238.25
        return income_tax

    # calculates federal income tax for married filing jointly
    @staticmethod
    def federal_tax_rate_married_joint():
        income_tax = 0
        annual_income = TaxCalculator.annual_income
        if annual_income <= 22000:
            income_tax = annual_income * 0.10
        elif 22001 <= annual_income <= 89450:
            income_tax = (annual_income - 22000) * 0.12 + 2200
        elif 89451 <= annual_income <= 190750:
            income_tax = (annual_income - 89450) * 0.22 + 10294
        elif 190751 <= annual_income <= 364200:
            income_tax = (annual_income - 190750) * 0.24 + 32596.50
        elif 364201 <= annual_income <= 462500:
            income_tax = (annual_income - 364200) * 0.32 + 74224.50
        elif 462501 <= annual_income <= 693750:
            income_tax = (annual_income - 462500) * 0.35 + 105680.50
        elif 693751 <= annual_income:
            income_tax = (annual_income - 578125) * 0.37 + 186618
        return income_tax

    # calculates federal income tax for married filing separately
    @staticmethod
    def federal_tax_rate_married_separate():
        income_tax = 0
        annual_income = TaxCalculator.annual_income
        if annual_income <= 11000:
            income_tax = annual_income * 0.10
        elif 11001 <= annual_income <= 44725:
            income_tax = (annual_income - 11000) * 0.12 + 1100
        elif 44726 <= annual_income <= 95375:
            income_tax = (annual_income - 44725) * 0.22 + 5147
        elif 95376 <= annual_income <= 182100:
            income_tax = (annual_income - 95375) * 0.24 + 16290
        elif 182101 <= annual_income <= 231250:
            income_tax = (annual_income - 182100) * 0.32 + 37104
        elif 231251 <= annual_income <= 346875:
            income_tax = (annual_income - 231250) * 0.35 + 52832
        elif 346876 <= annual_income:
            income_tax = (annual_income - 346875) * 0.37 + 93300
        return income_tax

    # calculates federal income tax for head of household filing status
    @staticmethod
    def federal_tax_rate_head():
        income_tax = 0
        annual_income = TaxCalculator.annual_income
        if annual_income <= 15700:
            income_tax = annual_income * 0.10
        elif 15701 <= annual_income <= 59850:
            income_tax = (annual_income - 15700) * 0.12 + 1570
        elif 59851 <= annual_income <= 148850:
            income_tax = (annual_income - 59850) * 0.22 + 6897
        elif 148851 <= annual_income <= 226850:
            income_tax = (annual_income - 148850) * 0.24 + 27540
        elif 226851 <= annual_income <= 405100:
            income_tax = (annual_income - 226850) * 0.32 + 49844
        elif 405101 <= annual_income <= 432200:
            income_tax = (annual_income - 405100) * 0.35 + 117868
        elif 432201 <= annual_income:
            income_tax = (annual_income - 432200) * 0.37 + 126957
        return income_tax


# Test the class
if __name__ == "__main__":
    TaxCalculator.collect_income()
    print("Annual Income:", TaxCalculator.annual_income)
    print("State Income Tax:", TaxCalculator.state_income_tax())
    print("Federal Tax Rate (Single):", TaxCalculator.federal_tax_rate_single())
    print("Federal Tax Rate (Married, Joint):", TaxCalculator.federal_tax_rate_married_joint())
    print("Federal Tax Rate (Married, Separate):", TaxCalculator.federal_tax_rate_married_separate())
    print("Federal Tax Rate (Head of Household):", TaxCalculator.federal_tax_rate_head())
