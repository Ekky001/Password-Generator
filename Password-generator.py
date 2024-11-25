import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters (!, @, #, etc.)
    
    # Combine all character sets
    all_characters = letters + digits + symbols
    
    # Ensure password length is valid
    if length < 4:
        return "Password length must be at least 4 characters!"
    
    # Randomly select at least one character from each set for stronger passwords
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle to ensure randomness
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)

def main():
    try:
        # User input for password length
        length = int(input("Enter the desired password length: "))
        
        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number for password length!")

if __name__ == "__main__":
    main()
