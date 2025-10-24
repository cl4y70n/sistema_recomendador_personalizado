from app.utils.embeddings import get_user_vector, get_product_vectors, rank_products

def get_recommendations(user_id: str):
    user_vec = get_user_vector(user_id)
    products = get_product_vectors()
    ranked = rank_products(user_vec, products)
    return ranked