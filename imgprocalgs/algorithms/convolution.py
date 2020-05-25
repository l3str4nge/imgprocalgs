import numpy as np
from numpy import asarray
from PIL import Image
import argparse
from collections import namedtuple
from imgprocalgs.visualisation.server import App


ImageData = namedtuple("ImgData", 'header image')

 
def convolution(image, kernel): 
    image_row, image_col = image.shape  # getting image dimensions
    kernel_row, kernel_col = kernel.shape  # getting kernel dimensions
 
    output = np.zeros(image.shape)  # Intializing output array

    #  For convolution, we need to add a zero padding on all the four sides
 
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)
 
    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
 
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

    for row in range(image_row):
        for col in range(image_col):
            output[row, col] = np.sum(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])

    return output


def apply_convolution(image_path: str, dest_path: str, filter_kernel):
    kernel = filter_kernel
    input_image = Image.open(image_path)
    input_image = input_image.convert('1')      # Convert to black&white

    input_image = asarray(input_image)  # converting to numpy array for array manipulation
    input_array = convolution(input_image, kernel)

    output = Image.fromarray(input_array)
    output = output.convert('RGB')  # Convert to RGB
    output.save(dest_path)


filter_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])


def example(app: App):
    apply_convolution('tests/data/flower.jpg', 'data/flower_convoluted.jpg', filter_kernel)
    data = {
        'title': 'Convolution algorithm',
        'header': ' ',
        'image_data': [
            ImageData("Convoluted image", "flower_convoluted.jpg"),
        ]
    }
    app.register_route("/", template_name="main_page.html", **data)


def parse_args():
    parser = argparse.ArgumentParser(description='Convolution algorithms')
    parser.add_argument("--src", type=str, help="Source file path.")
    parser.add_argument("--dest", type=str, help="Destination file path.", default='data/')
    parser.add_argument("--factor", type=int, help="Sepia factor value")
    parser.add_argument("--example", type=bool, help="Show example", default=False)
    parser.add_argument("--visualize", type=bool, help="Open visualization in webbrowser", default=False)
    return parser.parse_args()


def main():
    args = parse_args()
    app = App()
    if args.example:
        example(app)
        app.run_server('127.0.0.1', 8000, open_webiste=args.visualize)
    else:
        apply_convolution(args.src, args.dest, filter_kernel)


if __name__ == "__main__":
    app = App()
    example(app)
    app.run_server("127.0.0.1", 8001, open_webiste=True)
