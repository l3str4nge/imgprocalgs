from imgprocalgs.algorithms.utilities import Image, create_empty_image
from imgprocalgs.visualisation.server import App

OUTPUT_FILENAME = "sepia.jpg"


def make_sepia(image_path: str, dest_path: str, factor: int):
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

    output.save(dest_path)


def get_greyscale(red, green, blue):
    return 0.2126 * red + 0.587 * green + 0.114 * blue


if __name__ == "__main__":
    from collections import namedtuple
    img_data = namedtuple('ÍmgData', 'header image')
    make_sepia('tests/data/desert.jpg', 'data/desert_sepia.jpg', 30)
    data = {
        "title": "Sepia algorithm",
        "header": "Sepia with different factors",
        "image_data": [img_data("Factor: 30", "sepia.jpg")]
    }

    app = App()
    app.register_route("/", template_name="main_page.html", **data)
    app.run_server("127.0.0.1", 8001, open_webiste=True)
