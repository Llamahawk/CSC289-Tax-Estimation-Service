import pytest
from taxFunctions import TaxCalculator


# Test state_income_tax with string input
def test_state_income_tax_with_string_input():
    TaxCalculator.annual_income = "invalid"
    with pytest.raises(TypeError):
        TaxCalculator.state_income_tax()


# Test federal_tax_rate_single with string input
def test_federal_tax_rate_single_with_string_input():
    TaxCalculator.annual_income = "invalid"
    with pytest.raises(TypeError):
        TaxCalculator.federal_tax_rate_single()


# Test federal_tax_rate_married_joint with string input
def test_federal_tax_rate_married_joint_with_string_input():
    TaxCalculator.annual_income = "invalid"
    with pytest.raises(TypeError):
        TaxCalculator.federal_tax_rate_married_joint()


# Test federal_tax_rate_married_separate with string input
def test_federal_tax_rate_married_separate_with_string_input():
    TaxCalculator.annual_income = "invalid"
    with pytest.raises(TypeError):
        TaxCalculator.federal_tax_rate_married_separate()


# Test federal_tax_rate_head with string input
def test_federal_tax_rate_head_with_string_input():
    TaxCalculator.annual_income = "invalid"
    with pytest.raises(TypeError):
        TaxCalculator.federal_tax_rate_head()


# Test collect_income with string input
def test_collect_income_with_string_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "invalid")
    with pytest.raises(ValueError):
        TaxCalculator.collect_income()


# Test create_account with string input
def test_create_account_with_string_input():
    with pytest.raises(TypeError):
        TaxCalculator.create_account()


# Test login with string input
def test_login_with_string_input():
    with pytest.raises(TypeError):
        TaxCalculator.login()


if __name__ == "__main__":
    pytest.main()
