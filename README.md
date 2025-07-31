# 🧠 NVIDIA Earnings Call Signal Dashboard

A web-based dashboard that uses LLMs (via the OpenAI API) to extract and visualize sentiment insights from the last four NVIDIA earnings call transcripts.

## 🔍 Overview

This project leverages LLMs to analyze both **management remarks** and **Q&A sessions** from NVIDIA's quarterly earnings calls. The app extracts:

- 📈 Management Sentiment  
- 🎤 Q&A Sentiment  
- 📌 Strategic Focuses  
- 📊 Quarter-over-Quarter Sentiment Trends  

Sentiment is evaluated using prompt-based querying over indexed transcripts, powered by [`llama-index`](https://github.com/jerryjliu/llama_index).

## 🖼️ Demo Screenshots

### Dashboard View – Sentiment Analysis for Q1 2025
![Dashboard Screenshot](./screenshots/Screenshot%202025-07-31%20at%204.32.08%20PM.png)

### Strategic Focuses and Sentiment Trend
![Trend Screenshot](./screenshots/Screenshot%202025-07-31%20at%204.32.25%20PM.png)

## 🛠️ Tech Stack

- **Frontend**: React (Vite)  
- **Backend**: Python (FastAPI or equivalent)  
- **LLM API**: OpenAI  
- **Vector Store**: `llama-index` + local persistence  
- **Data**: Raw earnings call transcripts  

## 📂 Project Structure

```
app/
├── data/
│   ├── transcripts/         # Raw transcript .txt files
│   └── index/               # Persisted LlamaIndex vector store
├── services/
│   ├── llama_indexer.py     # Index builder/loader
│   └── sentiment.py         # OpenAI-powered sentiment analysis
├── main.py                  # Backend API entrypoint
frontend/
├── main.jsx                 # React root render
├── App.jsx                  # UI logic and state
├── index.css                # Styling
```

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/nvidia-earnings-dashboard.git
cd nvidia-earnings-dashboard
```

### 2. Install Backend Requirements

```bash
cd app
pip install -r requirements.txt
```

Required packages include:

- `llama-index`  
- `openai`  
- `fastapi`  
- `uvicorn`  

### 3. Set OpenAI API Key

Create a `.env` file in the root of the project:

```bash
OPENAI_API_KEY=your-key-here
```

### 4. Index the Transcripts

```bash
python -c "from services.llama_indexer import build_index; build_index()"
```

This will process all transcripts in `app/data/transcripts/` and persist the index.

### 5. Run the Backend

```bash
uvicorn main:app --reload
```

### 6. Run the Frontend

```bash
cd frontend
npm install
npm run dev
```

## 🧪 Testing

You can run backend sentiment tests with:

```bash
python test_sentiment.py
```

## 📈 Example Use Case

This dashboard is designed for financial analysts, investors, and NLP practitioners to:

- Gauge sentiment trends across quarters  
- Track AI ecosystem developments mentioned by NVIDIA  
- Compare management tone vs Q&A responsiveness  

## 📬 Contact

Built by **Raghav Sunil**  
If you’re interested in collaborating on NLP, AI infrastructure, or LLM-powered apps, feel free to reach out!

## 📝 License

MIT License