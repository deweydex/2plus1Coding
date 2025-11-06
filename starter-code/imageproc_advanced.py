"""
IMAGE PROCESSING - Advanced Starter Code
=========================================

This starter code provides image loading, basic transformations, and
a filter application framework. Your focus will be on implementing
interesting effects and creating a user-friendly interface.

BEFORE RUNNING: Install the required library:
    pip install pillow

RUN THIS FILE FIRST to see what you're starting with:
    python imageproc_advanced.py

The program demonstrates basic image operations.

YOUR TASKS:
1. Implement multiple image filters and effects
2. Create a menu-driven interface for applying transformations
3. Add batch processing for multiple images
4. Implement advanced effects (sepia, vignette, pixelation)
5. Create before/after comparison views
"""

from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import urllib.request
import os


def load_image(filename="image.jpg"):
    """
    Loads an image from a file, downloading a sample if needed.

    Parameters:
        filename (str): Path to the image file

    Returns:
        Image: A PIL Image object, or None if loading fails
    """
    if not os.path.exists(filename):
        print(f"Downloading sample image...")
        url = "https://picsum.photos/500/400"
        try:
            urllib.request.urlretrieve(url, filename)
            print(f"Sample image saved as {filename}")
        except Exception as e:
            print(f"Could not download: {e}")
            return None

    try:
        img = Image.open(filename)
        print(f"Loaded: {img.width}x{img.height} {img.mode}")
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


def convert_to_grayscale(img):
    """
    Converts an image to grayscale.

    Parameters:
        img (Image): The image to convert

    Returns:
        Image: Grayscale version of the image
    """
    return img.convert('L')


def adjust_brightness(img, factor):
    """
    Adjusts image brightness.

    Parameters:
        img (Image): The image to adjust
        factor (float): Brightness factor (0.5=darker, 1.0=normal, 2.0=brighter)

    Returns:
        Image: Brightness-adjusted image
    """
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)


def apply_filter(img, filter_type):
    """
    Applies a built-in PIL filter to an image.

    Parameters:
        img (Image): The image to filter
        filter_type (ImageFilter): The filter to apply

    Returns:
        Image: Filtered image
    """
    return img.filter(filter_type)


def resize_image(img, width, height):
    """
    Resizes an image to specific dimensions.

    Parameters:
        img (Image): The image to resize
        width (int): New width in pixels
        height (int): New height in pixels

    Returns:
        Image: Resized image
    """
    return img.resize((width, height), Image.Resampling.LANCZOS)


def save_image(img, filename):
    """
    Saves an image to a file.

    Parameters:
        img (Image): The image to save
        filename (str): Output filename
    """
    try:
        img.save(filename)
        print(f"Saved: {filename}")
    except Exception as e:
        print(f"Error saving: {e}")


def main():
    """
    Main function demonstrating basic image operations.

    You'll expand this into a full-featured image processing program
    with multiple effects and a user-friendly interface.
    """
    print("=" * 50)
    print("  IMAGE PROCESSING - Advanced Starter")
    print("=" * 50)

    # Load image
    img = load_image("image.jpg")
    if not img:
        print("Cannot proceed without an image.")
        return

    # Demonstrate different operations
    print("\n--- Demonstrating Image Operations ---\n")

    # 1. Grayscale
    print("1. Creating grayscale version...")
    gray_img = convert_to_grayscale(img)
    save_image(gray_img, "output_grayscale.jpg")

    # 2. Brightness adjustment
    print("2. Adjusting brightness...")
    bright_img = adjust_brightness(img, 1.5)
    save_image(bright_img, "output_bright.jpg")

    # 3. Apply blur filter
    print("3. Applying blur filter...")
    blurred = apply_filter(img, ImageFilter.BLUR)
    save_image(blurred, "output_blurred.jpg")

    # 4. Resize
    print("4. Resizing image...")
    small = resize_image(img, 200, 150)
    save_image(small, "output_small.jpg")

    print("\n" + "=" * 50)
    print("Demo complete! Check the output files.")
    print("\nNow build your full image processor:")
    print("  - Create an interactive menu system")
    print("  - Add more effects (sepia, vignette, etc.)")
    print("  - Implement effect combinations")
    print("  - Add batch processing for multiple images")
    print("  - Create before/after comparison views")
    print("=" * 50)


if __name__ == "__main__":
    main()


"""
SUGGESTED PROMPTS FOR CLAUDE CODE:
===================================

After running this starter code, work on these features:

1. "Create a function called create_sepia_tone that converts an image to
   a warm, brownish tone (sepia effect) by manipulating RGB channels."

2. "Add a function for contrast adjustment using ImageEnhance.Contrast,
   similar to how brightness adjustment works."

3. "Create a pixelate effect by shrinking the image then enlarging it back
   without interpolation."

4. "Build an interactive menu system that displays available effects,
   gets user choice, applies the effect, and asks if they want to apply
   more effects or save and exit."

5. "Add a function that creates a side-by-side comparison image showing
   the original and processed version using Image.new and paste."

6. "Implement batch processing that applies the same effect to all images
   in a folder."

7. For enhancements, consider:
   - Edge detection and enhancement
   - Color channel manipulation (adjust red/green/blue separately)
   - Image rotation and flipping
   - Cropping and aspect ratio changes
   - Adding borders or watermarks
   - Creating thumbnails
   - Combining multiple images (collages, blending)
   - Histogram equalization for contrast
   - Custom convolution filters

Remember to test with different types of images (photos, graphics, etc.)!
"""
