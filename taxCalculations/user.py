from filingStatus import FilingStatus


class User:
    def __init__(self, first_name, last_name, email_address, password, filing_status, income):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password
        self.filing_status = FilingStatus(filing_status)
        self.income = income

    # Add any other methods or properties as needed
