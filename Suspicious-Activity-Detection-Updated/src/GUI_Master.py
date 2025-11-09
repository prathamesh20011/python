import tkinter as tk
from PIL import Image , ImageTk
import csv
from datetime import date
import time
import numpy as np
import cv2
from tkinter.filedialog import askopenfilename
import os
import shutil
import pickle

root = tk.Tk()
root.state('zoomed')
root.title("Suspicious Activity Detection")

current_path = str(os.path.dirname(os.path.realpath('__file__')))
basepath = current_path + "\\\\" 

# Background setup
try:
    img = Image.open("back5.jpg")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    bg = img.resize((w,h),Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(bg)
    bg_lbl = tk.Label(root,image=bg_img)
    bg_lbl.place(x=0,y=0)
except:
    pass

heading = tk.Label(root,text="Suspicious Activity Detection",width=25,font=("Times New Roman",45,'bold'),bg="#192841",fg="white")
heading.place(x=240,y=0)

def create_folder(FolderN):
    dst = os.getcwd() + "\\\\" + FolderN
    if not os.path.exists(dst):
        os.makedirs(dst)
    else:
        shutil.rmtree(dst, ignore_errors=True)
        os.makedirs(dst)

def CLOSE():
    root.destroy()
    
def update_label(str_T):
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25),bg='cyan',fg='black' )
    result_label.place(x=400, y=400)

def run_video(VPathName,XV,YV,S1,S2):
    cap = cv2.VideoCapture(VPathName)
    
    def show_frame():
        ret, frame = cap.read()
        cap.set(cv2.CAP_PROP_FPS, 30)
        
        out = cv2.transpose(frame)
        out = cv2.flip(out,flipCode=0)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image).resize((S1, S2))
        imgtk = ImageTk.PhotoImage(image = img)
        
        lmain = tk.Label(root)
        lmain.place(x=XV, y=YV)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)
                
    show_frame()
        
def VIDEO():
    global fn
    fn = ""
    fileName = askopenfilename(initialdir='/dataset', title='Select video',
                               filetypes=[("MP4 files", "*.mp4"), ("all files", "*.*")])
    fn = fileName
    if fileName:
        Sel_F = fileName.split('/').pop()
        Sel_F = Sel_F.split('.').pop()
        
        if Sel_F != 'mp4':
            print("Please select a .mp4 video file!")
        else:
            run_video(fn,560, 190,753, 485)

def show_FDD_video(video_path):
    ''' Display video with suspicious activity detection '''
    
    img_cols, img_rows = 64,64
    
    # Load mock model for demo
    try:
        with open('abnormalevent.pkl', 'rb') as f:
            FALLModel = pickle.load(f)
    except:
        class MockModel:
            def predict(self, X):
                return [[0.3, 0.7]]  # Mock prediction
        FALLModel = MockModel()
    
    video = cv2.VideoCapture(video_path)

    if (not video.isOpened()):
        print("{} cannot be opened".format(video_path))
        return

    font = cv2.FONT_HERSHEY_SIMPLEX
    green = (0, 255, 0) 
    red = (0, 0, 255)
    line_type = cv2.LINE_AA
    i = 1
    
    while True:
        ret, frame = video.read()
        
        if not ret:
            break
            
        img = cv2.resize(frame,(img_cols, img_rows),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.array(img)
        
        X_img = img.reshape(-1, img_cols, img_rows, 1)
        X_img = X_img.astype('float32')
        X_img /= 255
        
        predicted = FALLModel.predict(X_img)

        if predicted[0][0] < 0.5:
            predicted[0][0] = 0
            predicted[0][1] = 1
            label = 1
        else:
            predicted[0][0] = 1
            predicted[0][1] = 0
            label = 0
          
        frame_num = int(i)
        label_text = ""
        color = (255, 255, 255)
        
        if label == 1:
            label_text = "Suspicious Activity Detected"
            color = red
            try:
                from subprocess import call
                call(["python", "mail.py"])  
            except:
                print("Email notification failed")
        else:
            label_text = "Normal Activity detected"
            color = green

        frame = cv2.putText(
            frame, "Frame: {}".format(frame_num), (5, 30),
            fontFace = font, fontScale = 1, color = color, lineType = line_type
        )
        frame = cv2.putText(
            frame, "Label: {}".format(label_text), (5, 60),
            fontFace = font, fontScale =1, color = color, lineType = line_type
        )

        i = i + 1
        cv2.imshow('Suspicious Activity Detection', frame)
        if cv2.waitKey(30) == 27:  # ESC key
            break

    video.release()
    cv2.destroyAllWindows()
       
def Video_Verify():
    global fn
    fileName = askopenfilename(initialdir='/dataset', title='Select video',
                               filetypes=[("MP4 files", "*.mp4"), ("all files", "*.*")])
    fn = fileName
    
    if fileName:
        Sel_F = fileName.split('/').pop()
        Sel_F = Sel_F.split('.').pop()
        
        if Sel_F != 'mp4':
            print("Please select a .mp4 video file!")
        else:
            show_FDD_video(fn)
            
button5 = tk.Button(root,command = Video_Verify, text="Suspicious Activity Detection", width=20,font=("Times new roman", 25, "bold"),bg="cyan",fg="black")
button5.place(x=100,y=150)

close = tk.Button(root,command = CLOSE, text="Exit", width=20,font=("Times new roman", 25, "bold"),bg="red",fg="white")
close.place(x=100,y=300)

root.mainloop()