
import time
import sys
import pytesseract
from PIL import Image
import mss

# Optional: Set the path to tesseract if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(left, top, right, bottom, delay):
    if delay > 0:
        print(f"Waiting {delay} seconds before capture...")
        time.sleep(delay)

    width = right - left
    height = bottom - top

    with mss.mss() as sct:
        monitor = {"left": left, "top": top, "width": width, "height": height}
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        text = pytesseract.image_to_string(img)
        return text.strip()

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python screen_ocr.py x1 y1 x2 y2 delay_seconds")
        sys.exit(1)

    try:
        x1 = int(sys.argv[1])
        y1 = int(sys.argv[2])
        x2 = int(sys.argv[3])
        y2 = int(sys.argv[4])
        delay = float(sys.argv[5])
        result = extract_text(x1, y1, x2, y2, delay)
        print(result)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
