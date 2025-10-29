import random
import string

def generate_password(length=12):
    # Characters to choose from
    letters = string.ascii_letters   # a-z, A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # special characters like !, @, #
    
    # Combine all characters
    all_chars = letters + digits + symbols
    
    # Randomly choose characters for the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

# Example usage
print("Generated password:", generate_password(12))
