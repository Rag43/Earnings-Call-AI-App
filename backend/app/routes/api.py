from fastapi import APIRouter
from app.services.sentiment import (
    get_management_sentiment,
    get_qa_sentiment,
    get_strategic_focuses,
    get_tone_trend_over_quarters,
)

router = APIRouter()

@router.get("/api/sentiment/{quarter}")
def get_sentiments(quarter: str):
    return {
        "management": get_management_sentiment(f"{quarter}.txt"),
        "qa": get_qa_sentiment(f"{quarter}.txt"),
    }

@router.get("/api/focuses/{quarter}")
def get_focuses(quarter: str):
    return {
        "strategic_focuses": get_strategic_focuses(f"{quarter}.txt")
    }

@router.get("/api/tone-trend")
def get_tone_trend():
    quarters = ["Q1_2025.txt", "Q4_2024.txt", "Q3_2024.txt", "Q2_2024.txt"]
    return get_tone_trend_over_quarters(quarters)
