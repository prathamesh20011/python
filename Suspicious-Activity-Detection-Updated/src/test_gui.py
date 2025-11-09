import tkinter as tk

# Simple test to see if GUI opens
root = tk.Tk()
root.title("Test - GUI Working")
root.geometry("400x200")

label = tk.Label(root, text="GUI is working!", font=("Arial", 20))
label.pack(pady=50)

button = tk.Button(root, text="Close", command=root.destroy)
button.pack()

root.mainloop()