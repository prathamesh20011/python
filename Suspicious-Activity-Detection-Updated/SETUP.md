# Setup Instructions

## Quick Start

1. **Navigate to project directory:**
   ```bash
   cd "c:\Users\prath\Downloads\Suspicious-Activity-Detection-Updated"
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project:**
   ```bash
   python run_project.py
   ```

## Manual Setup

If you prefer to run components individually:

```bash
# Main GUI (Login/Register)
python src\suspiciousGUI_main.py

# Detection Interface
python src\GUI_Master.py
```

## Email Configuration

To enable email alerts:
1. Open `src\mail.py`
2. Update email credentials:
   - `SENDER_EMAIL` - Your Gmail address
   - `APP_PASSWORD` - Your Gmail app password
   - `RECIPIENT_EMAIL` - Alert recipient email

## Features Working

✅ User registration and login
✅ Video file selection and playback
✅ Mock suspicious activity detection
✅ GUI interfaces with backgrounds
✅ Email notification system
✅ Cross-platform compatibility

## Troubleshooting

- If images don't load, run: `python src\create_assets.py`
- For email issues, check Gmail app password setup
- Ensure Python 3.7+ is installed