from app.services.llama_indexer import load_index

def get_management_sentiment(quarter_filename: str):
    index = load_index()
    query_engine = index.as_query_engine()

    prompt = f"""
    From the prepared remarks in the earnings call transcript file named {quarter_filename},
    determine the overall management sentiment. Focus only on the [Prepared Remarks] section.
    
    Respond with one of: Positive, Neutral, or Negative. Then briefly explain your reasoning.
    """

    response = query_engine.query(prompt)
    return str(response)

def get_qa_sentiment(quarter_filename: str):
    index = load_index()
    query_engine = index.as_query_engine()

    prompt = f"""
    From the Q&A session in the earnings call transcript file named {quarter_filename},
    determine the overall sentiment of management during analyst questioning.
    Focus only on the [Q&A Session] section.

    Respond with one of: Positive, Neutral, or Negative. Then briefly explain your reasoning.
    """

    response = query_engine.query(prompt)
    return str(response)

def get_strategic_focuses(quarter_filename: str):
    index = load_index()
    query_engine = index.as_query_engine()

    prompt = f"""
    Based on the full earnings call transcript file named {quarter_filename},
    extract the top 3 to 5 strategic themes or business initiatives that management emphasized.
    
    Return the answer as a bulleted list.
    """

    response = query_engine.query(prompt)
    return str(response)

def get_tone_trend_over_quarters(quarters: list[str]):
    trend = []

    for q in quarters:
        mgmt_sent = get_management_sentiment(q)
        qa_sent = get_qa_sentiment(q)

        trend.append({
            "quarter": q.replace(".txt", ""),
            "management_sentiment": mgmt_sent,
            "qa_sentiment": qa_sent,
        })

    return trend
