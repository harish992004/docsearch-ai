from app.services.ocr_service import OCRService

print("Creating OCR Service...")

ocr = OCRService()

print("Reading Image...")

result = ocr.extract_text("outputs/images/page_1.png")

print("\n================ OCR RESULT ================\n")
print(result)
print("\n===========================================\n")