import re
import random
import string

def check_password_strength(password: str):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters for a stronger password.")
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$).")

    if len(set(password)) < len(password) * 0.6:
        feedback.append("Avoid repeating the same characters.")
    else:
        score += 1

    if score >= 7:
        strength = "VERY STRONG"
    elif score >= 5:
        strength = "STRONG"
    elif score >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return score, strength, feedback

def generate_strong_password(length: int = 14) -> str:
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# User Input - Password enter panna kekum
password = input("Enter your password: ")

score, strength, feedback = check_password_strength(password)

print(f"\nScore: {score}/7")
print(f"Strength: {strength}")

if feedback:
    print("\nSuggestions to improve:")
    for item in feedback:
        print(f" - {item}")

if score < 5:
    print(f"\nSuggested strong password: {generate_strong_password()}")
