# 🧠 Personalized Recommendation System

This project is a **lightweight, modular recommendation engine** that suggests products or courses based on user history and interests.
It uses **sentence embeddings**, **semantic similarity**, and **context-aware ranking** to deliver relevant recommendations.

---

## 🚀 Features

✅ Personalized product/course recommendations
✅ Context-aware ranking system using vector similarity
✅ Modular architecture (easily extendable to new data sources)
✅ Lightweight — works with small datasets for demo or testing
✅ API built with **FastAPI** for easy deployment and scalability
✅ Ready for local or cloud hosting (GitHub + local demo)

---

## 🧩 Tech Stack

| Category                   | Technology                                           |
| -------------------------- | ---------------------------------------------------- |
| **Backend Framework**      | FastAPI                                              |
| **Embedding Model**        | Hugging Face – Sentence Transformers                 |
| **Pipeline Orchestration** | LangChain & LangGraph                                |
| **Vector Similarity**      | Cosine Similarity (via `sentence-transformers.util`) |
| **Language**               | Python 3.10+                                         |

---

## 🏗️ Project Structure

```
sistema_recomendador_personalizado/
│
├── app/
│   ├── main.py                 # FastAPI entry point
│   ├── core/
│   │   └── config.py           # Application settings
│   ├── routers/
│   │   └── recommend.py        # API endpoints for recommendations
│   ├── services/
│   │   └── recommendation.py   # Core recommendation logic
│   └── utils/
│       └── embeddings.py       # Embedding generation and ranking functions
│
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation (this file)
```

---

## ⚙️ Installation

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/yourusername/personalized-recommendation-system.git
cd personalized-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API locally:

```bash
uvicorn app.main:app --reload
```

Access the API at:

```
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📚 API Endpoints

### **GET /**

Health check — returns API status.

**Response:**

```json
{
  "message": "API de Recomendação Personalizada Online"
}
```

---

### **GET /recommend/{user_id}**

Returns ranked product/course recommendations for the given user.

**Example:**

```
GET /recommend/1
```

**Response:**

```json
{
  "user_id": "1",
  "recommendations": [
    "Curso de Machine Learning prático",
    "Curso de Python avançado",
    "Curso de IA para iniciantes"
  ]
}
```

---

## 🧠 How It Works

1. **User Interest Embedding**

   * The system uses a pre-trained transformer model (`paraphrase-MiniLM-L6-v2`) to encode user interests into vector representations.

2. **Product Embedding**

   * Each available product/course is also encoded into the same vector space.

3. **Semantic Matching**

   * Cosine similarity measures how close user vectors are to product vectors.

4. **Ranking**

   * Products are ranked from most to least relevant and returned as recommendations.

---

## 🧩 Example Users & Data

```python
dummy_users = {
    "1": ["curso de python", "machine learning"],
    "2": ["marketing digital", "vendas online"]
}

dummy_products = [
    "Curso de IA para iniciantes",
    "Curso de Python avançado",
    "E-book de Vendas Online",
    "Curso de Machine Learning prático"
]
```

You can easily replace these with real datasets (e.g., CSV, database, or API sources).

---

## 🧪 Future Improvements

* Integration with **FAISS** or **ChromaDB** for scalable vector search
* Contextual recommendation graph using **LangGraph**
* Fine-tuning embeddings with user feedback
* Adding a **Streamlit frontend** for real-time visualization
* Multi-language support (English, Portuguese, Spanish)

---

## 💡 Example Use Cases

* Course and product recommendation systems
* Personalized e-learning platforms
* E-commerce intelligent suggestion engines
* Chatbots with contextual product guidance
* AI-based content filtering systems

---

## 🧑‍💻 Author

**Developed by:** Maison De Parfum
**Role:** AI Engineer / Developer
**Focus:** AI systems, intelligent recommendation engines, and LangChain-based projects.

---

## 🪪 License

This project is open-source under the **MIT License**.
You are free to modify and distribute it with attribution.

---

Quer que eu **adicione esse README ao ZIP** e gere uma nova versão para download?
