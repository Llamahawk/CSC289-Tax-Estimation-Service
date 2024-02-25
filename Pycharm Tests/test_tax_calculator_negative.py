import pytest
from taxFunctions import TaxCalculator


# Test federal_tax_rate_single with negative income
def test_federal_tax_rate_single_with_negative_income():
    TaxCalculator.annual_income = -60000
    assert TaxCalculator.federal_tax_rate_single() == 0


# Test federal_tax_rate_married_joint with negative income
def test_federal_tax_rate_married_joint_with_negative_income():
    TaxCalculator.annual_income = -90000
    assert TaxCalculator.federal_tax_rate_married_joint() == 0


# Test federal_tax_rate_married_separate with negative income
def test_federal_tax_rate_married_separate_with_negative_income():
    TaxCalculator.annual_income = -40000
    assert TaxCalculator.federal_tax_rate_married_separate() == 0


# Test federal_tax_rate_head with negative income
def test_federal_tax_rate_head_with_negative_income():
    TaxCalculator.annual_income = -70000
    assert TaxCalculator.federal_tax_rate_head() == 0


# Test state_income_tax with negative income
def test_state_income_tax_with_negative_income():
    TaxCalculator.annual_income = -50000
    assert TaxCalculator.state_income_tax() == 0


if __name__ == "__main__":
    pytest.main()
