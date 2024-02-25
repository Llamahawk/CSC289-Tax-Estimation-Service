import pytest
from taxFunctions import TaxCalculator


# Test state_income_tax with floating-point income
def test_state_income_tax_with_float_income():
    TaxCalculator.annual_income = 60000.75
    assert TaxCalculator.state_income_tax() == 2850.035625


# Test federal_tax_rate_single with floating-point income
def test_federal_tax_rate_single_with_float_income():
    TaxCalculator.annual_income = 60000.75
    assert TaxCalculator.federal_tax_rate_single() == 8507.665


# Test federal_tax_rate_married_joint with floating-point income
def test_federal_tax_rate_married_joint_with_float_income():
    TaxCalculator.annual_income = 60000.75
    assert TaxCalculator.federal_tax_rate_married_joint() == 6760.09


# Test federal_tax_rate_married_separate with floating-point income
def test_federal_tax_rate_married_separate_with_float_income():
    TaxCalculator.annual_income = 60000.75
    assert TaxCalculator.federal_tax_rate_married_separate() == 8507.665


# Test federal_tax_rate_head with floating-point income
def test_federal_tax_rate_head_with_float_income():
    TaxCalculator.annual_income = 60000.75
    assert TaxCalculator.federal_tax_rate_head() == 6930.165


if __name__ == "__main__":
    pytest.main()
