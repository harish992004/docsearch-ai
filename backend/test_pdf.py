from app.services.pdf_service import PDFService

images = PDFService.convert_pdf_to_images(
    "uploads/2026-EROLLGEN-S22-26-SIR-FinalRoll-Revision1-ENG-7-WI.pdf",
    "outputs/images"
)

print(images)