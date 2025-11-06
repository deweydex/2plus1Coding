"""
IMAGE PROCESSING - Beginner Starter Code
=========================================

This starter code provides the foundation for working with digital images.
It loads an image and displays it, so you can see visual output immediately.

BEFORE RUNNING: Install the required library:
    pip install pillow

YOUR TASKS:
1. Add a function to convert the image to grayscale
2. Create a brightness adjustment function
3. Add a simple filter (blur, sharpen, edge detection)
4. Let the user save the modified image
5. Add more filters and effects based on your interests

RUN THIS FILE FIRST to see what you're starting with:
    python imageproc_beginner.py

Then work with Claude Code to build image processing functions step by step.

NOTE: You'll need a sample image file. The code will try to download one
automatically, or you can place your own image.jpg in the same folder.
"""

from PIL import Image, ImageFilter
import urllib.request
import os


def load_image(filename="image.jpg"):
    """
    Loads an image from a file.

    If the file doesn't exist, downloads a sample image.

    Parameters:
        filename (str): Path to the image file

    Returns:
        Image: A PIL Image object
    """
    if not os.path.exists(filename):
        print(f"Image not found. Downloading a sample image...")
        url = "https://picsum.photos/400/300"
        try:
            urllib.request.urlretrieve(url, filename)
            print(f"Sample image saved as {filename}")
        except Exception as e:
            print(f"Could not download image: {e}")
            print("Please place an 'image.jpg' file in this directory.")
            return None

    try:
        img = Image.open(filename)
        print(f"Image loaded successfully!")
        print(f"Size: {img.width} x {img.height} pixels")
        print(f"Mode: {img.mode}")
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


def display_image(img):
    """
    Displays an image in the default image viewer.

    Parameters:
        img (Image): The image to display
    """
    if img:
        img.show()
    else:
        print("No image to display.")


def save_image(img, filename):
    """
    Saves an image to a file.

    Parameters:
        img (Image): The image to save
        filename (str): Path where the image should be saved
    """
    try:
        img.save(filename)
        print(f"Image saved as {filename}")
    except Exception as e:
        print(f"Error saving image: {e}")


def main():
    """
    Main function demonstrating basic image loading and display.

    You'll expand this to include filters and transformations.
    """
    print("=" * 50)
    print("  WELCOME TO IMAGE PROCESSING!")
    print("=" * 50)
    print("\nThis starter code loads and displays an image.")
    print("Your task is to add processing functions.\n")

    # Load an image
    img = load_image("image.jpg")

    if img:
        # Display the original image
        print("\nDisplaying the original image...")
        display_image(img)

        print("\n" + "=" * 50)
        print("This is your starting point!")
        print("Next step: Add a function to convert the image to grayscale.")
        print("=" * 50)
    else:
        print("\nCouldn't load an image. Please check the file exists.")


if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, try these prompts one at a time:

1. "Add a function called convert_to_grayscale that takes an image and
   returns a grayscale version using the convert method."

2. "Create a function called adjust_brightness that takes an image and a
   brightness factor (0.5 = darker, 2.0 = brighter) and returns the
   adjusted image using ImageEnhance."

3. "Add a function that applies the BLUR filter to an image and returns
   the blurred result."

4. "Create a menu system in main() that lets the user choose which effect
   to apply to the image, then saves the result with a descriptive name."

5. "Add more filters: sharpen, edge detection (FIND_EDGES), emboss, contour."

6. "Create a function that creates a photo collage by resizing multiple
   images and arranging them in a grid."

Remember: Test after each change! View the processed images to see the effects.
"""
