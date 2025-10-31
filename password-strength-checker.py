# password-strength-checker.py
import re

def check_strength(pwd):
    score = 0
    if len(pwd) >= 8: score += 1
    if re.search(r"[A-Z]", pwd): score += 1
    if re.search(r"[a-z]", pwd): score += 1
    if re.search(r"\d", pwd): score += 1
    if re.search(r"[@$!%*?&]", pwd): score += 1
    return ["Weak", "Moderate", "Strong"][min(score//2, 2)]

if __name__ == "__main__":
    p = input("Enter password: ")
    print("Strength:", check_strength(p))
