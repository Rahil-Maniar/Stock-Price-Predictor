# for collecting testing data
import os
from PIL import Image, ImageOps
import numpy as np

# Define the paths
image_dir = 'C:/Users/Rahil Maniar/Desktop/Stock Market Predictor/TestImages'  # Directory containing the original images
left_dir = 'C:/Users/Rahil Maniar/Desktop/Stock Market Predictor/TestImagesLeft'  # Directory to save left halves
right_dir = 'C:/Users/Rahil Maniar/Desktop/Stock Market Predictor/TestImagesRight'  # Directory to save right halves

# Create directories if they do not exist
os.makedirs(left_dir, exist_ok=True)
os.makedirs(right_dir, exist_ok=True)

# Fixed dimensions for resizing (e.g., height=256, width=512)
fixed_height = 256
fixed_width = 512

# Function to load, resize, split, and save images
def split_and_save_images(image_dir, left_dir, right_dir):
    for filename in os.listdir(image_dir):
        if filename.endswith('.png'):
            image_path = os.path.join(image_dir, filename)
            image = Image.open(image_path)
            image_resized = image.resize((fixed_width, fixed_height))  # Resize image
            image_gray = ImageOps.grayscale(image_resized)
            image_array = np.array(image_gray)

            height, width = image_array.shape
            left_half = image_array[:, :width // 2]
            right_half = image_array[:, width // 2:]

            # Convert numpy arrays back to images
            left_image = Image.fromarray(left_half)
            right_image = Image.fromarray(right_half)

            # Save the images
            left_image.save(os.path.join(left_dir, filename))
            right_image.save(os.path.join(right_dir, filename))

# Run the function
split_and_save_images(image_dir, left_dir, right_dir)