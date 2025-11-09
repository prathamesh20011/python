#!/usr/bin/env python3
"""
Suspicious Activity Detection Project Launcher
"""

import os
import sys
import subprocess

def main():
    print("=" * 60)
    print("    SUSPICIOUS ACTIVITY DETECTION SYSTEM")
    print("=" * 60)
    print()
    print("Choose an option:")
    print("1. Start Main Application (Login/Register)")
    print("2. Start Detection Interface Directly")
    print("3. Exit")
    print()
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\nStarting Main Application...")
            try:
                subprocess.run([sys.executable, "src/suspiciousGUI_main.py"], check=True)
            except Exception as e:
                print(f"Error: {e}")
            break
            
        elif choice == '2':
            print("\nStarting Detection Interface...")
            try:
                subprocess.run([sys.executable, "src/GUI_Master.py"], check=True)
            except Exception as e:
                print(f"Error: {e}")
            break
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()