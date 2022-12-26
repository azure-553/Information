import streamlit as st 
from streamlit_chat import message 
import pandas as pd 
from sentence_transformers import SentenceTransformer 
from sklearn.metrics.pairwise import cosine_similarity 
import json

# 챗봇 UI 설계
st.title('부산소프트웨어마이스터고등학교 챗봇:)')
st.subheader('안녕하세요, 부산 소프트웨어 마이스터 고등학교 입학 안내 챗봇입니다.')

# 채팅 폼
with st.form('form',clear_on_submit = True):
    user_input = st.text_input('사용자 : ','')
    submitted = st.form_submit_button('전송')

@st.cache(allow_output_mutation=True)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('bsm_chatbot.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

# 응답
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

# 사용자 질문
if 'past' not in st.session_state:
    st.session_state['past'] = []

# 예회처리
if submitted and user_input:
    embedding = model.encode(user_input)

    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding],[x]).squeeze())
    answer = df.loc[df['distance'].idxmax()]

    st.session_state.past.append(user_input)
    if answer['distance'] > 0.5:
        st.session_state.generated.append(answer['챗봇'])
    else:
        st.session_state.generated.append("무슨 말인지 모르겠어요")

for i in range(len(st.session_state['past'])):
    message(st.session_state['past'][i],is_user=True,key=str(i) + '_user')
    if len(st.session_state['generated']) > i:
        message(st.session_state['generated'][i],key=str(i)+'_bot')
