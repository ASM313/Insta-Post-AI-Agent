from utils import create_image_with_quote



# Usage
input_text_file = 'Research/new-blog-post.txt'  # Path to the text file containing the quote
output_image_file = 'quote_image.png'  # Path to save the generated image

create_image_with_quote(input_text_file, output_image_file)

print(f"Image created and saved as {output_image_file}")
