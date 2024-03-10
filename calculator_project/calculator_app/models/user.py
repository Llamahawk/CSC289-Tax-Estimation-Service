import re
import bcrypt


def validate_string_input(value, field_name):
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field_name} must be a non-empty string.")
    return value


def validate_email_address(email_address):
    if not email_address:
        raise ValueError("Email address must be a non-empty string.")
    # Basic email format validation using regex
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
        raise ValueError("Invalid email address format")
    return email_address


def validate_password(password):
    # Password length requirement
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

    # Complexity requirements
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        raise ValueError("Password must contain at least one special character")
    return password


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(validate_password(password).encode('utf-8'), salt)
    return hashed_password


class User:

    def __init__(self, first_name, last_name, email_address, password):
        self.first_name = validate_string_input(first_name, "First name")
        self.last_name = validate_string_input(last_name, "Last name")
        self.email_address = validate_email_address(email_address)
        self.hashed_password = hash_password(password)

    def validate_hashed_password(self, entered_password):
        return bcrypt.checkpw(entered_password.encode('utf-8'), self.hashed_password)
