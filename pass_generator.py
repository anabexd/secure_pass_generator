import random
import string
try:
    import pyperclip
except ImportError:
    pyperclip = None
from art import text2art
from colorama import init, Fore, Style

init()

def generate_password(length, include_lower_case, include_upper_case, include_numbers, include_specials):
    characters = ""
    if include_lower_case:
        characters += string.ascii_lowercase
    if include_upper_case:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_specials:
        characters += string.punctuation
    
    if not characters:
        return "No character type selected!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    ascii_art = text2art("Secure Password Generator", font='small',chr_ignore=True)
    print(Fore.GREEN + ascii_art)
    print(Style.RESET_ALL)  # Reset colors to default after printing
    length = int(input("Type the password length: "))
    include_lower_case = input("Include lower case? (y/n): ").lower() == 'y'
    include_upper_case = input("Include upper case? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_specials = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, include_lower_case, include_upper_case, include_numbers, include_specials)
    print(f"Password: {password}")

    if pyperclip:
        pyperclip.copy(password)
        print("Password has been copied to clipboard")

if __name__ == "__main__":
    main()
