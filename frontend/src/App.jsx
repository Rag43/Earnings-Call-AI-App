// Restored App.jsx to working version (with full sentiment strings)
import React, { useEffect, useState } from "react";
import axios from "axios";

const quarters = ["Q1_2025", "Q4_2024", "Q3_2024", "Q2_2024"];

function App() {
  const [selectedQuarter, setSelectedQuarter] = useState(quarters[0]);
  const [sentiment, setSentiment] = useState(null);
  const [focuses, setFocuses] = useState([]);
  const [trendData, setTrendData] = useState([]);

  // Fetch sentiment & focuses when quarter changes
  useEffect(() => {
    axios
      .get(`http://localhost:8000/api/sentiment/${selectedQuarter}`)
      .then((res) => setSentiment(res.data))
      .catch((err) => console.error("Sentiment API error:", err));

    axios
      .get(`http://localhost:8000/api/focuses/${selectedQuarter}`)
      .then((res) =>
        setFocuses(res.data.strategic_focuses.split("\n").filter(Boolean))
      )
      .catch((err) => console.error("Focuses API error:", err));
  }, [selectedQuarter]);

  // Fetch tone trend once on load
  useEffect(() => {
    axios
      .get("http://localhost:8000/api/tone-trend")
      .then((res) => setTrendData(res.data))
      .catch((err) => console.error("Tone trend API error:", err));
  }, []);

  return (
    <div
      style={{
        padding: "2rem",
        maxWidth: "800px",
        margin: "0 auto",
        fontFamily: "sans-serif",
      }}
    >
      <h1>🧠 NVIDIA Earnings Call Signal Dashboard</h1>
      <p>Insights extracted using LLMs over the last 4 earnings calls</p>

      <div style={{ margin: "1rem 0" }}>
        <label htmlFor="quarter">Select Quarter:&nbsp;</label>
        <select
          id="quarter"
          value={selectedQuarter}
          onChange={(e) => setSelectedQuarter(e.target.value)}
        >
          {quarters.map((q) => (
            <option key={q} value={q}>
              {q}
            </option>
          ))}
        </select>
      </div>

      {sentiment && (
        <>
          <h2>📈 Management Sentiment</h2>
          <p>{sentiment.management}</p>

          <h2>🎤 Q&A Sentiment</h2>
          <p>{sentiment.qa}</p>
        </>
      )}

      {focuses.length > 0 && (
        <>
          <h2>📌 Strategic Focuses</h2>
          <ul>
            {focuses.map((line, idx) => (
              <li key={idx}>{line}</li>
            ))}
          </ul>
        </>
      )}

      <h2>🔄 Quarter-over-Quarter Tone Trend</h2>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th style={{ borderBottom: "1px solid #ccc", textAlign: "left" }}>
              Quarter
            </th>
            <th style={{ borderBottom: "1px solid #ccc", textAlign: "left" }}>
              Mgmt Sentiment
            </th>
            <th style={{ borderBottom: "1px solid #ccc", textAlign: "left" }}>
              Q&A Sentiment
            </th>
          </tr>
        </thead>
        <tbody>
          {trendData.map((t, idx) => (
            <tr key={idx}>
              <td style={{ padding: "0.5rem 0" }}>{t.quarter}</td>
              <td>{t.management_sentiment.trim().split(/\s+/)[0]}</td>
              <td>{t.qa_sentiment.trim().split(/\s+/)[0]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
