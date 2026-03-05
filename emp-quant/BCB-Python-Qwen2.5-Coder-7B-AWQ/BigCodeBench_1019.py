from PIL import Image
import codecs
import pytesseract
IMAGE_PATH = "image.png"
def task_func(filename=IMAGE_PATH, from_encoding="cp1251", to_encoding="utf8"):
    try:
        # Attempt OCR extraction
        image = Image.open(filename)
        text = pytesseract.image_to_string(image)
        if text:
            return convert_encoding(text, from_encoding, to_encoding)
        
        # If OCR fails, try image comment
        comment = image.info.get('comment', '')
        if comment:
            return convert_encoding(comment, from_encoding, to_encoding)
        
    except Exception as e:
        raise ValueError("Error during OCR or comment processing: " + str(e))
    
    return ""
def convert_encoding(text, from_encoding, to_encoding):
    try:
        return text.encode(from_encoding).decode(to_encoding)
    except (UnicodeDecodeError, LookupError) as e:
        raise ValueError("Error during encoding conversion: " + str(e))