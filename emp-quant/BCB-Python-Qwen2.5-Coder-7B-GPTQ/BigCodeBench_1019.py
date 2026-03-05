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
            # Convert text encoding
            try:
                converted_text = text.encode(from_encoding).decode(to_encoding)
                return converted_text
            except (UnicodeDecodeError, LookupError):
                raise ValueError("Encoding conversion failed")
    except Exception as e:
        # Handle exceptions from OCR extraction
        print(f"OCR extraction failed: {e}")

    try:
        # Attempt to read image comment
        with open(filename, 'rb') as f:
            f.seek(24)  # Skip the header
            comment = f.read()
            if comment:
                # Convert comment encoding
                try:
                    converted_comment = comment.decode(from_encoding).encode(to_encoding).decode(to_encoding)
                    return converted_comment
                except (UnicodeDecodeError, LookupError):
                    raise ValueError("Encoding conversion failed")
    except Exception as e:
        # Handle exceptions from reading image comment
        print(f"Reading image comment failed: {e}")

    # Return empty string if both OCR extraction and comment processing fail
    return ""