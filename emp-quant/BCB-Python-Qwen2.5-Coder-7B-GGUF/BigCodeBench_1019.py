
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
            return text.encode(from_encoding).decode(to_encoding)
    
    except Exception as e:
        print(f"OCR extraction failed: {e}")
    
    try:
        # Attempt comment processing
        with open(filename, 'rb') as f:
            image_data = f.read()
            comment = image_data[image_data.find(b'\x89PNG\r\n\x1a\n') + 8:image_data.find(b'\x00IEND\xaeB`\x82')]
            if comment:
                return comment.decode(from_encoding, errors='ignore').encode(to_encoding, errors='ignore').decode(to_encoding)
    
    except Exception as e:
        print(f"Comment processing failed: {e}")
    
    return ""