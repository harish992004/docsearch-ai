from paddleocr import PaddleOCR


class OCRService:
    def __init__(self):
        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang="en"
        )

    def extract_text(self, image_path):
        print(f"Reading image: {image_path}")

        result = self.ocr.ocr(image_path, cls=True)

        print("OCR Finished!")
        return result