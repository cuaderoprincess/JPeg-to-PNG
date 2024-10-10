import os
from PIL import Image

def convert_jpeg_to_png(input_path, output_path):
    try:
        # Open the JPEG image
        with Image.open(input_path) as img:
            # Convert and save as PNG
            img.save(output_path, 'PNG')
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {str(e)}")

def main():
    input_folder = "input_jpegs"
    output_folder = "output_pngs"

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
            convert_jpeg_to_png(input_path, output_path)

if __name__ == "__main__":
    main()
