import re

def evaluate_password(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Use at least one special character.")

    # Result
    if score == 5:
        status = "Strong 💪"
    elif score >= 3:
        status = "Moderate ⚠️"
    else:
        status = "Weak ❌"

    return status, suggestions


def main():
    print("🔐 Password Strength Checker\n")
    while True:
        password = input("Enter a password to check (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Goodbye! 👋")
            break

        status, tips = evaluate_password(password)
        print(f"\n✅ Password Status: {status}")

        if tips:
            print("📌 Suggestions to improve your password:")
            for tip in tips:
                print("  -", tip)

        print("\n" + "-"*40 + "\n")


if __name__ == "__main__":
    main()
    