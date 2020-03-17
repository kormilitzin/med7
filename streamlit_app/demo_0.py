import spacy
from spacy import displacy
import streamlit as st
import numpy as np
import pandas as pd

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""


st.text('Please wait while Med7 is loading...')
med7 = spacy.load('en_core_med7_lg')

col_dict = {}
seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
    col_dict[label] = colour

options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}

labels = med7.pipe_labels['ner']

sentence = st.text_input('Input your sentence here:') 

if sentence:
    doc = med7(sentence)
    st.write('The identified medical concepts:')
    html = displacy.render(doc, style="ent", options=options)
    # Newlines seem to mess with the rendering
    html = html.replace("\n", " ")
    st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)
    attrs = ["text", "label_", "start_char", "end_char"]

    data = [
            [str(getattr(ent, attr)) for attr in attrs]
            for ent in doc.ents
            if ent.label_ in labels
        ]
    st.write('The structured table:')
    df = pd.DataFrame(data, columns=attrs)
    st.dataframe(df)