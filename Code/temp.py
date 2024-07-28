# %%writefile app.py
import streamlit as st
import requests
from transformers import pipeline
# from rouge_score import rouge_scorer
from bs4 import BeautifulSoup

# Load summarization model (replace with your actual model path)
summarizer = pipeline('summarization', model='facebook/bart-large-cnn')


# def create_summaryOf_full_text_returnedAsString(URL):
#   r = requests.get(URL)
#   soup = BeautifulSoup(r.text, 'html')
#   find = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])
#   dict_to_store_title_para_pairs = {}
#   para = ''; heading = ''
#   for i in range(len(find)):
#     if(find[i].name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
#       heading = find[i].text.strip()
#       i += 1
#       while(i < len(find) and find[i].name == 'p'):
#         para += find[i].text.strip()
#         i+=1
#       dict_to_store_title_para_pairs[heading] = para
#       para = ''
#       heading = ''

#   ARTICLE = ""
#   for heading, summary in dict_to_store_title_para_pairs.items():
#     ARTICLE += summary + " "

#   total_summary_list = []
#   i = 0
#   for i in range(0, len(ARTICLE), 1000):
#     summary = summarizer(ARTICLE[i:min(i+1000, len(ARTICLE))])
#     total_summary_list.append(summary[0]['summary_text'])
#   total_summary = ' '.join(total_summary_list)

#   return total_summary

def create_summary(text):
  summary_list = []
  i = 0
  while(i < len(text)):
    summary = summarizer(text[i:min(i+1000, len(text))])
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
def soup(URL):
  r = requests.get(URL)
  soup = BeautifulSoup(r.text, 'html')
  para = soup.find_all('p')
  text = ''.join([p.text for p in para])
  return text



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
# page_bg_color = f"""<style>

#                     background-color: yellow;
#                     background-size: cover;
#                     background-position: center center;
#                     background-repeat: no-repeat;
#                     background-attachment: local;

#                 </style>"""


# st.markdown(page_bg_color, unsafe_allow_html=True)

  left, right = st.columns(2)
  with right:
    st.image("iitisoc.png")

  with left:
    st.header('Summary Generator')
    option =  st.selectbox('select article type',['link','text'])
  if option == 'link':
    link = st.text_input('Please paste the link of the text for summary generation')
    if link:
      summary = create_summary_return_dictOf_head_sum_pair(link)
      st.success('Summary generated successfully!')
      st.write(summary)
      # st.write('Rouge score : ')
      # scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
      # scores = scorer.score(soup(link), summary)
      # st.write(scores)
  else:
    para = st.text_input('please paste the text for summary generation')
    if para:
      summary = create_summary(para)
      st.success('Summary generated successfully!')
      st.write(summary)
      # st.write('Rouge score : ')
      # scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
      # scores = scorer.score(para, summary)
      # st.write(scores)



