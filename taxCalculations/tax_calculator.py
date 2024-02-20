from filing_status import FilingStatus


class TaxCalculator:
    def __init__(self, income, filing_status):
        self.income = income
        self.filing_status = filing_status

    def calculate_federal_tax(self):
        if self.filing_status == FilingStatus.SINGLE:
            return self.federal_tax_rate_single()
        elif self.filing_status == FilingStatus.MFJ:
            return self.federal_tax_rate_married_joint_or_qw()
        elif self.filing_status == FilingStatus.MFS:
            return self.federal_tax_rate_married_separate()
        elif self.filing_status == FilingStatus.HH:
            return self.federal_tax_rate_head()
        elif self.filing_status == FilingStatus.QW:
            return self.federal_tax_rate_married_joint_or_qw()

    def calculate_state_tax(self):
        return self.state_income_tax()

    def calculate_total_tax(self):
        return self.calculate_federal_tax() + self.calculate_state_tax()

    def state_income_tax(self):
        return self.income * 0.0475

    # calculates federal income tax for single filing status
    def federal_tax_rate_single(self):
        # Bracket 1
        if self.income <= 11000:
            return self.income * 0.10
        # Bracket 2
        elif 11001 <= self.income <= 44725:
            return (self.income - 11000) * 0.12 + 1100
        # Bracket 3
        elif 44726 <= self.income <= 95375:
            return (self.income - 44725) * 0.22 + 5147
        # Bracket 4
        elif 95376 <= self.income <= 182100:
            return (self.income - 95375) * 0.24 + 16290
        # Bracket 5
        elif 182101 <= self.income <= 231250:
            return (self.income - 182100) * 0.32 + 37104
        # Bracket 6
        elif 231251 <= self.income <= 578125:
            return (self.income - 231250) * 0.35 + 52832
        # Bracket 7
        elif 578126 <= self.income:
            return (self.income - 578125) * 0.37 + 174238.25

    # calculates federal income tax for married filing jointly or qualified widow(er)
    def federal_tax_rate_married_joint_or_qw(self):
        # Bracket 1
        if self.income <= 22000:
            return self.income * 0.10
        # Bracket 2
        elif 22001 <= self.income <= 89450:
            return (self.income - 22000) * 0.12 + 2200
        # Bracket 3
        elif 89451 <= self.income <= 190750:
            return (self.income - 89450) * 0.22 + 10294
        # Bracket 4
        elif 190751 <= self.income <= 364200:
            return (self.income - 190750) * 0.24 + 32596.50
        # Bracket 5
        elif 364201 <= self.income <= 462500:
            return (self.income - 364200) * 0.32 + 74224.50
        # Bracket 6
        elif 462501 <= self.income <= 693750:
            return (self.income - 462500) * 0.35 + 105680.50
        # Bracket 7
        elif 693751 <= self.income:
            return (self.income - 578125) * 0.37 + 186618

    # calculates federal income tax for married filing separately
    def federal_tax_rate_married_separate(self):
        # Bracket 1
        if self.income <= 11000:
            return self.income * 0.10
        # Bracket 2
        elif 11001 <= self.income <= 44725:
            return (self.income - 11000) * 0.12 + 1100
        # Bracket 3
        elif 44726 <= self.income <= 95375:
            return (self.income - 44725) * 0.22 + 5147
        # Bracket 4
        elif 95376 <= self.income <= 182100:
            return (self.income - 95375) * 0.24 + 16290
        # Bracket 5
        elif 182101 <= self.income <= 231250:
            return (self.income - 182100) * 0.32 + 37104
        # Bracket 6
        elif 231251 <= self.income <= 346875:
            return (self.income - 231250) * 0.35 + 52832
        # Bracket 7
        elif 346876 <= self.income:
            return (self.income - 346875) * 0.37 + 93300

    # calculates federal income tax for head of household filing status
    def federal_tax_rate_head(self):
        # Bracket 1
        if self.income <= 15700:
            return self.income * 0.10
        # Bracket 2
        elif 15701 <= self.income <= 59850:
            return (self.income - 15700) * 0.12 + 1570
        # Bracket 3
        elif 59851 <= self.income <= 95350:
            return (self.income - 59850) * 0.22 + 6868
        # Bracket 4
        elif 95351 <= self.income <= 182100:
            return (self.income - 95350) * 0.24 + 14678
        # Bracket 5
        elif 182101 <= self.income <= 231250:
            return (self.income - 182100) * 0.32 + 35498
        # Bracket 6
        elif 231251 <= self.income <= 578100:
            return (self.income - 231250) * 0.35 + 51226
        # Bracket 7
        elif 578101 <= self.income:
            return (self.income - 346875) * 0.37 + 172621.50


def login():
    return True


def create_account():
    pass


def collect_income():
    annual_income = float(input("Please enter your annual income: "))
    return annual_income
