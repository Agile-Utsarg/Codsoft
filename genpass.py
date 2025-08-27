import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Welcome to the Password Generator!")
 
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
      
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if _name_ == "_main_":
    main()
