import random
import string

def generate_password(length, complexity):
    characters = ''
    if 'letters' in complexity:
        characters += string.ascii_letters
    if 'numbers' in complexity:
        characters += string.digits
    if 'symbols' in complexity:
        characters += string.punctuation

    if len(characters) == 0:
        print("Please select at least one type of character for the password.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity (letters/numbers/symbols, separated by commas): ").split(',')

    password = generate_password(length, complexity)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
