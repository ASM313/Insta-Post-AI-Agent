from PIL import Image, ImageDraw, ImageFont
import textwrap

# Function to create an image with the quote
def create_image_with_quote(input_text_file, output_image_file, image_size=(1080, 1920), font_size=60):
    # Read the quote from the text file
    with open(input_text_file, 'r', encoding='utf-8') as file:
        quote = file.read()

    # Create a blank image with white background
    image = Image.new('RGB', image_size, color='white')
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Change to a path of a .ttf font if necessary
    except IOError:
        font = ImageFont.load_default()  # Use default font if specified font is unavailable

    # Word wrapping to fit the text within the image
    margin = 40
    max_width = image_size[0] - 2 * margin
    wrapped_text = textwrap.fill(quote, width=40)  # Adjust width for wrapping

    # Calculate the bounding box of the wrapped text
    text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    text_x = margin
    text_y = (image_size[1] - text_height) // 2  # Center the text vertically

    # Add the text to the image
    draw.text((text_x, text_y), wrapped_text, fill="black", font=font)

    # Save the image to a file
    image.save(output_image_file)

