
from PIL import Image
import codecs
import pytesseract

IMAGE_PATH = "image.png"

def task_func(filename=IMAGE_PATH, from_encoding="cp1251", to_encoding="utf8"):
    try:
        # Attempt OCR extraction
        text = pytesseract.image_to_string(Image.open(filename))
        if text:
            # Convert text to target encoding
            try:
                text = text.encode(from_encoding).decode(to_encoding)
                return text
            except (UnicodeDecodeError, LookupError):
                raise ValueError("Incorrect encoding provided for text conversion")
    except Exception as e:
        # Handle OCR errors
        print(f"OCR error: {e}")

    # Fallback to image comment processing
    try:
        # Open the image and get the comment
        with Image.open(filename) as img:
            comment = img.info.get('comment', '')
            if comment:
                # Convert comment to target encoding
                try:
                    comment = comment.encode(from_encoding).decode(to_encoding)
                    return comment
                except (UnicodeDecodeError, LookupError):
                    raise ValueError("Incorrect encoding provided for comment conversion")
    except Exception as e:
        # Handle image comment errors
        print(f"Image comment error: {e}")

    # Return an empty string if both OCR and comment processing fail
    return ""