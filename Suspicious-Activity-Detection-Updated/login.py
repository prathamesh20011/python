import tkinter as tk
from tkinter import messagebox
import sqlite3

class LoginWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login - Suspicious Activity Detection")
        self.window.geometry("400x350")
        self.window.configure(bg="#2c3e50")
        
        self.setup_ui()
        self.window.mainloop()
    
    def setup_ui(self):
        """Setup the login UI"""
        # Title
        title = tk.Label(self.window, text="LOGIN", 
                        font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
        title.pack(pady=30)
        
        # Username
        tk.Label(self.window, text="Username:", font=("Arial", 12), 
                bg="#2c3e50", fg="white").pack(pady=5)
        self.username_entry = tk.Entry(self.window, font=("Arial", 12), width=25)
        self.username_entry.pack(pady=5)
        
        # Password
        tk.Label(self.window, text="Password:", font=("Arial", 12), 
                bg="#2c3e50", fg="white").pack(pady=5)
        self.password_entry = tk.Entry(self.window, font=("Arial", 12), width=25, show="*")
        self.password_entry.pack(pady=5)
        
        # Buttons
        login_btn = tk.Button(self.window, text="LOGIN", command=self.login,
                             width=15, height=2, font=("Arial", 12, "bold"),
                             bg="#3498db", fg="white")
        login_btn.pack(pady=20)
        
        register_btn = tk.Button(self.window, text="CREATE ACCOUNT", command=self.show_register,
                               width=15, height=1, font=("Arial", 10),
                               bg="#27ae60", fg="white")
        register_btn.pack(pady=5)
        
        back_btn = tk.Button(self.window, text="BACK TO MAIN", command=self.back_to_main,
                           width=15, height=1, font=("Arial", 10),
                           bg="#95a5a6", fg="white")
        back_btn.pack(pady=5)
    
    def login(self):
        """Handle user login"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password!")
            return
        
        # Check credentials
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                          (username, password))
            user = cursor.fetchone()
            conn.close()
            
            if user:
                messagebox.showinfo("Success", f"Welcome {username}!")
                self.show_dashboard(username)
            else:
                messagebox.showerror("Error", "Invalid username or password!")
                
        except Exception as e:
            messagebox.showerror("Error", f"Login failed: {str(e)}")
    
    def show_dashboard(self, username):
        """Navigate to dashboard"""
        from dashboard import Dashboard
        self.window.destroy()
        Dashboard(username)
    
    def show_register(self):
        """Navigate to registration window"""
        from register import RegisterWindow
        self.window.destroy()
        RegisterWindow()
    
    def back_to_main(self):
        """Go back to main menu"""
        from main import SuspiciousActivityApp
        self.window.destroy()
        SuspiciousActivityApp()