
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
            return convert_text(text, from_encoding, to_encoding)
    
    except Exception as e:
        print(f"OCR error: {e}")
    
    try:
        # Fallback to image comment processing
        image = Image.open(filename)
        comment = image.info.get('comment', '')
        
        if comment:
            return convert_text(comment, from_encoding, to_encoding)
    
    except Exception as e:
        print(f"Comment processing error: {e}")
    
    return ""

def convert_text(text, from_encoding, to_encoding):
    try:
        decoded_text = text.encode(from_encoding).decode(to_encoding)
        return decoded_text
    
    except (UnicodeDecodeError, LookupError) as e:
        raise ValueError(f"Encoding error: {e}")