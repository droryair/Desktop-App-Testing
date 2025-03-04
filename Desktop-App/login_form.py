import tkinter as tk
from tkinter import messagebox

# Function to validate login credentials
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "testuser" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, testuser!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
app = tk.Tk()
app.title("Login Form")
app.geometry("300x200")

# Create and place the username label and entry
username_label = tk.Label(app, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(app)
username_entry.pack(pady=5)

# Create and place the password label and entry
password_label = tk.Label(app, text="Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(app, show="*")
password_entry.pack(pady=5)

# Create and place the login button
login_button = tk.Button(app, text="Login", command=validate_login)
login_button.pack(pady=20)

# Run the application
app.mainloop()
