# %%writefile app1.py
import pandas as pd
import streamlit as st
import tabula
from tabulate import tabulate
import dataframe_image as dfi

def app1():
#   import pandas as pd
#   import streamlit as st
# from tabula import read_pdf
# from tabulate import tabulate
  st.title("Table Extractor")
  file = st.file_uploader("Upload a PDF file", type=["pdf"])
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


# Reads table from pdf file
  if file is None:
    st.warning('Please upload a PDF file')
    df = None
  elif file is not None:
    df = tabula.read_pdf(file, pages="all")
    df1 = []
    for i in range(len(df)):
      df1.append(pd.DataFrame(df[i]))
    # Address of pdf file
    st.write(f"File uploaded: {file.name}")
    for i in range(len(df1)):
      dfi.export(df1[i].dropna(), 'dataframe' + str(i) + '.png')
      st.image('dataframe' + str(i) + '.png')




# '''import pandas as pd
# from tabulate import tabulate as tbl
# import tabula

# df = tabula.read_pdf("C:/Users/saksh/Downloads/Test.pdf", pages = "all")
# df1 = pd.DataFrame(df[0])

# import dataframe_image as dfi
# dfi.export(df1.dropna(), 'dataframe2.png')'''