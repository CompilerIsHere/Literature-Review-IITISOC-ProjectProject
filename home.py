# %%writefile home.py
def home():
  import streamlit as st
  st.title('IITISOC SUMMARY GENERATOR PROJECT IN ML DOMAIN')
  st.header('This is a literature review generator model made as a part of the project in ML domain of IITISOC.')
  st.header('The name of team members is : ')
  st.header('1. Saksham Gautam')
  st.header('2. Ishaan Sammi')
  st.header('3. Deepanshu')
  st.header('4. Raunak Anand')
  st.markdown
  page_bg_img = f"""
  <style>
  [data-testid="stAppViewContainer"] > .main {{
  background-image: url("");
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: local;
  }}
  [data-testid="stHeader"] {{
  background: rgba(0,0,0,0);
  }}
  </style>
  """

  st.markdown(page_bg_img, unsafe_allow_html=True)


