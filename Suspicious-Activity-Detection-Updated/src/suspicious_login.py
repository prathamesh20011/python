import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re

root = tk.Tk()
root.configure(background="black")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")

username = tk.StringVar()
password = tk.StringVar()

# For background Image
try:
    image2 = Image.open('1.jpg')
    image2 = image2.resize((w,h), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0)
except:
    pass

def registration():
    from subprocess import call
    call(["python","suspicious_registration.py"])
    root.destroy()

def login():
    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            ms.showinfo("Message", "Login successful")
            root.destroy()
            # Test simple GUI first
            import os
            os.system('python test_gui.py')
            # Then open main GUI
            os.system('python GUI_Master.py')
         else:
           ms.showerror('Error!', 'Username or Password not found.')

title=tk.Label(root, text="Login Here", font=("Algerian", 30, "bold","italic"),bd=5,bg="black",fg="white")
title.place(x=600,y=190,width=250)
        
Login_frame=tk.Frame(root,bg="#8B1C62")
Login_frame.place(x=500,y=300)
        
logolbl=tk.Label(Login_frame,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Username",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="Green",fg="black")
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="red",fg="black")
btn_reg.grid(row=3,column=0,pady=10)

root.mainloop()