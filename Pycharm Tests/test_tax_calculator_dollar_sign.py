import pytest
from taxFunctions import TaxCalculator


# Test state_income_tax with income containing dollar signs
def test_state_income_tax_with_dollar_signs():
    TaxCalculator.annual_income = "$50000"
    assert TaxCalculator.state_income_tax() == 2375.0


# Test federal_tax_rate_single with income containing dollar signs
def test_federal_tax_rate_single_with_dollar_signs():
    TaxCalculator.annual_income = "$60000"
    assert TaxCalculator.federal_tax_rate_single() == 8507.5


# Test federal_tax_rate_married_joint with income containing dollar signs
def test_federal_tax_rate_married_joint_with_dollar_signs():
    TaxCalculator.annual_income = "$90000"
    assert TaxCalculator.federal_tax_rate_married_joint() == 10415.0


# Test federal_tax_rate_married_separate with income containing dollar signs
def test_federal_tax_rate_married_separate_with_dollar_signs():
    TaxCalculator.annual_income = "$40000"
    assert TaxCalculator.federal_tax_rate_married_separate() == 4580.0


# Test federal_tax_rate_head with income containing dollar signs
def test_federal_tax_rate_head_with_dollar_signs():
    TaxCalculator.annual_income = "$70000"
    assert TaxCalculator.federal_tax_rate_head() == 9130.0


if __name__ == "__main__":
    pytest.main()
