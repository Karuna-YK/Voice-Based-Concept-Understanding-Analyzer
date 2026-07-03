# Voice Based Concept Understanding Analyzer

## Overview

The Voice Based Concept Understanding Analyzer is an AI-powered web application that converts speech into text and evaluates the user's conceptual understanding using semantic similarity. The application also extracts audio features, calculates speech statistics, provides AI feedback, and generates a PDF report.

## Features

- Speech-to-Text Conversion
- Audio File Upload
- Audio Feature Extraction
- Word Count Calculation
- Speaking Speed Analysis
- Similarity Score Calculation
- AI-Based Feedback
- Performance Evaluation
- PDF Report Generation
- Interactive Streamlit User Interface


## Technologies Used

- Python
- Streamlit
- OpenAI Whisper
- Sentence Transformers
- Librosa
- NumPy
- Pandas
- Scikit-learn
- ReportLab
- Git
- GitHub
- Visual Studio Code


## Project Structure

```text
Voice-Based-Concept-Understanding-Analyzer/
│
├── app.py
├── requirements.txt
├── assets/
│   └── style.css
└── services/
    ├── speech_to_text.py
    ├── audio_features.py
    ├── similarity.py
    └── pdf_report.py
```

---

## Installation

```bash
pip install -r requirements.txt
```

```bash
streamlit run app.py
```


## Workflow

1. Upload an audio file.
2. Convert speech into text.
3. Extract audio features.
4. Calculate speech statistics.
5. Compare with the expected answer.
6. Generate similarity score.
7. Display AI feedback.
8. Download the PDF report.


## Output

- Speech Transcript
- Audio Statistics
- Similarity Score
- AI Feedback
- Performance Evaluation
- PDF Report
