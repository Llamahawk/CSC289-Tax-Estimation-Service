from enum import Enum


class FilingStatus(Enum):
    SINGLE = 1
    MFJ = 2  # Married Filing Jointly
    MFS = 3  # Married Filing Separately
    HH = 4  # Head of Household
    QW = 5  # Qualifying Widow(er)
