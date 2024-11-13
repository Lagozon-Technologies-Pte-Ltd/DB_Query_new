# global selected_subject
# config.py
#subject_areas = ['HR', 'Customer Support', 'Medical', 'Inventory', 'Sales', 'Finance', 'Insurance', 'Legal']
from dotenv import load_dotenv # type: ignore
import os
import streamlit as st # type: ignore

# Load environment variables from .env file
load_dotenv()
flag=os.getenv("flag")
if flag=="True":
    subject_areas1 = os.getenv('subject_areas1').split(',')
    selected_subject = subject_areas1[0]
else :
    subject_areas2 = os.getenv('subject_areas2').split(',')
    selected_subject = subject_areas2[0]
if flag=="True":
    if "selected_subject" not in st.session_state:
        st.session_state.selected_subject = subject_areas1[0]
    if "previous_subject" not in st.session_state:
        st.session_state.previous_subject = subject_areas1[0]
    
else:
    if "selected_subject" not in st.session_state:
        st.session_state.selected_subject = subject_areas2[0]
    if "previous_subject" not in st.session_state:
        st.session_state.previous_subject = subject_areas2[0]
models = os.getenv('models').split(',')
selected_models = models[0]
# database = ['PostgreSQL', 'Oracle', 'SQLite', 'MySQL']
databases = os.getenv('databases').split(',')
selected_database = databases[0]
gauge_config = {
    "Faithfulness": {"value": 95, "color": "green"},
    "Relevancy": {"value": 82, "color": "lightgreen"},
    "Precision": {"value": 80, "color": "yellow"},
    "Recall": {"value": 78, "color": "orange"},
    "Harmfulness": {"value": 15, "color": "green"}
}