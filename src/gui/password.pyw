# Using the text-based generator in a GUI instead
import secrets
import tkinter as tk
import string
from tkinter import BOTTOM, CENTER, messagebox
import pyperclip


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


# Copy the password to the clipboard
def copy_to_clipboard():
    out = secure_pass.get()
    pyperclip.copy(str(out))


# Generate the password
def sec_pass():
    try:
        p_length = int(pass_len.get())
        if p_length < 8 or p_length > 32:
            tk.messagebox.showerror("Error", "Password length must be between 8 and 32 characters")
            return
        new_pass = password.password_generator(p_length)
        secure_pass.set(new_pass)
    except:
        tk.messagebox.showerror("Error", "Password length must be an integer")



root = tk.Tk()
root.geometry("400x200")
root.resizable(0, 0)
root.title("Password Generator")

tk.Label(root, text='Password Generator', font='arial 10 bold', pady=10).pack()
tk.Label(root, text='By @mbutcherdev', font='arial 8 italic').pack(side=BOTTOM)

# Set password length
tk.Label(root, text='Password Length', font='arial 10 bold', justify=CENTER).pack()
pass_len = tk.IntVar()
tk.Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=10, justify=CENTER).pack()

password = PasswordGeneration()
secure_pass = tk.StringVar()

tk.Button(root, text="Generate Password", command=sec_pass).pack(pady=5)
tk.Entry(root, textvariable=secure_pass, show="*", width=50).pack()

tk.Button(root, text='Copy to clipboard', command=copy_to_clipboard).pack(pady=5)

root.mainloop()
