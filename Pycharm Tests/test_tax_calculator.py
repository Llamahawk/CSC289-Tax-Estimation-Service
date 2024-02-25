import pytest
from taxFunctions import TaxCalculator


def test_initialization():
    # Test object initialization
    tax_calculator = TaxCalculator()
    assert isinstance(tax_calculator, TaxCalculator)


def test_state_income_tax():
    # Test state income tax calculation
    TaxCalculator.annual_income = 50000
    assert TaxCalculator.state_income_tax() == 2375.0


def test_federal_tax_rate_single():
    # Test federal tax rate calculation for single filing status
    TaxCalculator.annual_income = 60000
    assert TaxCalculator.federal_tax_rate_single() == 8507.5


def test_federal_tax_rate_married_joint():
    # Test federal tax rate calculation for married filing jointly
    TaxCalculator.annual_income = 90000
    assert TaxCalculator.federal_tax_rate_married_joint() == 10415.0


def test_federal_tax_rate_married_separate():
    # Test federal tax rate calculation for married filing separately
    TaxCalculator.annual_income = 40000
    assert TaxCalculator.federal_tax_rate_married_separate() == 4580.0


def test_federal_tax_rate_head():
    # Test federal tax rate calculation for head of household filing status
    TaxCalculator.annual_income = 70000
    assert TaxCalculator.federal_tax_rate_head() == 9130.0


if __name__ == "__main__":
    pytest.main()
