from filing_status import FilingStatus


class User:
    def __init__(self, first_name, last_name, email_address, password, filing_status, income):
        self.first_name = self.validate_string_input(first_name, "First name")
        self.last_name = self.validate_string_input(last_name, "Last name")
        self.email_address = self.validate_email(email_address)
        self.password = self.validate_string_input(password, "Password")
        self.filing_status = self.validate_filing_status(filing_status)
        self.income = self.validate_numeric_input(income, "Income")

    def validate_string_input(self, value, field_name):
        if not isinstance(value, str) or not value:
            raise ValueError(f"{field_name} must be a non-empty string.")
        return value

    def validate_email(self, email):
        # Add email validation logic here
        # You might want to use a regular expression or a library for this
        if not isinstance(email, str) or not email:
            raise ValueError("Email must be a non-empty string.")
        # Add more email validation logic if needed
        return email

    def validate_filing_status(self, status):
        if not (0 < status < 6):
            raise ValueError("Invalid filing status.")
        return status

    def validate_numeric_input(self, value, field_name):
        try:
            return float(value)
        except (ValueError, TypeError):
            raise ValueError(f"{field_name} must be a valid numeric value.")
