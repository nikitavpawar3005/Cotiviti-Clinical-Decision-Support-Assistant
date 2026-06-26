# AI Clinical Decision Support Assistant

## Overview

This project is a proof of concept developed for the **Cotiviti Internship Assessment**.

The application demonstrates how **Generative AI** can support clinical decision-making by analyzing fictional clinical notes and generating:

* Patient Summary
* Risk Level (Low, Medium, High)
* Key Findings
* Recommended Next Steps

The application is built using **Python**, **Streamlit**, and **Google Gemini**.

---

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* python-dotenv

---

## Project Files

* `app.py` – Main Streamlit application
* `requirements.txt` – Project dependencies
* `Cotiviti_Report_Nikita_Pawar_ASU.docx` – Project report
* `Cotiviti_Final_Presentation_Nikita_Pawar_ASU.pptx` – Presentation
* Screenshots demonstrating the application

---

## How to Run

1. Clone the repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

4. Start the application:

```bash
streamlit run app.py
```

---

## Disclaimer

This application is intended for educational and demonstration purposes only. It uses fictional clinical data and is designed to showcase AI-assisted clinical decision support. It should not be used for real-world diagnosis or medical treatment decisions.
