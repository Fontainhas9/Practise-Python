import random
import string

def generate_password(length):
    """Generate a random password with given length"""
    # Define all the possible characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use random.choices() to select `length` number of characters from the pool of `characters`
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    # Ask the user for the desired length of the password
    length = int(input("How many characters should the password be? "))
    
    # Generate a password and print it out
    password = generate_password(length)
    print("Your new password is:", password)

if __name__ == "__main__":
    main()
