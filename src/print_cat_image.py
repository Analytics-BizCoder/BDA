import os

def print_cat_image_from_url(image_url):
    # Download the cat image file
    os.system(f"wget {image_url} -O cat_image.jpg")

    # Convert the image to ASCII art and print in the terminal
    os.system("jp2a cat_image.jpg --width=80")

# Example usage:
cat_image_url = os.getenv("CAT_IMAGE_URL")

if cat_image_url:
    print_cat_image_from_url(cat_image_url)
else:
    print("Error: CAT_IMAGE_URL environment variable is not set.")
