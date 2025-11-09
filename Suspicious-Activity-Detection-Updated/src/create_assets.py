"""
Create required background images and mock model
"""

from PIL import Image, ImageDraw
import pickle
import numpy as np

def create_background_images():
    """Create background images for the GUI"""
    
    # Main GUI background
    img1 = Image.new('RGB', (1530, 900), (50, 50, 100))
    draw1 = ImageDraw.Draw(img1)
    draw1.text((765, 450), "Suspicious Activity Detection", fill='white', anchor='mm')
    img1.save('new5.jpg')
    
    # Detection interface background
    img2 = Image.new('RGB', (1920, 1080), (30, 30, 60))
    draw2 = ImageDraw.Draw(img2)
    draw2.text((960, 540), "Detection Interface", fill='white', anchor='mm')
    img2.save('back5.jpg')
    
    # Login background
    img3 = Image.new('RGB', (1920, 1080), (40, 40, 80))
    draw3 = ImageDraw.Draw(img3)
    draw3.text((960, 540), "LOGIN", fill='white', anchor='mm')
    img3.save('1.jpg')
    
    # Registration background
    img4 = Image.new('RGB', (600, 800), (60, 60, 120))
    draw4 = ImageDraw.Draw(img4)
    draw4.text((300, 400), "REGISTER", fill='white', anchor='mm')
    img4.save('register.jpg')
    
    print("Background images created successfully!")

class MockModel:
    def predict(self, X):
        # Random prediction for demo purposes
        return np.random.rand(1, 2)

def create_mock_model():
    """Create a mock model for testing"""
    
    model = MockModel()
    with open('abnormalevent.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("Mock model created successfully!")

if __name__ == "__main__":
    create_background_images()
    create_mock_model()