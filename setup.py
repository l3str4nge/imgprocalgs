import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="imgprocalgs",
    version="0.1",
    author="mateuszz0000",
    author_email="mtszzwdzk@gmail.com",
    description="Collection of common image processing algorithms.",
    long_description="Collection of common image processing algorithms.",
    long_description_content_type="text/markdown",
    url="https://github.com/mateuszz0000/imgprocalgs",
    install_requires=required,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'imgprocalgs-sepia=imgprocalgs.algorithms.tone:main',
            'imgprocalgs-tiltshift=imgprocalgs.algorithms.tilt_shift:main',
        ],
    }
)
