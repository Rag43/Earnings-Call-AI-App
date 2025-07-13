from app.services.sentiment import (
    get_management_sentiment,
    get_qa_sentiment,
    get_tone_trend_over_quarters,
    get_strategic_focuses
)

quarters = ["Q1_2025.txt", "Q4_2024.txt", "Q3_2024.txt", "Q2_2024.txt"]

# Optional: Run one at a time if using GPT-4 to avoid rate limits
for q in quarters:
    print(f"\n📊 {q}")
    print("📈 Management Sentiment:")
    print(get_management_sentiment(q))

    print("\n🎤 Q&A Sentiment:")
    print(get_qa_sentiment(q))

    print("\n📌 Strategic Focuses:")
    print(get_strategic_focuses(q))

# 🔄 Quarter-to-quarter trend summary
print("\n🔁 Quarter-over-Quarter Tone Trend:")
trend = get_tone_trend_over_quarters(quarters)
for t in trend:
    print(t)
