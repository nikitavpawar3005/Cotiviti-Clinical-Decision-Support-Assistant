import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

st.set_page_config(
    page_title="Clinical Decision Support",
    page_icon="🏥"
)
st.sidebar.title("Project Information")

st.sidebar.markdown("""
### AI Clinical Decision Support

**Developer**
Nikita Pawar

**University**
Arizona State University

**Technology**
- Python
- Streamlit
- Google Gemini
- Generative AI

**Purpose**
Assist healthcare professionals by generating AI-supported summaries and clinical decision-support recommendations from fictional clinical notes.
""")
load_dotenv("demo/.env")

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("Gemini API key not found. Please check your .env file.")
    st.stop()

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🏥 AI Clinical Decision Support Assistant")

st.caption(
    "Powered by Google Gemini | Built using Python & Streamlit"
)

st.markdown("""
This application demonstrates how Generative AI can assist healthcare professionals
by analyzing clinical notes, identifying potential risks, and generating concise
decision-support recommendations.

**Project:** Clinical Decision Support Assistant

**Domain:** Healthcare | Generative AI | Clinical Decision Support
""")

sample_notes = {
    "Select a sample note": "",
    "High Risk - Cardiac": "A 58-year-old female arrived at the emergency department complaining of severe chest pain that began while climbing stairs. She has a history of hypertension and type 2 diabetes. ECG findings show ST-segment abnormalities, and troponin levels are elevated. The attending physician admitted the patient for continuous cardiac monitoring and requested an urgent cardiology consultation.",
    "Medium Risk - Diabetes Follow-up": "A 47-year-old male visited the outpatient clinic for a diabetes follow-up appointment. He reports missing several doses of his medication over the past month. His blood glucose remains above the target range, and his blood pressure is mildly elevated. The physician discussed medication adherence, diet changes, and scheduled a follow-up visit in four weeks.",
    "Low Risk - Routine Visit": "A 24-year-old patient visited the clinic with a sore throat, mild fever, and nasal congestion for two days. Physical examination showed no signs of serious infection. The physician advised rest, hydration, and over-the-counter medication, with instructions to return if symptoms worsen."
}

selected_sample = st.selectbox("Choose a sample clinical note", list(sample_notes.keys()))

patient_note = st.text_area(
    "Enter Clinical Notes",
    value=sample_notes[selected_sample],
    height=180
)
if st.button("🔍 Analyze Clinical Note"):
    if not patient_note.strip():
        st.warning("Please enter clinical notes before analyzing.")
    else:
        prompt = f"""
You are a healthcare AI assistant supporting clinical decision making.
Analyze the following fictional clinical note.

Important:
- Do not provide a diagnosis as final medical advice.
- Present the output as decision support only.
- Be concise and professional.

Clinical Note:
{patient_note}

Return the answer in this exact format:

Patient Summary:
Risk Level: Low, Medium, or High
Key Findings:
-
Recommended Next Steps:
-
"""

        try:
            with st.spinner("Gemini is reviewing the clinical note and generating decision-support output..."):
                response = model.generate_content(prompt)

            st.success("AI analysis completed successfully!")
            st.markdown(response.text)

            st.divider()

            st.info(
                "⚠️ This application is a proof-of-concept for educational purposes. "
                "It provides AI-assisted clinical decision support and should not be used "
                "to replace professional medical judgment, diagnosis, or treatment."
            )

        except Exception:
            st.error("Something went wrong while generating the AI response.")
            st.write("Please check your API key, internet connection, or model configuration.")