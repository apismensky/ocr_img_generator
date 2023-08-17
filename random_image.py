import os
import random
from PIL import Image, ImageDraw, ImageFont

# Image dimensions
width, height = 1000, 1000

# Specify your fonts folder
fonts = os.listdir("/Library/Fonts/Managed")

# Specify your font size range
min_font, max_font = 23, 27

# don't go crazy with this one, especially with smaller fonts it may make everything unreadable.
max_noice_intensity = 10

# Specify your output directory
image_path = "random_images"


def generate_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Current teseeract version does not support text rotation with arbitrary angles, only 90 degree increments.
def generate_random_text_angle():
    return random.randint(0, 3) * 90


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


# noise generation function - takes a random number between -intensity and +intensity and adds it to each pixel.
# This will make the text less readable, but it will also make it harder for tesseract to recognize it.
def generate_random_noise(image, intensity=max_noice_intensity):
    w, h = image.size
    pixels = image.load()
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            noise = random.randint(-intensity, intensity)
            pixels[x, y] = (
                max(0, min(255, r + noise)),
                max(0, min(255, g + noise)),
                max(0, min(255, b + noise))
            )


# This function generates a random image with the specified text and saves it to the specified path.
# It uses the PIL library to generate the image.
def generate_random_image(text, output_path):
    background_color = generate_random_color()
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font_path = random.choice(fonts)
    font_size = random.randint(min_font, max_font)
    font_color = generate_random_color()
    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text(
        (x, y),
        text,
        font=font,
        fill=font_color,
    )
    image = image.rotate(generate_random_text_angle(), expand=1)
    generate_random_noise(image)
    image.save(output_path)


if __name__ == "__main__":
    # Read some text from a file
    lorem = read_file("lorem.txt")
    # Create the output directory if it does not exist
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    # Generate 10 random images
    for i in range(0, 10):
        output_image_path = os.path.join(image_path, f'image_{i}.png')
        generate_random_image(lorem, output_image_path)
