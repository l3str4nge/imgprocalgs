import argparse

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from imgprocalgs import application


def parse_args():
    parser = argparse.ArgumentParser(description='Image Processing Algorithms')
    parser.add_argument("--src", type=str, help="Source file path.")
    parser.add_argument("--dest", type=str, help="Destination file path.", default='data/')
    parser.add_argument("--names", type=str, help="Algorithm names list to execute, comma separated.")
    parser.add_argument("--visualize", type=bool, help="Open visualization in webbrowser", default=False)
    return parser.parse_args()


if __name__ == '__main__':
    application.run(parse_args())
