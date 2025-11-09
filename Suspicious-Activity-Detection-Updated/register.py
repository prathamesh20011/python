import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

class RegisterWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Register - Suspicious Activity Detection")
        self.window.geometry("400x500")
        self.window.configure(bg="#34495e")
        
        self.setup_ui()
        self.window.mainloop()
    
    def setup_ui(self):
        """Setup the registration UI"""
        # Title
        title = tk.Label(self.window, text="REGISTER", 
                        font=("Arial", 20, "bold"), bg="#34495e", fg="white")
        title.pack(pady=20)
        
        # Username
        tk.Label(self.window, text="Username:", font=("Arial", 12), 
                bg="#34495e", fg="white").pack(pady=5)
        self.username_entry = tk.Entry(self.window, font=("Arial", 12), width=25)
        self.username_entry.pack(pady=5)
        
        # Email
        tk.Label(self.window, text="Email:", font=("Arial", 12), 
                bg="#34495e", fg="white").pack(pady=5)
        self.email_entry = tk.Entry(self.window, font=("Arial", 12), width=25)
        self.email_entry.pack(pady=5)
        
        # Password
        tk.Label(self.window, text="Password:", font=("Arial", 12), 
                bg="#34495e", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.window, font=("Arial", 12), width=25, show="*")
        self.password_entry.pack(pady=5)
        
        # Confirm Password
        tk.Label(self.window, text="Confirm Password:", font=("Arial", 12), 
                bg="#34495e", fg="white").pack(pady=5)
        self.confirm_password_entry = tk.Entry(self.window, font=("Arial", 12), width=25, show="*")
        self.confirm_password_entry.pack(pady=5)
        
        # Buttons
        register_btn = tk.Button(self.window, text="REGISTER", command=self.register,
                               width=15, height=2, font=("Arial", 12, "bold"),
                               bg="#27ae60", fg="white")
        register_btn.pack(pady=20)
        
        back_btn = tk.Button(self.window, text="BACK TO MAIN", command=self.back_to_main,
                           width=15, height=1, font=("Arial", 10),
                           bg="#95a5a6", fg="white")
        back_btn.pack(pady=5)
    
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def register(self):
        """Handle user registration"""
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        # Validation
        if not username or not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format!")
            return
        
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters!")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        # Save to database
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                          (username, password, email))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", "Registration successful! You can now login.")
            self.show_login()
            
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {str(e)}")
    
    def show_login(self):
        """Navigate to login window"""
        from login import LoginWindow
        self.window.destroy()
        LoginWindow()
    
    def back_to_main(self):
        """Go back to main menu"""
        from main import SuspiciousActivityApp
        self.window.destroy()
        SuspiciousActivityApp()