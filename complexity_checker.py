import re

def check_password_strength(password):
    # Initialize variables
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None
    
    # Calculate strength
    strength = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])
    
    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")
    
    # Determine strength level
    if strength == 5:
        strength_level = "Very Strong"
    elif strength == 4:
        strength_level = "Strong"
    elif strength == 3:
        strength_level = "Moderate"
    elif strength == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"
    
    return strength_level, feedback

def main():
    password = input("Enter your password: ")
    strength_level, feedback = check_password_strength(password)
    
    print(f"Password Strength: {strength_level}")
    for msg in feedback:
        print(f"- {msg}")

if __name__ == "__main__":
    main()
