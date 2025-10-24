from fastapi import APIRouter
from app.services.recommendation import get_recommendations

router = APIRouter(prefix="/recommend", tags=["recommendations"])

@router.get("/{user_id}")
def recommend_items(user_id: str):
    recs = get_recommendations(user_id)
    return {"user_id": user_id, "recommendations": recs}