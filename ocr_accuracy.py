import Levenshtein
import pytesseract
from PIL import Image


#  https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
def clean_text(text):
    if text is None:
        return ''
    return ' '.join(text.lower().strip().split())


def read_file(fp):
    with open(fp, "r") as f:
        return f.read()


true_text = clean_text(read_file("lorem.txt"))
true_text_len = len(true_text)


#  Levenshtein distance
#  https://en.wikipedia.org/wiki/Levenshtein_distance
def get_distance(sr, tt=true_text):
    return Levenshtein.distance(clean_text(sr), clean_text(tt))


#  Character Error Rate (CER) = Levenshtein distance / Total number of characters
def cer(dist, truth_len=true_text_len):
    if truth_len == 0:
        raise ValueError("truth_len should not be 0")
    return min((dist * 100 / truth_len), 100.0)


#  Accuracy = 100 - CER
def accuracy(actual, truth=true_text):
    dist = get_distance(actual, truth)
    return 100.0 - cer(dist, true_text_len)


#  OCR
#  https://nanonets.com/blog/ocr-with-tesseract/
def perform_ocr(image_path):
    try:
        # Open the image using PIL (Python Imaging Library)
        image = Image.open(image_path)

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image, config='--psm 1')

        return text
    except Exception as e:
        return str(e)


if __name__ == '__main__':

    for i in range(0, 10):
        file_path = f'random_images/image_{i}.png'
        scan_result = perform_ocr(file_path)
        distance = get_distance(scan_result)
        c = cer(distance)
        a = accuracy(scan_result)
        print(f'{file_path}, distance: {distance}, CER: {c}, accuracy: {a}, scan_result: {scan_result}')

