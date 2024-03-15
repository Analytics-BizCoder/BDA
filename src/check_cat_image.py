import sys
import cv2
import urllib.request
import numpy as np
import requests
import os

# Get API key from environment variable
api_key_cats = os.environ.get('CATS_API_KEY')

def fetch_cat_image_with_api_key():
    api_key = api_key_cats
    headers = {
        "x-api-key": api_key
    }
    response = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            cat_image_url = data[0]['url']
            return cat_image_url
# Fetch a cat image URL using the API
cat_image_url = fetch_cat_image_with_api_key()    

def check_for_cat(cat_image_url):
    # Load the cascade for detecting cats
    cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

    # Download the cat image from the URL
    try:
        req = urllib.request.urlopen(cat_image_url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        cat_image = cv2.imdecode(arr, -1)
    except Exception as e:
        print("Failed to download the cat image:", e)
        return False

    # Convert the image to grayscale
    gray = cv2.cvtColor(cat_image, cv2.COLOR_BGR2GRAY)

    # Detect cats in the image
    cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If cats are detected, return True
    if len(cats) > 0:
        return True
    else:
        return False

# Check if image contains a cat
if check_for_cat(cat_image_url):
    print("The image contains a cat!")
else:
    print("No cats found in the image.")
