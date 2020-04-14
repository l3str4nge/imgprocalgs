from imgprocalgs.utilities import Image, create_empty_image

OUTPUT_FILENAME = "negative.jpg"


def make_negative(image_path: str):
    image = Image(image_path)
    width, height = image.get_size()
    output = create_empty_image(width, height)
    output_pixels = output.load()
    for x in range(width):
        for y in range(height):
            red, green, blue = image.pixels[x, y]
            output_pixels[x, y] = (255 - red, 255 - green, 255 - blue)

    output.save(OUTPUT_FILENAME)



