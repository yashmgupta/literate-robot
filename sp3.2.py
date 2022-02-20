
"""

You need to install spacy-streamlit from pip: pip install spacy-streamlit
English model from spaCy, Prerequisites: 
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_sd


"""
import streamlit as st
from spacy_streamlit import process_text
from spacy_streamlit import visualize_parser

st.title("Part of speech visualizer")

spacy_model = st.sidebar.selectbox("Model name", ["en_core_web_sm", "en_core_web_md"])
text = st.text_area("Text to analyze", "Type your text here")
doc = process_text(spacy_model, text)
visualize_parser(doc)