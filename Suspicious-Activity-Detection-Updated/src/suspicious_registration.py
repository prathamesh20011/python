import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re

window = tk.Tk()
window.geometry("600x800")
window.title("REGISTRATION FORM")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()

# Database setup
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()

def password_check(passwd): 
    SpecialSym =['$', '@', '#', '%'] 
    val = True
    
    if len(passwd) < 6: 
        val = False
    if len(passwd) > 20: 
        val = False
    if not any(char.isdigit() for char in passwd): 
        val = False
    if not any(char.isupper() for char in passwd): 
        val = False
    if not any(char.islower() for char in passwd): 
        val = False
    if not any(char in SpecialSym for char in passwd): 
        val = False
    return val

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    find_user = ('SELECT * FROM registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    regex='^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False

    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "Please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Different One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif (var.get() == 0):
        ms.showinfo("Message", "Please select gender")
    elif not password_check(pwd):
        ms.showinfo("Message", "Password must contain at least 1 uppercase, 1 symbol, 1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password and Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))
            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully!')
            window.destroy()
            from subprocess import call
            call(['python','suspicious_login.py'])

# Background Image
try:
    image2 = Image.open('register.jpg')
    image2 = image2.resize((600, 800), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(window, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0)
except:
    pass

l1 = tk.Label(window, text="REGISTRATION FORM", font=("Times new roman",25, "bold"), bg="#FFF5EE", fg="#800517")
l1.place(x=160, y=50)

l2 = tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=100, y=150)
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=300, y=150)

l3 = tk.Label(window, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l3.place(x=100, y=200)
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=300, y=200)

l5 = tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l5.place(x=100, y=250)
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=300, y=250)

l6 = tk.Label(window, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l6.place(x=100, y=300)
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=300, y=300)

l7 = tk.Label(window, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l7.place(x=100, y=350)
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=var, value=1).place(x=300, y=350)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=var, value=2).place(x=400, y=350)

l8 = tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l8.place(x=100, y=400)
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=300, y=400)

l4 = tk.Label(window, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l4.place(x=100, y=450)
t3 = tk.Entry(window, textvar=username, width=20, font=('', 15))
t3.place(x=300, y=450)

l9 = tk.Label(window, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l9.place(x=100, y=500)
t9 = tk.Entry(window, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=300, y=500)

l10 = tk.Label(window, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"), bg="snow")
l10.place(x=100, y=550)
t10 = tk.Entry(window, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=300, y=550)

btn = tk.Button(window, text="Register", bg="red",font=("",20),fg="white", width=9, height=1, command=insert)
btn.place(x=230, y=620)

window.mainloop()