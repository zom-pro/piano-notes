import os
from PIL import Image


def list_pngs(images_path):
    """
    Lists the pngs in a particular location
    """
    pngs = [os.path.join(images_path, f) for f in os.listdir(images_path)
            if os.path.isfile(os.path.join(images_path, f)) and f.endswith(".png")]
    return pngs


def add_images_to_sheet(images_folder_path):
    """
    Grabs the list of pngs and adds them to an A4 sheet
    """
    # creates an a4 image 2480 pixels x 3508 pixels at 300 DPI
    background = Image.new('RGBA', (2480, 3508), (255, 255, 255, 255))

    number_of_cols = 7
    padding = 20

    horizontal_offset = padding
    vertical_offset = padding

    cols_counter = 0

    for png_path in list_pngs(images_folder_path):
        cols_counter += 1
        img = Image.open(png_path, 'r')
        img_width, img_height = img.size

        horizontal_offset = horizontal_offset + img_width + padding
        background.paste(img, (horizontal_offset, vertical_offset))

        if cols_counter % number_of_cols == 0:
            horizontal_offset = padding
            vertical_offset = vertical_offset + img_height + padding

    background.save(os.path.join(images_folder_path, 'out/out.png'))


if __name__ == "__main__":
    this_path = os.path.dirname(os.path.realpath(__file__))
    add_images_to_sheet(os.path.join(this_path, "notes"))