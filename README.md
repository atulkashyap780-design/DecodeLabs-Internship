🔐 Password Strength Checker

📌 Project Description

The Password Strength Checker is a Python-based cybersecurity project developed as part of Cyber Security Project 1 at DecodeLabs.

The purpose of this project is to evaluate the strength of a user's password and classify it as Weak, Medium, or Strong based on different security criteria.

The program checks:

- 🔹 Password length
- 🔹 Presence of uppercase letters
- 🔹 Presence of numbers
- 🔹 Presence of special symbols

The project demonstrates basic Python programming, string handling, conditional logic, and fundamental cybersecurity concepts.

⚙️ How It Works

The program asks the user to enter a password and then checks different characteristics of that password.

A score is calculated based on the security requirements:

Requirement| Score
Password has 8 or more characters| +1
Contains an uppercase letter| +1
Contains a number| +1
Contains a special symbol| +1

The final score is used to determine the password strength:

- 🔴 Weak — Score 0–2
- 🟡 Medium — Score 3
- 🟢 Strong — Score 4

Example

Enter your password: Atul@123

Password Strength : Strong

🛠️ Technologies Used

- Python 3
- Python "string" module
- Conditional statements
- String handling
- Character validation

▶️ How to Run

1. Install Python

Make sure Python 3 is installed on your computer.

You can check it using:

python --version

or:

python3 --version

2. Clone the Repository

git clone https://github.com/YOUR-USERNAME/password-strength-checker.git

3. Open the Project Folder

cd password-strength-checker

4. Run the Program

python password_strength_checker.py

If your system uses "python3", run:

python3 password_strength_checker.py

🧪 Example Test Cases

Weak Password

Enter your password: atul123

Password Strength : Weak

Medium Password

Enter your password: Atul1234

Password Strength : Medium

Strong Password

Enter your password: Atul@123

Password Strength : Strong

🎯 Learning Outcomes

Through this project, I practiced:

- String manipulation in Python
- Conditional statements
- Character validation
- Password security fundamentals
- Basic security logic
- Writing and testing a cybersecurity-related program

🚀 Future Improvements

The project can be further improved by adding:

- Common/leaked password detection
- Password length recommendations
- Lowercase character checking
- Password entropy calculation
- Feedback explaining why a password is weak
- A graphical user interface (GUI)

👨‍💻 Author

Atul Kashyap

Cyber Security Intern
DecodeLabs — 2026
