import unittest

from calculator_project.calculator_app.models.filing_status import FilingStatus
from calculator_project.calculator_app.models.user import User
from calculator_project.calculator_app.services.tax_calculator import calculate_taxes
from calculator_project.calculator_app.services.tax_calculator import validate_filing_status
from calculator_project.calculator_app.services.tax_calculator import validate_numeric_input


class TestTaxCalculator(unittest.TestCase):

    def test_validate_numeric_input_valid(self):
        value = "50000"
        result = validate_numeric_input(value)
        self.assertEqual(result, 50000.0)

    def test_validate_numeric_input_invalid(self):
        value = "invalid_value"
        with self.assertRaises(ValueError):
            validate_numeric_input(value)

    def test_validate_filing_status_valid(self):
        result = validate_filing_status(2)
        self.assertEqual(result, FilingStatus.MFJ)

    def test_validate_filing_status_invalid(self):
        value = "invalid_value"
        with self.assertRaises(ValueError):
            validate_filing_status(value)

    def test_valid_user_creation(self):
        first_name = "John"
        last_name = "Doe"
        email_address = "john.doe@example.com"
        entered_password = "Pa$$w0rd"

        user = User(first_name, last_name, email_address, entered_password)

        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.email_address, email_address)
        self.assertTrue(user.validate_hashed_password(entered_password))

    def test_invalid_email_address(self):
        first_name = "John"
        last_name = "Doe"
        invalid_email_address = "invalid_email"

        with self.assertRaises(ValueError):
            User(first_name, last_name, invalid_email_address, "secure_password")

    def test_invalid_password_length(self):
        first_name = "John"
        last_name = "Doe"
        email_address = "john.doe@example.com"
        invalid_password = "short"

        with self.assertRaises(ValueError):
            User(first_name, last_name, email_address, invalid_password)

    def test_zero_taxes_single(self):
        filing_status = 1
        income = 10000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 0)
        self.assertEqual(total_tax, 0)

    def test_zero_state_single(self):
        filing_status = 1
        income = 15000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 115)
        self.assertEqual(total_tax, 115)

    def test_not_zero_single(self):
        filing_status = 1
        income = 27000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 19)
        self.assertEqual(fed_tax, 1358)
        self.assertEqual(total_tax, 1377)

    def test_zero_taxes_MFS(self):
        filing_status = 3
        income = 10000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 0)
        self.assertEqual(total_tax, 0)

    def test_zero_state_MFS(self):
        filing_status = 3
        income = 15000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 115)
        self.assertEqual(total_tax, 115)

    def test_not_zero_MFS(self):
        filing_status = 3
        income = 27000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 19)
        self.assertEqual(fed_tax, 1358)
        self.assertEqual(total_tax, 1377)

    def test_zero_taxes_MFJ(self):
        filing_status = 2
        income = 25000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 0)
        self.assertEqual(total_tax, 0)

    def test_zero_state_MFJ(self):
        filing_status = 2
        income = 30000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 230)
        self.assertEqual(total_tax, 230)

    def test_not_zero_taxes_MFJ(self):
        filing_status = 2
        income = 54000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 38)
        self.assertEqual(fed_tax, 2716)
        self.assertEqual(total_tax, 2754)


    def test_zero_taxes_QW(self):
        filing_status = 5
        income = 25000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 0)
        self.assertEqual(total_tax, 0)

    def test_zero_state_QW(self):
        filing_status = 5
        income = 30000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 230)
        self.assertEqual(total_tax, 230)

    def test_not_zero_taxes_QW(self):
        filing_status = 5
        income = 54000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 38)
        self.assertEqual(fed_tax, 2716)
        self.assertEqual(total_tax, 2754)


    def test_zero_taxes_HH(self):
        filing_status = 4
        income = 20000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 0)
        self.assertEqual(total_tax, 0)

    def test_zero_state_HH(self):
        filing_status = 4
        income = 30000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 0)
        self.assertEqual(fed_tax, 420)
        self.assertEqual(total_tax, 420)

    def test_not_zero_taxes_HH(self):
        filing_status = 4
        income = 40000

        state_tax, fed_tax, total_tax = calculate_taxes(income, filing_status)

        self.assertEqual(state_tax, 4)
        self.assertEqual(fed_tax, 1990)
        self.assertEqual(total_tax, 1994)



if __name__ == '__main__':
    unittest.main()
