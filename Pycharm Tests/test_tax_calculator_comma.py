import pytest
from taxFunctions import TaxCalculator


# Test state_income_tax with income containing commas
def test_state_income_tax_with_commas():
    TaxCalculator.annual_income = "50,000"
    assert TaxCalculator.state_income_tax() == 2375.0


# Test federal_tax_rate_single with income containing commas
def test_federal_tax_rate_single_with_commas():
    TaxCalculator.annual_income = "60,000"
    assert TaxCalculator.federal_tax_rate_single() == 8507.5


# Test federal_tax_rate_married_joint with income containing commas
def test_federal_tax_rate_married_joint_with_commas():
    TaxCalculator.annual_income = "90,000"
    assert TaxCalculator.federal_tax_rate_married_joint() == 10415.0


# Test federal_tax_rate_married_separate with income containing commas
def test_federal_tax_rate_married_separate_with_commas():
    TaxCalculator.annual_income = "40,000"
    assert TaxCalculator.federal_tax_rate_married_separate() == 4580.0


# Test federal_tax_rate_head with income containing commas
def test_federal_tax_rate_head_with_commas():
    TaxCalculator.annual_income = "70,000"
    assert TaxCalculator.federal_tax_rate_head() == 9130.0


if __name__ == "__main__":
    pytest.main()
