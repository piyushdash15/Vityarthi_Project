import tkinter as tk
import math
import re


WEAK_PATTERNS = [
    "qwerty", "asdf", "zxcv", "password", "letmein",
    "admin", "welcome", "iloveyou", "12345", "11111"
]

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset += 33
    return len(password) * math.log2(charset) if charset else 0

def contains_weak_pattern(password):
    pw = password.lower()
    return any(p in pw for p in WEAK_PATTERNS)

def score_password(pwd):
    score = 0
    suggestions = []

    length = len(pwd)
    entropy = calculate_entropy(pwd)

    # Length scoring
    if length >= 16: score += 3
    elif length >= 12: score += 2
    elif length >= 8: score += 1
    else: suggestions.append("Use at least 12–16 characters.")

    # Character diversity
    if re.search(r'[a-z]', pwd): score += 1
    else: suggestions.append("Add lowercase letters.")

    if re.search(r'[A-Z]', pwd): score += 1
    else: suggestions.append("Add uppercase letters.")

    if re.search(r'[0-9]', pwd): score += 1
    else: suggestions.append("Add digits.")

    if re.search(r'[^a-zA-Z0-9]', pwd): score += 1
    else: suggestions.append("Add special characters (!@#$).")

    # Weak patterns
    if contains_weak_pattern(pwd):
        score -= 2
        suggestions.append("Avoid common patterns (qwerty, 12345, password).")

    # Repeating characters
    if len(pwd) > 0 and len(set(pwd)) <= 2:
        score -= 2
        suggestions.append("Avoid repeating characters too much.")

    # Entropy
    if entropy < 40:
        suggestions.append("Increase complexity — entropy too low.")
    elif entropy > 60:
        score += 1

    # Strength level
    if score <= 2:
        strength = "Very Weak"
        color = "#e74c3c"     # Red
    elif score <= 4:
        strength = "Weak"
        color = "#e67e22"     # Orange
    elif score <= 6:
        strength = "Moderate"
        color = "#f1c40f"     # Yellow
    elif score <= 8:
        strength = "Strong"
        color = "#2ecc71"     # Green
    else:
        strength = "Very Strong"
        color = "#3498db"     # Blue

    return strength, entropy, suggestions, score, color


def check_password(event=None):
    pwd = password_var.get()

    strength, entropy, suggestions, score, color = score_password(pwd)

    strength_label.config(text=f"Strength: {strength}")
    entropy_label.config(text=f"Entropy: {entropy:.2f} bits")

    # Update the custom bar
    bar_canvas.delete("all")
    width = (score / 10) * 300
    bar_canvas.create_rectangle(0, 0, width, 25, fill=color, outline="")

    # Suggestions
    suggestions_box.config(state="normal")
    suggestions_box.delete("1.0", tk.END)

    if len(suggestions) == 0:
        suggestions_box.insert(tk.END, "Great password! No improvements needed.")
    else:
        for s in suggestions:
            suggestions_box.insert(tk.END, "• " + s + "\n")

    suggestions_box.config(state="disabled")


root = tk.Tk()
root.title("Smart Password Checker")
root.geometry("460x380")
root.resizable(False, False)

title_label = tk.Label(root, text="Smart Password Checker", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), show="*", width=30)
password_entry.pack()
password_entry.bind("<KeyRelease>", check_password)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12))
strength_label.pack(pady=5)

entropy_label = tk.Label(root, text="Entropy: ", font=("Arial", 12))
entropy_label.pack(pady=5)

# CUSTOM COLORED BAR (Canvas-based)
bar_canvas = tk.Canvas(root, width=300, height=25, bg="#ddd", highlightthickness=0)
bar_canvas.pack(pady=10)

tk.Label(root, text="Suggestions:", font=("Arial", 12, "bold")).pack()

suggestions_box = tk.Text(root, height=7, width=50, state="disabled", font=("Arial", 10))
suggestions_box.pack(pady=5)

root.mainloop()