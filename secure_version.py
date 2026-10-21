
"""
CodSoft Task 3: Secure Code Assessment
File: secure_version.py

A safer educational implementation of a profile validator.
Uses fictional, local input only.
"""

import re


MAX_NAME_LENGTH = 80
MAX_EMAIL_LENGTH = 254
MIN_AGE = 1
MAX_AGE = 120

# A simple format check for this learning project.
# Real applications should use a well-tested email validation
# strategy and verify addresses when necessary.
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class ValidationError(ValueError):
    """Raised when profile input does not meet validation rules."""


def validate_name(name):
    """Validate the profile name."""
    if not isinstance(name, str):
        raise ValidationError("Name must be text.")

    name = name.strip()

    if not name:
        raise ValidationError("Name cannot be empty.")

    if len(name) > MAX_NAME_LENGTH:
        raise ValidationError(
            f"Name must be {MAX_NAME_LENGTH} characters or fewer."
        )

    if any(ord(character) < 32 for character in name):
        raise ValidationError("Name contains unsupported control characters.")

    return name


def validate_email(email):
    """Perform a basic email format and length check."""
    if not isinstance(email, str):
        raise ValidationError("Email must be text.")

    email = email.strip()

    if not email or len(email) > MAX_EMAIL_LENGTH:
        raise ValidationError("Email is empty or too long.")

    if not EMAIL_PATTERN.fullmatch(email):
        raise ValidationError("Enter a valid email format.")

    return email


def validate_age(age):
    """Validate age as an integer within the permitted range."""
    if isinstance(age, bool):
        raise ValidationError("Age must be a whole number.")

    try:
        # Reject fractional and other non-integer input.
        age_value = int(age)
    except (ValueError, TypeError, OverflowError):
        raise ValidationError("Age must be a whole number.") from None

    if isinstance(age, float) and not age.is_integer():
        raise ValidationError("Age must be a whole number.")

    if isinstance(age, str) and not re.fullmatch(r"\d+", age.strip()):
        raise ValidationError("Age must be a whole number.")

    if not MIN_AGE <= age_value <= MAX_AGE:
        raise ValidationError(
            f"Age must be between {MIN_AGE} and {MAX_AGE}."
        )

    return age_value


def create_profile(name, email, age):
    """Validate all fields before returning a profile."""
    return {
        "name": validate_name(name),
        "email": validate_email(email),
        "age": validate_age(age),
    }


def main():
    print("=== Secure Profile Validator ===")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")

    try:
        profile = create_profile(name, email, age)
    except ValidationError as error:
        # Expected validation errors are safe to explain to the user.
        print(f"Input error: {error}")
        return
    except Exception:
        # Avoid showing unexpected internal exception details.
        print("An unexpected error occurred. Please try again.")
        return

    print("\nProfile validated successfully.")
    # Print fields separately instead of displaying an arbitrary object.
    print(f"Name: {profile['name']}")
    print(f"Email: {profile['email']}")
    print(f"Age: {profile['age']}")


if __name__ == "__main__":
    main()
