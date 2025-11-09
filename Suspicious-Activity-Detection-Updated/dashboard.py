import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import os

class Dashboard:
    def __init__(self, username):
        self.username = username
        self.window = tk.Tk()
        self.window.title(f"Dashboard - Welcome {username}")
        self.window.geometry("800x600")
        self.window.configure(bg="#2c3e50")
        
        self.setup_ui()
        self.window.mainloop()
    
    def setup_ui(self):
        """Setup the dashboard UI"""
        # Header
        header_frame = tk.Frame(self.window, bg="#34495e", height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        title = tk.Label(header_frame, text=f"Welcome, {self.username}!", 
                        font=("Arial", 18, "bold"), bg="#34495e", fg="white")
        title.pack(pady=20)
        
        # Main content area
        main_frame = tk.Frame(self.window, bg="#2c3e50")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Instructions
        instructions = tk.Label(main_frame, 
                              text="Select a video or image file to detect suspicious activities",
                              font=("Arial", 14), bg="#2c3e50", fg="white")
        instructions.pack(pady=20)
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg="#2c3e50")
        button_frame.pack(pady=20)
        
        video_btn = tk.Button(button_frame, text="SELECT VIDEO (MP4)", 
                             command=self.select_video,
                             width=20, height=2, font=("Arial", 12, "bold"),
                             bg="#e74c3c", fg="white")
        video_btn.pack(side="left", padx=10)
        
        image_btn = tk.Button(button_frame, text="SELECT IMAGE", 
                             command=self.select_image,
                             width=20, height=2, font=("Arial", 12, "bold"),
                             bg="#f39c12", fg="white")
        image_btn.pack(side="left", padx=10)
        
        # Results area
        self.results_frame = tk.Frame(main_frame, bg="#34495e", relief="raised", bd=2)
        self.results_frame.pack(fill="both", expand=True, pady=20)
        
        results_title = tk.Label(self.results_frame, text="Detection Results", 
                               font=("Arial", 16, "bold"), bg="#34495e", fg="white")
        results_title.pack(pady=10)
        
        self.results_text = tk.Text(self.results_frame, height=10, width=70, 
                                   font=("Arial", 11), bg="white", fg="black")
        self.results_text.pack(pady=10, padx=10)
        
        # Logout button
        logout_btn = tk.Button(main_frame, text="LOGOUT", command=self.logout,
                              width=15, height=1, font=("Arial", 10),
                              bg="#95a5a6", fg="white")
        logout_btn.pack(pady=10)
    
    def select_video(self):
        """Handle video file selection"""
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[("MP4 files", "*.mp4"), ("AVI files", "*.avi"), ("All files", "*.*")]
        )
        
        if file_path:
            if not file_path.lower().endswith(('.mp4', '.avi')):
                messagebox.showerror("Error", "Please select a valid video file (MP4 or AVI)")
                return
            
            self.analyze_video(file_path)
    
    def select_image(self):
        """Handle image file selection"""
        file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp"), ("All files", "*.*")]
        )
        
        if file_path:
            if not file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                messagebox.showerror("Error", "Please select a valid image file")
                return
            
            self.analyze_image(file_path)
    
    def analyze_video(self, video_path):
        """Analyze video for suspicious activities"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Analyzing video: {os.path.basename(video_path)}\\n\\n")
        self.window.update()
        
        try:
            cap = cv2.VideoCapture(video_path)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            suspicious_count = 0
            normal_count = 0
            frame_count = 0
            
            self.results_text.insert(tk.END, f"Video Info:\\n")
            self.results_text.insert(tk.END, f"- Total Frames: {total_frames}\\n")
            self.results_text.insert(tk.END, f"- FPS: {fps:.2f}\\n")
            self.results_text.insert(tk.END, f"- Duration: {total_frames/fps:.2f} seconds\\n\\n")
            self.results_text.insert(tk.END, "Analysis Results:\\n")
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame_count += 1
                
                # Mock detection logic (replace with actual ML model)
                detection_result = self.mock_detection(frame)
                
                if detection_result == "suspicious":
                    suspicious_count += 1
                    if suspicious_count <= 5:  # Show first 5 detections
                        timestamp = frame_count / fps
                        self.results_text.insert(tk.END, 
                            f"⚠️  SUSPICIOUS ACTIVITY detected at {timestamp:.2f}s (Frame {frame_count})\\n")
                else:
                    normal_count += 1
                
                # Update progress every 30 frames
                if frame_count % 30 == 0:
                    progress = (frame_count / total_frames) * 100
                    self.results_text.insert(tk.END, f"Progress: {progress:.1f}%\\n")
                    self.window.update()
            
            cap.release()
            
            # Final results
            self.results_text.insert(tk.END, f"\\n=== ANALYSIS COMPLETE ===\\n")
            self.results_text.insert(tk.END, f"Total Frames Analyzed: {frame_count}\\n")
            self.results_text.insert(tk.END, f"Suspicious Activities: {suspicious_count}\\n")
            self.results_text.insert(tk.END, f"Normal Activities: {normal_count}\\n")
            
            if suspicious_count > 0:
                self.results_text.insert(tk.END, f"\\n🚨 WARNING: {suspicious_count} suspicious activities detected!\\n")
                messagebox.showwarning("Detection Alert", 
                    f"Suspicious activities detected in video!\\nCount: {suspicious_count}")
            else:
                self.results_text.insert(tk.END, f"\\n✅ No suspicious activities detected.\\n")
                messagebox.showinfo("Analysis Complete", "No suspicious activities found in the video.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Video analysis failed: {str(e)}")
    
    def analyze_image(self, image_path):
        """Analyze image for suspicious activities"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Analyzing image: {os.path.basename(image_path)}\\n\\n")
        
        try:
            # Load and analyze image
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError("Could not load image")
            
            height, width = image.shape[:2]
            self.results_text.insert(tk.END, f"Image Info:\\n")
            self.results_text.insert(tk.END, f"- Dimensions: {width} x {height}\\n")
            self.results_text.insert(tk.END, f"- File: {os.path.basename(image_path)}\\n\\n")
            
            # Mock detection logic
            detection_result = self.mock_detection(image)
            
            self.results_text.insert(tk.END, "Analysis Results:\\n")
            
            if detection_result == "suspicious":
                self.results_text.insert(tk.END, "🚨 SUSPICIOUS ACTIVITY DETECTED!\\n")
                self.results_text.insert(tk.END, "- Potential threat identified\\n")
                self.results_text.insert(tk.END, "- Recommend immediate attention\\n")
                messagebox.showwarning("Detection Alert", "Suspicious activity detected in the image!")
            else:
                self.results_text.insert(tk.END, "✅ NORMAL ACTIVITY DETECTED\\n")
                self.results_text.insert(tk.END, "- No threats identified\\n")
                self.results_text.insert(tk.END, "- Image appears safe\\n")
                messagebox.showinfo("Analysis Complete", "No suspicious activities found in the image.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Image analysis failed: {str(e)}")
    
    def mock_detection(self, frame):
        """Mock detection algorithm (replace with actual ML model)"""
        # Simple mock logic based on image properties
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Calculate some basic features
        mean_intensity = np.mean(gray)
        std_intensity = np.std(gray)
        
        # Mock decision logic (replace with trained model)
        if mean_intensity < 50 or std_intensity > 80:
            return "suspicious"
        else:
            return "normal"
    
    def logout(self):
        """Handle user logout"""
        from main import SuspiciousActivityApp
        self.window.destroy()
        SuspiciousActivityApp()