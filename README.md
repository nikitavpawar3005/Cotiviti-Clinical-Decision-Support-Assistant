# AI Clinical Decision Support Assistant

This project is a proof-of-concept for Cotiviti’s GenAI internship assessment.

## Project Topic
Clinical Decision Making and Pattern Recognition in Health Care

## Overview
This Streamlit application uses Google Gemini to analyze fictional clinical notes and generate:
- Patient summary
- Risk level
- Key findings
- Recommended next steps

## Technologies Used
- Python
- Streamlit
- Google Gemini API
- python-dotenv

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Add Gemini API key in `.env`:
   GEMINI_API_KEY=your_api_key_here

3. Run the app:
   streamlit run demo/app.py

## Disclaimer
This project is for educational and demonstration purposes only. It is not intended to replace medical judgment, diagnosis, or treatment.