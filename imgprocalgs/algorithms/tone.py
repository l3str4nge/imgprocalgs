from imgprocalgs.utilities import Image, create_empty_image

OUTPUT_FILENAME = "sepia.jpg"


def make_sepia(image_path: str, factor: int):
    image = Image(image_path)
    width, height = image.get_size()
    output = create_empty_image(width, height)
    output_pixels = output.load()
    for x in range(width):
        for y in range(height):
            red, green, blue = image.pixels[x, y]
            grey_red = int(get_greyscale(red, green, blue))
            grey_green = int(get_greyscale(red, green, blue))
            grey_blue = int(get_greyscale(red, green, blue))

            output_pixels[x, y] = (grey_red + 2 * factor, grey_green + factor, grey_blue)

    output.save(OUTPUT_FILENAME)


def get_greyscale(red, green, blue):
    return 0.2126 * red + 0.587 * green + 0.114 * blue