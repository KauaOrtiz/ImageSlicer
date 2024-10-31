from PIL import Image
import os

def slice_sprites(image_path, num_slices):
    sprite_sheet = Image.open(image_path)
    slice_width = 32
    slice_height = 32
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_folder = f"{base_name}_slices"
    os.makedirs(output_folder, exist_ok=True)
    slices = []
    
    for i in range(num_slices):
        left = i * slice_width
        upper = 0
        right = left + slice_width
        lower = slice_height
        slice_image = sprite_sheet.crop((left, upper, right, lower))
        slices.append(slice_image)
        output_path = os.path.join(output_folder, f"{base_name}_slice_{i+1}.png")
        slice_image.save(output_path)
    return slices

slices = slice_sprites("yourImageHere.png", num_slices=8)
# for i, slice_image in enumerate(slices):
#     slice_image.show()
