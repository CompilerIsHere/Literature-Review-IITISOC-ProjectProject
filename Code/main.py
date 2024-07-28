# %%writefile main.py
import streamlit as st
# import streamlit as st
# import requests
# from transformers import pipeline
# from rouge_score import rouge_scorer
# from bs4 import BeautifulSoup
# from tabula import read_pdf
# from tabulate import tabulate
import home
import temp

import app
# st.title("Hai")

    # Add a selectbox to the sidebar:
page = st.sidebar.selectbox(
        'Select a page',
        ('Home','Summary Generator', 'Table Extractor')
    )
if page == 'Home':
    home.home()

elif page == 'Summary Generator':
    temp.app()
elif page == 'Table Extractor':
    app.app1()