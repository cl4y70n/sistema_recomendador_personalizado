import numpy as np
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

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

def get_user_vector(user_id):
    interests = dummy_users.get(user_id, ["sem histórico"])
    return model.encode(" ".join(interests), convert_to_tensor=True)

def get_product_vectors():
    return {p: model.encode(p, convert_to_tensor=True) for p in dummy_products}

def rank_products(user_vec, products):
    scores = {p: util.cos_sim(user_vec, emb).item() for p, emb in products.items()}
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [p for p, _ in ranked]