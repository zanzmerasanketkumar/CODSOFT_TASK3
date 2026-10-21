
"""
CodSoft Task 3: Secure Code Assessment
File: example_vulnerable.py

WARNING:
This is a deliberately insecure educational example.
Do not use this implementation in a real application.
"""


def create_profile(name, email, age):
    """Create a profile using insufficient input validation."""

    # Issue 1: No validation of name or email.
    # Empty strings, unexpected values, or malformed email addresses
    # can be accepted.

    # Issue 2: Age is converted without validating its range.
    # Negative ages and implausibly large ages are accepted.
    age = int(age)

    # Issue 3: Raw user input is placed directly into the output.
    # If another system later renders this data as HTML, it must
    # apply appropriate output encoding for that context.
    profile = {
        "name": name,
        "email": email,
        "age": age,
    }

    return profile


def main():
    print("=== Vulnerable Profile Validator (Educational Only) ===")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    age = input("Enter your age: ")

    try:
        profile = create_profile(name, email, age)
        print("\nProfile created:")
        print(profile)
    except Exception as error:
        # Issue 4: Displays internal exception details directly.
        # This can expose implementation information to users.
        print(f"Internal error: {error}")


if __name__ == "__main__":
    main()
