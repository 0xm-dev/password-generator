# Password generator in Python

import secrets
import string


class PasswordGeneration:
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.punctuation = string.punctuation
        self.alphabet = self.letters + self.digits + self.punctuation
        self.password = ""

    def password_generator(self, x):
        while True:
            self.password = ''.join(secrets.choice(self.alphabet) for i in range(x))
            if (any(char in self.letters for char in self.password) and sum(
                    char in self.punctuation for char in self.password) >= 3):
                break
        return self.password


def main():
    pwd = PasswordGeneration()
    while True:
        try:
            pass_length = int(input("Enter the length of the password: "))
            if pass_length <= 8:
                print("Password length must be greater than 8")
            else:
                print(f"Your password: {pwd.password_generator(pass_length)}")
                break
        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()
