# 📄 DocSearch AI

> AI-powered document intelligence platform for scanned PDFs.

DocSearch AI is an end-to-end backend system that converts scanned PDF documents into searchable structured data using OCR and AI.

The project begins with electoral roll PDFs but is designed to support any scanned document such as:

- Electoral Rolls
- Government Records
- Research Papers
- Invoices
- Land Records
- Books

---

## ✨ Features

- Upload scanned PDFs
- Convert PDF pages into images
- OCR text extraction (Coming Soon)
- Structured data extraction (Coming Soon)
- Fast document search (Coming Soon)
- AI-powered document assistant (Coming Soon)

---

## 🏗 Architecture

```
PDF Upload
     │
     ▼
FastAPI Backend
     │
     ▼
PDF Processing
     │
     ▼
Image Generation
     │
     ▼
OCR Engine
     │
     ▼
Structured Data
     │
     ▼
Database
     │
     ▼
Search Engine
     │
     ▼
AI Assistant
```

---

## 🛠 Tech Stack

### Backend

- FastAPI
- Python 3.10+

### AI / OCR

- PyMuPDF *(planned)*
- PaddleOCR *(planned)*
- OpenCV *(planned)*

### Database

- PostgreSQL *(planned)*

### Frontend

- React *(planned)*

---

## 📁 Project Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── services/
│   └── utils/
│
├── uploads/
├── outputs/
├── tests/
└── main.py
```

---

## 🚀 Current Progress

- [x] Git & GitHub Setup
- [x] FastAPI Backend
- [x] Swagger Documentation
- [x] PDF Upload API
- [ ] PDF → Images
- [ ] OCR
- [ ] Data Extraction
- [ ] Database
- [ ] Search Engine
- [ ] AI Assistant
- [ ] Docker Deployment

---

## 📦 Installation

```bash
git clone https://github.com/harish992004/docsearch-ai.git

cd docsearch-ai/backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🎯 Vision

Build an AI-powered platform capable of understanding scanned documents instead of simply extracting text.

---

## 📄 License

MIT License