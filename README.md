SMART PASSWORD STRENGTH CHECKER

The Smart Password Strength Checker is a Python-based GUI application built using Tkinter.
It analyzes passwords in real time and provides:

•	Strength classification

•	Entropy value

•	Visual strength indicator bar

•	Suggestions for improvement

•	Detection of weak patterns and repeated characters

This tool helps users understand the security of their passwords and encourages strong password creation.
FEATURES:
1)	Automatically evaluates password strength as per the user types.
2)	Compute password entropy in bits to measure unpredictability.
3)	Identifies common sequences like:- ‘qwerty’ , ‘12345’ , ‘password’ , ‘admin’ , etc
4)	Colored bar dynamically updates with score.
5)	Provides meaningful recommendations for improving quality.
6)	Evaluate lowercase , uppercase , numbers , and special characters
TECHNOLOGIES & TOOLS USED:
Technology/Tool	                          Purpose
Python 3 	                                Primary programming language
Tkinter	                                  GUI Framework
Regex(re module)	                        Pattern detection & validation
Math module	                              Entropy calculation
ReportLab(only for PDF generation tasks)	Used if exporting documentation (not part of main program)

INSTALLATION & SETUP GUIDE:
•	Ensure you have Python 3.8 + installed.
•	Create a file named password_checker.py and paste your Tkinter program code inside it.
•	The program will run and GUI window will open
Instructions for Testing:
Follow these steps to verify all features:
1. Test Weak Passwords
Examples to try:
•	12345
•	Password
•	qwerty123
•	aaaaaaa
Expected result:
•	Low entropy
•	Red or Orange strength bar
•	Multiple suggestions
