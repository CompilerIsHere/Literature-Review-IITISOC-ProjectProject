# %%writefile home.py
def home():
  import streamlit as st
  st.title('PaperDigest (IITISOC SUMMARY GENERATOR PROJECT IN ML DOMAIN)')
  st.header('An advanced summarization model designed to streamline your research journey.')
  st.header('The name of team members is : ')
  st.header('1. Saksham Gautam')
  st.header('2. Ishaan Sammi')
  st.header('3. Deepanshu')
  st.header('4. Raunak Anand')

  st.markdown
  page_bg_img = f"""
  <style>
  [data-testid="stAppViewContainer"] > .main {{
  background-image: url("https://cdn.dribbble.com/userupload/12925811/file/original-f7be1dc2525dd3d60641b24d427c15f0.jpg?resize=400x300&vertical=center");
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


