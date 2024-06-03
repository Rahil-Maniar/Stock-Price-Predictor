import pyautogui
import time
import pyperclip
import cv2
import numpy as np
from datetime import datetime

# Function to take a screenshot of a specific region or the whole screen
def take_screenshot(search_text, region=None):
    if region:
        # Take a screenshot of the specified region
        screenshot = pyautogui.screenshot(region=region)
    else:
        # Take a screenshot of the whole screen
        screenshot = pyautogui.screenshot()

    # Save the screenshot with a timestamp to ensure unique filenames
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot.save(f'C:/Users/Rahil Maniar/Desktop/Stock Market Predictor/Images/{search_text}.png')   # Replace with your desired path, training: /Images , testing: /TestImages

    print(f'Screenshot taken and saved as {search_text}.png')

# Function to locate and click the "6M" button
def locate_and_click_6m_button(image_path):
    # Load the image of the "6M" button
    button_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if button_image is None:
        print("Button image not found. Please check the path.")
        return False
    
    # Take a screenshot of the screen
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
    
    # Find the button on the screen
    result = cv2.matchTemplate(screen, button_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Set a threshold for matching
    threshold = 0.8
    if max_val >= threshold:
        # Calculate the position to click
        button_height, button_width = button_image.shape
        click_position = (max_loc[0] + button_width // 2, max_loc[1] + button_height // 2)
        
        # Click the "6M" button
        pyautogui.click(click_position)
        print(f'Clicked on the "6M" button at position: {click_position}')
        return True
    else:
        print('6M button not found on the screen.')
        return False

# Function to search text in Chrome, locate the "6M" button, click it, and take a screenshot
def search_and_screenshot(search_text, region, search_bar_coords, button_image_path):
    # Click on the search bar, clear it, and type the search text
    pyautogui.click(search_bar_coords)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyperclip.copy(search_text)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    # Wait for the search results to load
    time.sleep(2)

    # Locate and click the "6M" button
    if locate_and_click_6m_button(button_image_path):
        # Wait for a second after clicking the "6M" button
        time.sleep(1)
        
        # Take a screenshot of the specified region only if the button was found
        take_screenshot(search_text, region)
    else:
        # Take a screenshot of the whole screen if the button was not found
        take_screenshot(search_text)

# Main function to process the text file
def process_text_file(file_path, region, search_bar_coords, button_image_path):
    with open(file_path, 'r') as file:
        for line in file:
            search_text = line.strip() + " share price"
            if search_text:
                search_and_screenshot(search_text, region, search_bar_coords, button_image_path)

# Parameters for the region (x, y, width, height)
# Example: (left, top, width, height)
region = (238, 687, 825, 250)  # Adjust these values as needed

# Coordinates for the search bar
search_bar_coords = (865, 90)  # Adjust these values based on your screen resolution and browser layout

# Path to the text file
file_path = 'C:/Users/Rahil Maniar/Desktop/Stock Market Predictor/shares.txt'  # Replace with your text file path

# Path to the image of the "6M" button
button_image_path = 'C:/Users/Rahil Maniar/Desktop/Stock Market Predictor/6M_button.png'  # Path to the uploaded "6M" button image, you can use any button image

# Process the text file and perform the search, click, and screenshot sequence
process_text_file(file_path, region, search_bar_coords, button_image_path)
