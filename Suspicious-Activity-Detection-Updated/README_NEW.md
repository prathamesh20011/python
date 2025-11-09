# Suspicious Activity Detection System

A complete suspicious activity detection system with user authentication and file analysis capabilities.

## Features

- **User Registration & Login System**
- **Dashboard Interface** 
- **Video Analysis** (MP4, AVI files)
- **Image Analysis** (JPG, PNG, BMP files)
- **Real-time Detection Results**
- **Alert Notifications**

## Installation

1. Install required packages:
```bash
pip install -r requirements_new.txt
```

## Usage

1. **Start the application:**
```bash
python main.py
```

2. **Register a new account:**
   - Click "REGISTER"
   - Fill in username, email, password
   - Click "REGISTER"

3. **Login:**
   - Click "LOGIN" 
   - Enter your credentials
   - Click "LOGIN"

4. **Use Dashboard:**
   - **For Videos:** Click "SELECT VIDEO (MP4)" → Choose MP4/AVI file
   - **For Images:** Click "SELECT IMAGE" → Choose JPG/PNG/BMP file
   - View detection results in the results panel

## Detection Results

- **Suspicious Activity:** Red alerts with warnings
- **Normal Activity:** Green confirmations
- **Detailed Analysis:** Frame-by-frame for videos, comprehensive for images

## Project Structure

```
├── main.py           # Main entry point
├── login.py          # Login functionality  
├── register.py       # Registration functionality
├── dashboard.py      # Main dashboard with detection
├── requirements_new.txt  # Dependencies
└── users.db          # SQLite database (auto-created)
```

## System Requirements

- Python 3.7+
- OpenCV
- Pillow
- NumPy
- Tkinter (included with Python)