import pytest

from calculator_project.calculator_app.services.tax_calculator import calculate_taxes


# Tax calculation with income containing comma raises exception
def test_calculate_taxes_with_comma_raises_exception():
    with pytest.raises(ValueError):
        calculate_taxes("50,000", 1)


# Tax calculation with income containing dollar sign raises exception
def test_calculate_taxes_with_dollar_sign_raises_exception():
    with pytest.raises(ValueError):
        calculate_taxes("$50000", 1)


# Tax calculation with negative income raises exception
def test_federal_tax_rate_single_with_negative_income():
    with pytest.raises(ValueError):
        calculate_taxes(-50000, 1)


# Test calculate_taxes with floating-point income when Single
def test_calculate_taxes_with_float_income_and_single():
    assert calculate_taxes(60000.75, 1) == (2850.04, 8507.67, 11357.71)


# Test calculate_taxes with floating-point income when Married Filing Jointly
def test_calculate_taxes_with_float_income_and_MFJ():
    assert calculate_taxes(60000.75, 2) == (2850.04, 6760.09, 9610.13)


# Test calculate_taxes with floating-point income when Married Filing Separately
def test_calculate_taxes_with_float_income_and_MFS():
    assert calculate_taxes(60000.75, 3) == (2850.04, 8507.67, 11357.71)


# Test calculate_taxes with floating-point income when Head of Household
def test_calculate_taxes_with_float_income_and_HH():
    assert calculate_taxes(60000.75, 4) == (2850.04, 6901.16, 9751.2)


# Test calculate_taxes with floating-point income when Qualifying Widow(er)
def test_calculate_taxes_with_float_income_and_QW():
    assert calculate_taxes(60000.75, 5) == (2850.04, 6760.09, 9610.13)


if __name__ == "__main__":
    pytest.main()
