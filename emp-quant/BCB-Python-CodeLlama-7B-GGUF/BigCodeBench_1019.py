
from PIL import Image
import codecs
import pytesseract

IMAGE_PATH = "image.png"

def task_func(filename=IMAGE_PATH, from_encoding="cp1251", to_encoding="utf8"):
    try:
        # Open the image file
        image = Image.open(filename)

        # Extract text using OCR
        text = pytesseract.image_to_string(image)

        # Convert text encoding
        text = text.encode(from_encoding).decode(to_encoding)

        # Extract image comment
        comment = image.info.get("comment", "")

        # Convert image comment encoding
        comment = comment.encode(from_encoding).decode(to_encoding)

        # Return the converted text and comment
        return comment, text

    except (ValueError, LookupError):
        # Raise exception if incorrect encodings are provided
        raise ValueError("Incorrect encodings provided")

    except (pytesseract.TesseractError, FileNotFoundError):
        # Raise exception if OCR extraction or comment processing fails
        raise ValueError("OCR extraction or comment processing failed")

    except Exception:
        # Raise exception if any other error occurs
        raise ValueError("Unknown error occurred")