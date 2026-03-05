
from PIL import Image
import codecs
import pytesseract

IMAGE_PATH = "image.png"

def task_func(filename=IMAGE_PATH, from_encoding="cp1251", to_encoding="utf8"):
    try:
        # Open the image file
        image = Image.open(filename)

        # Extract text from the image using OCR
        text = pytesseract.image_to_string(image, lang="eng")

        # Convert the text to the target encoding
        converted_text = codecs.decode(text, from_encoding, to_encoding)

        # Return the converted text
        return converted_text
    except (ValueError, LookupError) as e:
        # Raise the exception
        raise e
    except:
        # Return an empty string if OCR extraction and comment processing both fail
        return ""