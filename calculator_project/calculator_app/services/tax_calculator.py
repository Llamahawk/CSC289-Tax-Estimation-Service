from calculator_app.models.filing_status import FilingStatus


def validate_numeric_input(value):
    try:
        numeric_value = float(value)
        if numeric_value < 0:
            raise ValueError("Income must be a non-negative value")

        return numeric_value
    except ValueError:
        raise ValueError('Invalid numeric value')


def validate_filing_status(value):
    try:
        return FilingStatus(int(value))
    except ValueError:
        raise ValueError('Invalid filing status')


def calculate_taxes(income, filing_status):

    # Validate income
    income = validate_numeric_input(income)

    # Validate filing status
    filing_status = validate_filing_status(filing_status)

    def calculate_state_income_tax():
        rate = 0.0475
        return round(income * rate, 2)

    def calculate_federal_income_tax():
        return round(
            federal_tax_rate_single() if filing_status == FilingStatus.SINGLE
            else federal_tax_rate_head() if filing_status == FilingStatus.HH
            else federal_tax_rate_married_separate() if filing_status == FilingStatus.MFS
            else federal_tax_rate_married_joint_or_qw(), 2
        )

    # calculates federal income tax for single filing status
    def federal_tax_rate_single():
        return (
            # Bracket 1
            income * 0.10 if income <= 11000
            # Bracket 2
            else (income - 11000) * 0.12 + 1100 if 11001 <= income <= 44725
            # Bracket 3
            else (income - 44725) * 0.22 + 5147 if 44726 <= income <= 95375
            # Bracket 4
            else (income - 95375) * 0.24 + 16290 if 95376 <= income <= 182100
            # Bracket 5
            else (income - 182100) * 0.32 + 37104 if 182101 <= income <= 231250
            # Bracket 6
            else (income - 231250) * 0.35 + 52832 if 231251 <= income <= 578125
            # Bracket 7
            else (income - 578125) * 0.37 + 174238.25
        )

    # calculates federal income tax for head of household filing status
    def federal_tax_rate_head():
        return (
            # Bracket 1
            income * 0.10 if income <= 15700
            # Bracket 2
            else (income - 15700) * 0.12 + 1570 if 15701 <= income <= 59850
            # Bracket 3
            else (income - 59850) * 0.22 + 6868 if 59851 <= income <= 95350
            # Bracket 4
            else (income - 95350) * 0.24 + 14678 if 95351 <= income <= 182100
            # Bracket 5
            else (income - 182100) * 0.32 + 35498 if 182101 <= income <= 231250
            # Bracket 6
            else (income - 231250) * 0.35 + 51226 if 231251 <= income <= 578100
            # Bracket 7
            else (income - 578100) * 0.37 + 172621.50
        )

    # calculates federal income tax for married filing separately
    def federal_tax_rate_married_separate():
        return (
            # Bracket 1
            income * 0.10 if income <= 11000
            # Bracket 2
            else (income - 11000) * 0.12 + 1100 if 11001 <= income <= 44725
            # Bracket 3
            else (income - 44725) * 0.22 + 5147 if 44726 <= income <= 95375
            # Bracket 4
            else (income - 95375) * 0.24 + 16290 if 95376 <= income <= 182100
            # Bracket 5
            else (income - 182100) * 0.32 + 37104 if 182101 <= income <= 231250
            # Bracket 6
            else (income - 231250) * 0.35 + 52832 if 231251 <= income <= 346875
            # Bracket 7
            else (income - 346875) * 0.37 + 93300
        )

    # calculates federal income tax for married filing jointly or qualified widow(er)
    def federal_tax_rate_married_joint_or_qw():
        return (
            # Bracket 1
            income * 0.10 if income <= 22000
            # Bracket 2
            else (income - 22000) * 0.12 + 2200 if 22001 <= income <= 89450
            # Bracket 3
            else (income - 89450) * 0.22 + 10294 if 89451 <= income <= 190750
            # Bracket 4
            else (income - 190750) * 0.24 + 32596.50 if 190751 <= income <= 364200
            # Bracket 5
            else (income - 364200) * 0.32 + 74224.50 if 364201 <= income <= 462500
            # Bracket 6
            else (income - 462500) * 0.35 + 105680.50 if 462501 <= income <= 693750
            # Bracket 7
            else (income - 693750) * 0.37 + 186618
        )

    state_tax = calculate_state_income_tax()
    federal_tax = calculate_federal_income_tax()
    total_tax = round(state_tax + federal_tax, 2)

    return state_tax, federal_tax, total_tax
