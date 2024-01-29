import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        password_length = int(length_entry.get())
        
        if password_length < 1:
            result_label.config(text="Please enter a valid password length.")
        else:
            generated_password = generate_password(password_length)
            result_label.config(text="Generated Password: " + generated_password)
    
    except ValueError:
        result_label.config(text="Please enter a valid numerical password length.")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create and place widgets in the window
length_label = ttk.Label(app, text="Enter Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = ttk.Entry(app)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(app, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = ttk.Label(app, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the application
app.mainloop()
