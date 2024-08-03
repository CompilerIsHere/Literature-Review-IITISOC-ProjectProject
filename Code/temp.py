#-----------------------------------------------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


def create_summary(text):
  summary_list = []
  i = 0
  while(i < len(text)):
    summary = query({
      "inputs": text[i:min(i+1000, len(text))],
    })
    summary_list.append(summary[0]['summary_text'])
    i += 1000
  summary_text = ' '.join(summary_list)
  return summary_text

def create_summary_return_dictOf_head_sum_pair(URL):
  r = requests.get(URL)
  soup = BeautifulSoup(r.text, 'html')
  find = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])
  dict_to_store_title_para_pairs = {}
  para = ''; heading = ''
  for i in range(len(find)):
    if(find[i].name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
      heading = find[i].text.strip()
      i += 1
      while(i < len(find) and find[i].name == 'p'):
        para += find[i].text.strip()
        i+=1
      dict_to_store_title_para_pairs[heading] = para
      para = ''
      heading = ''

  dict_to_store_title_summary_pairs = {}
  for heading, paragraph in dict_to_store_title_para_pairs.items():
    if(paragraph != ''):
      summary = create_summary(paragraph)
      dict_to_store_title_summary_pairs[heading] = summary

  return dict_to_store_title_summary_pairs

# create_summary_return_dictOf_head_sum_pair("https://en.wikipedia.org/wiki/Photoelectric_effect")


def app():
  st.title('LITERATURE REVIEW GENERATOR')

  st.write('---')




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


  left, right = st.columns(2)
  # with right:
    # st.image("iitisoc.png")

  with left:
    st.header('Summary Generator')
    option =  st.selectbox('select article type',['link','text'])
  if option == 'link':
    link = st.text_input('Please paste the link of the text for summary generation')
    if link:
      summary = create_summary_return_dictOf_head_sum_pair(link)
      st.success('Summary generated successfully!')
      st.write(summary)

  else:
    para = st.text_input('please paste the text for summary generation')
    if para:
      summary = create_summary(para)
      st.success('Summary generated successfully!')
      st.write(summary)
