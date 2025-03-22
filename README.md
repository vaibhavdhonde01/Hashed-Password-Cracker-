# Hashed-Password-Cracker-
Hashed Password Cracker is a GUI tool for recovering lost passwords and testing password security using a dictionary attack. It matches hashes with a precomputed list and generates SHA-256 hashes for given passwords. Ideal for security testing and research.

Hashed Password Cracker

Overview

Hashed Password Cracker is a GUI-based tool designed to help users recover lost passwords and test the strength of password implementations. The tool leverages a dictionary attack method to match precomputed hashes with plaintext passwords, allowing users to verify whether a password has been compromised or securely stored.

Features

Dictionary Attack: Matches input hashes with a precomputed list of password hashes.

Hash Lookup: Computes the SHA-256 hash of a given password to check if it exists in the dataset.

User-Friendly Interface: Built using Tkinter, making it easy to use for both technical and non-technical users.

Supports Common Hash Algorithms: Uses SHA-256 for hashing and comparison.

Use Cases

Password Recovery: Helps users retrieve lost passwords by checking against common password lists.

Security Testing: Assists cybersecurity professionals in evaluating the strength of password implementations.

Digital Forensics: Useful for forensic investigators in analyzing password security.

Installation

Prerequisites

Ensure you have Python 3.x installed on your system.

Steps to Install & Run

Clone this repository:

git clone https://github.com/yourusername/hashed-password-cracker.git
cd hashed-password-cracker

Install required dependencies:

pip install -r requirements.txt

Run the application:

python main.py

File Structure

├── hashed_password_cracker.py  # Main application file
├── password.txt                # List of common passwords
├── hashed.txt                  # Precomputed password hashes
├── README.md                   # Project documentation
├── requirements.txt             # Python dependencies

Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

License

This project is licensed under the MIT License.

Disclaimer

This tool is intended for educational and security research purposes only. Unauthorized password cracking is illegal and unethical. Use responsibly!

