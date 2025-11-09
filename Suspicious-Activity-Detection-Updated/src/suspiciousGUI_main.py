import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import time

global fn
fn = ""

root = tk.Tk()
root.configure(background="brown")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Suspicious Activity Detection ")

# For background Image
try:
    image2 = Image.open('src/new5.jpg')
    image2 = image2.resize((1530, 900), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=70)
except:
    # Fallback if image not found
    pass

label_l1 = tk.Label(root, text="Suspicious Activity Detection ",font=("Times New Roman", 35, 'bold'),
                    background="#000000", fg="Magenta", width=60, height=2)
label_l1.place(x=0, y=0)

def reg():
    from subprocess import call
    call(["python","src/suspicious_registration.py"])

def log():
    from subprocess import call
    call(["python","src/suspicious_login.py"])
    
def window():
    root.destroy()

button1 = tk.Button(root, text="LOGIN", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="brown")
button1.place(x=20, y=190)

button2 = tk.Button(root, text="REGISTER",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="brown")
button2.place(x=20, y=300)

root.mainloop()