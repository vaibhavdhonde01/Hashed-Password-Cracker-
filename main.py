import tkinter as tk
from tkinter import messagebox
import hashlib

# Load password and hash files
def load_data():
    with open("password.txt", "r") as f:
        passwords = [line.strip() for line in f]

    with open("hashed.txt", "r") as f:
        hashes = [line.strip() for line in f]

    return passwords, hashes

password_list, hash_list = load_data()

# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Dictionary attack method
def dictionary_attack(input_hash):
    for password, hash_value in zip(password_list, hash_list):
        if input_hash == hash_value:
            return password
    return None

# Reverse lookup for plaintext passwords
def find_hash(input_password):
    detected_hash = hash_password(input_password)  # Default SHA-256
    if detected_hash in hash_list:
        return detected_hash
    return None

# GUI Functions
def crack_hash():
    input_hash = hash_entry.get().strip()
    if not input_hash:
        messagebox.showerror("Error", "Please enter a hash value")
        return

    result = dictionary_attack(input_hash)
    if result:
        result_label.config(text=f"Password Found (Dictionary): {result}", fg="green")
    else:
        result_label.config(text="Password Not Found in Dictionary!", fg="red")

def find_password():
    input_password = password_entry.get().strip()
    if not input_password:
        messagebox.showerror("Error", "Please enter a password")
        return

    result = find_hash(input_password)
    if result:
        result_label.config(text=f"Hash Found: {result}", fg="blue")
    else:
        result_label.config(text="Hash Not Found!", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Hashed Password Cracker")
root.geometry("500x400")

# Title Label
tk.Label(root, text="Hashed Password Cracker", font=("Arial", 16, "bold")).pack(pady=10)

# Input for Hash Cracking (Dictionary)
tk.Label(root, text="Enter Hash Value:").pack()
hash_entry = tk.Entry(root, width=50)
hash_entry.pack(pady=5)
tk.Button(root, text="Crack Hash (Dictionary)", command=crack_hash, bg="orange", fg="white").pack(pady=5)

# Input for Password to Find Hash
tk.Label(root, text="Enter Plaintext Password:").pack()
password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)
tk.Button(root, text="Find Hash", command=find_password, bg="blue", fg="white").pack(pady=5)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

# Start GUI
root.mainloop()