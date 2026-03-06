
from PIL import Image
import codecs
import pytesseract

IMAGE_PATH = "image.png"

def task_func(filename=IMAGE_PATH, from_encoding="cp1251", to_encoding="utf8"):
    # Open the image file
    image = Image.open(filename)

    # Extract text from the image using OCR
    text = pytesseract.image_to_string(image)

    # Convert the text to the target encoding
    try:
        text = text.encode(to_encoding)
    except (UnicodeDecodeError, LookupError):
        # If the conversion fails, try to extract text from the image comment
        comment = image.info.get("comment")
        if comment:
            try:
                comment = comment.encode(to_encoding)
            except (UnicodeDecodeError, LookupError):
                # If the conversion fails again, return an empty string
                return ""
        else:
            # If there is no comment, return an empty string
            return ""

    # Return the converted text
    return comment