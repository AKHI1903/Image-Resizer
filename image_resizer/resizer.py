import os
from PIL import Image

# Input and output folders
input_folder = "images"
output_folder = "output"

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resize settings
new_size = (400, 400)  # width x height

# Process all files in the input folder
for filename in os.listdir(input_folder):
    try:
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Resize
            img_resized = img.resize(new_size)

            # Save as PNG (you can change format if needed)
            save_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
            img_resized.save(save_path)

            print(f"✅ {filename} resized and saved as {save_path}")
    except Exception as e:
        print(f"⚠️ Could not process {filename}: {e}")