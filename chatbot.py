import streamlit as st 
from streamlit_chat import message 
import pandas as pd 
from sentence_transformers import SentenceTransformer 
from sklearn.metrics.pairwise import cosine_similarity 
import json

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

local_css("style.css")

# 챗봇 UI 설계
st.title('부산 소프트웨어마이스터 고등학교 🏫')
st.subheader('홍보 및 입학 안내 챗봇:)')
st.write('안녕하세요, 부산 소프트웨어 마이스터 고등학교 입학 안내 챗봇입니다. 궁금한것에 대해 문의해주세요!')

tab1,tab2,tab3 = st.tabs(["학교 소개","입학안내","문의"])

with tab1:
    st.header("저희 소마고를 소개합니다")
with tab2:
    st.header("입학 안내")
with tab3:
    st.header("문의 - 051")
    
st.sidebar.header('About')
st.sidebar.markdown('[BSSM 사이트 바로가기](https://school.busanedu.net/bssm-h/main.do)')

st.sidebar.header('About')
st.sidebar.markdown('[BSSM 사이트 바로가기](https://school.busanedu.net/bssm-h/main.do)')


# 채팅 폼
with st.form('form',clear_on_submit = True):
    user_input = st.text_input('질문 : ','')
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
        st.session_state.generated.append("잘 모르겠습니다. 더 자세한 문의는 입학 문의처로 해주세요")

for i in range(len(st.session_state['past'])):
    # message(st.session_state['past'][i],is_user=True,key=str(i) + '_user')
    # if len(st.session_state['generated']) > i:
    #     message(st.session_state['generated'][i],key=str(i)+'_bot')
    st.markdown(
    """
    <div class="msg right-msg">
        <div class="msg-img">
        {0}
        </div>
    <div class="msg left-msg">
    {1}
    </div>
    """.format(st.session_state['past'][i], st.session_state['generated'][i]), unsafe_allow_html=True)
