# 👗 AI-Based Fashion Recommender

Upload a photo of your outfit and get smart fashion suggestions powered by AI!  
This is a lightweight REST API using FastAPI and Hugging Face's CLIP model to analyze outfit styles and return improvement ideas.

---

## 🚀 Features

- Upload outfit images (`/upload`)
- Get AI-generated style suggestions using CLIP
- Simple REST interface (cURL/Postman/Swagger)
- Auto reload during dev (`--reload`)
- Extensible for Pinterest integration, user preferences, and more

---

## 📦 Requirements

- Python 3.8+
- pip (Python package manager)

Install dependencies:

```pip install -r requirements.txt```

## 🧠 Model Used

```🤖 openai/clip-vit-base-patch32```

CLIP compares your image to a set of descriptive fashion prompts and ranks the most relevant styles.

---

## 🛠 How to Run

🌐 Start the server

```uvicorn app.main:app --reload```

---

## Test the API

Visit ```http://127.0.0.1:8000/docs``` for Swagger UI