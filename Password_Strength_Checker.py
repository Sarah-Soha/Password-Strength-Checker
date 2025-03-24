import string


def password_strength_checker(password):
    length = len(password)
    score = 0

    if length >= 8:
        score += 1

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_symbol = True

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    # Strength rating based on score
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"


# Main Program
password = input("Enter a password to check: ")
strength = password_strength_checker(password)
print(f"Password Strength: {strength}")