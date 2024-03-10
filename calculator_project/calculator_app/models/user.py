import re
import bcrypt
import base64


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


class User:

    def __init__(self, first_name, last_name, email_address, password):
        self.first_name = validate_string_input(first_name, "First name")
        self.last_name = validate_string_input(last_name, "Last name")
        self.email_address = validate_email_address(email_address)
        self.hashed_password = self._hash_password(validate_password(password))

    @staticmethod
    def _hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return base64.b64encode(hashed_password).decode('utf-8')

    def validate_hashed_password(self, entered_password):
        entered_password_bytes = entered_password.encode('utf-8')
        hashed_password_bytes = base64.b64decode(self.hashed_password.encode('utf-8'))

        if bcrypt.checkpw(entered_password_bytes, hashed_password_bytes):
            return "Valid"
        else:
            return "Invalid"