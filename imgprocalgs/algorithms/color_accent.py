from imgprocalgs.algorithms import utilities


def accent_color(input_path: str, output_path: str, h: float, _range: int):
    def h1_lt_h2(_h, _h1, _h2):
        return _h1 < _h < _h2

    def h1_gt_h2(_h, _h1, _h2):
        return _h <= _h1 or _h >= _h2

    h1 = (h - (_range / 2) + 360) % 360
    h2 = (h + (_range / 2) + 360) % 360
    func = h1_lt_h2 if h1 <= h2 else h1_gt_h2

    input_image = utilities.Image(input_path)
    width, height = input_image.get_size()
    output_image = utilities.create_empty_image(width, height)
    output_pixels = output_image.load()
    for x in range(width):
        for y in range(height):
            hsv = utilities.rgb_to_hsv(*input_image.pixels[x, y])

            if func(hsv.h, h1, h2):
                output_pixels[x, y] = input_image.pixels[x, y]
            else:
                greyscale_value = int(utilities.get_greyscale(*input_image.pixels[x, y]))
                output_pixels[x, y] = (greyscale_value, greyscale_value, greyscale_value)

    output_image.save(output_path)
