# Password Strength Analyzer - By Pooja Sri Harini
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Password 12+ characters iruntha innum strong ah irukkum")
    else:
        feedback.append("Password romba short! Minimum 8 characters venum")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Oru Capital Letter (A-Z) add pannu")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Oru Small Letter (a-z) add pannu")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Oru Number (0-9) add pannu")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Oru Special Character (!@#$) add pannu")

    if len(set(password)) < len(password) * 0.6:
        feedback.append("Same letters niraya repeat aaguthu")
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

    return strength, score, feedback

def suggest_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(14))

print("=== PASSWORD STRENGTH ANALYZER ===")
pwd = input("Un password ah type pannu: ")
strength, score, feedback = check_password_strength(pwd)
print(f"\nScore: {score}/8")
print(f"Strength: {strength}")
if feedback:
    print("\nImprove panna:")
    for f in feedback:
        print(f"- {f}")
if score < 5:
    print(f"\nSuggest panna strong password: {suggest_strong_password()}")
