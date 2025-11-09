#!/usr/bin/env python3
"""
Suspicious Activity Detection System
Main Entry Point
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

class SuspiciousActivityApp:
    def __init__(self):
        self.setup_database()
        self.show_main_menu()
    
    def setup_database(self):
        """Initialize the database"""
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def show_main_menu(self):
        """Show the main menu"""
        self.root = tk.Tk()
        self.root.title("Suspicious Activity Detection System")
        self.root.geometry("400x300")
        self.root.configure(bg="#2c3e50")
        
        # Title
        title = tk.Label(self.root, text="Suspicious Activity Detection", 
                        font=("Arial", 18, "bold"), bg="#2c3e50", fg="white")
        title.pack(pady=30)
        
        # Buttons
        login_btn = tk.Button(self.root, text="LOGIN", command=self.show_login,
                             width=20, height=2, font=("Arial", 12, "bold"),
                             bg="#3498db", fg="white")
        login_btn.pack(pady=10)
        
        register_btn = tk.Button(self.root, text="REGISTER", command=self.show_register,
                                width=20, height=2, font=("Arial", 12, "bold"),
                                bg="#27ae60", fg="white")
        register_btn.pack(pady=10)
        
        exit_btn = tk.Button(self.root, text="EXIT", command=self.root.quit,
                            width=20, height=2, font=("Arial", 12, "bold"),
                            bg="#e74c3c", fg="white")
        exit_btn.pack(pady=10)
        
        self.root.mainloop()
    
    def show_login(self):
        """Show login window"""
        from login import LoginWindow
        self.root.destroy()
        LoginWindow()
    
    def show_register(self):
        """Show registration window"""
        from register import RegisterWindow
        self.root.destroy()
        RegisterWindow()

if __name__ == "__main__":
    app = SuspiciousActivityApp()