# ocr_img_generator
Generate image with random font, colors, angle and noice with the text for OCR. 

Simple script to generate images with random fonts, colors, angle (0, 90, 180, 270) and noice with the text for OCR.
The text is always the same (in lorem.txt) so it is easy to check the OCR results (accuracy, CER etc)

## Requirements
``` bash
pip install -r requirements.txt
```

## Usage
You can specify the number of images (`for i in range(0, 10):`) to generate and the output directory, by default it will generate 10 images in the random_images directory.
``` bash
python ocr_img_generator.py 
```

## Example with tesseract
``` bash
python ocr_img_generator.py 
```
output (10 files generated):

```
random_images/image_1.png distance: 0, cer: 0.0, accuracy: 100.0, scan_result: Lorem ipsum dolor sit amet,

consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate

velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,

sunt in culpa qui officia deserunt mollit anim id est
```
    




