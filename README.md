<p align="center">
    <h1>ImageProcessingAlgorithms</h1>
</p>
<p align="center">
    <a href="https://travis-ci.com/github/mateuszz0000/imgprocalgs">
        <img src="https://travis-ci.com/mateuszz0000/imgprocalgs.svg?branch=master">
    </a>
    <a href="https://codecov.io/gh/mateuszz0000/imgprocalgs">
        <img src="https://img.shields.io/codecov/c/github/mateuszz0000/imgprocalgs">
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg">
    </a>
</p>



Collection of common image processing algorithms. This project aims to learn digital image processing algorithms by coding them from scratch in Python >= 3.6. 
Small Flask application is used to generate output in website to see algorithm result.

Travis-CI is used for CI/CD environment.

Implemented so far:
* resizing algorithms:
    * Nearest neighbour (https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm)
    * Bilinear interpolation (https://en.wikipedia.org/wiki/Bilinear_interpolation)
    * Bicubic interpolation (https://en.wikipedia.org/wiki/Bicubic_interpolation)
* other:
    * negative (https://en.wikipedia.org/wiki/Negative_(photography))
    * Tilt-shift (https://pl.wikipedia.org/wiki/Tilt-shift)
    * RGB to HSV conversion(https://en.wikipedia.org/wiki/HSL_and_HSV)
    * HSV to RGB conversion(https://en.wikipedia.org/wiki/HSL_and_HSV)
    * color accent
* tone
    * sepia (https://en.wikipedia.org/wiki/Photographic_print_toning#Sepia_toning)
* dithering
    * Floyd-Steinberg (https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering)
    * Jarvis Judice Ninke (https://en.wikipedia.org/wiki/Dither)
    * Stucki (https://en.wikipedia.org/wiki/Dither)
* Convolution
    * Edge detection (https://en.wikipedia.org/wiki/Kernel_(image_processing))

##### Installation
```buildoutcfg
git clone https://github.com/mateuszz0000/imgprocalgs
pip install -U imgprocalgs/
```

##### Usage
A different entry point is prepared for each type of algorithm:
```buildoutcfg
imgprocalgs-sepia <OPTIONS>
imgprocalgs-tiltshift <OPTIONS>
imgprocalgs-dithering <OPTIONS>
imgprocalgs-negative <OPTIONS>
imgprocalgs-color-accent <OPTIONS>
```

#### Contribution
Read our [Contribution Guidelines](CONTRIBUTING.md) before you contribute.
