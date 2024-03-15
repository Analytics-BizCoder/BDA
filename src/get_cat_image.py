import requests
import os
import subprocess

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
            print(f"Cat image URL: {cat_image_url}")
            return cat_image_url
            
    # Set the cat image URL as an output parame

cat_image_url= fetch_cat_image_with_api_key()

print(f"::set-output name=cat_image_url::{cat_image_url}")
