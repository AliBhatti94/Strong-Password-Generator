import random
import string

def generate_strong_password(length=12):
    if length < 8:  # You can set your own minimum length
        raise ValueError("Password length should be at least 8 characters.")
    
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password has at least one of each character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password length with random choices from all character sets
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to avoid any predictable sequences
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    password_length = 12  # You can change the length here
    strong_password = generate_strong_password(password_length)
    print(f"Generated strong password: {strong_password}")
