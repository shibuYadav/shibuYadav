import tkinter as tk
from tkinter import messagebox
import math
import threading

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to find factors
def find_factors(num):
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return factors

# Function to analyze the number
def analyze_number():
    result_label.config(text="Analyzing... Please wait.", fg="#FF5733")
    
    def process():
        try:
            num = int(entry.get())
            if num < 0:
                messagebox.showerror("Invalid Input", "Please enter a positive integer.")
                return
            
            # Prime Check
            prime_status = "Yes" if is_prime(num) else "No"
            
            # Factors
            factors = find_factors(num)
            
            # Mathematical Properties
            square = num ** 2
            square_root = round(math.sqrt(num), 4)
            cube = num ** 3
            
            result = f"""
            ✅ Number: {num}
            ✅ Prime: {prime_status}
            ✅ Factors: {factors}
            ✅ Square: {square}
            ✅ Square Root: {square_root}
            ✅ Cube: {cube}
            """
            
            result_label.config(text=result, fg="#00FF00")
        
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
    
    # Run the logic in a separate thread to avoid UI freezing
    threading.Thread(target=process).start()

# Function to clear the input and result
def clear():
    entry.delete(0, tk.END)
    result_label.config(text="", fg="#FFFFFF")

# Initialize the main window
root = tk.Tk()
root.title("Number Analyzer Tool")
root.geometry("500x400")
root.configure(bg="#2C2C2C")

# Heading Label
heading = tk.Label(root, text="🔍 Number Analyzer", font=("Arial", 24, "bold"), fg="#FF5733", bg="#2C2C2C")
heading.pack(pady=10)

# Input Field
entry = tk.Entry(root, font=("Arial", 18), width=15, bg="#333333", fg="#FFFFFF", justify="center", relief="flat", borderwidth=2)
entry.pack(pady=5)

# Analyze Button
analyze_btn = tk.Button(root, text="Analyze", command=analyze_number, font=("Arial", 16, "bold"), bg="#FF5733", fg="#FFFFFF", activebackground="#FF8C00", relief="flat", borderwidth=0)
analyze_btn.pack(pady=5)

# Clear Button
clear_btn = tk.Button(root, text="Clear", command=clear, font=("Arial", 16, "bold"), bg="#555555", fg="#FFFFFF", activebackground="#777777", relief="flat", borderwidth=0)
clear_btn.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="#FFFFFF", bg="#2C2C2C", justify="left", wraplength=480)
result_label.pack(pady=10)

# Footer
footer = tk.Label(root, text="Developed by Shibu", font=("Arial", 12), fg="#777777", bg="#2C2C2C")
footer.pack(side="bottom", pady=5)

# Run the main loop
root.mainloop()
