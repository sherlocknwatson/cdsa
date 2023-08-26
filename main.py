import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI(openai_api_key="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")

st.title("한국데이터사이언티스트협회 노코딩 분석툴 검색")

contents = st.text_input('노코드 분석툴 이름을 입력하세요')

if st.button('설명받기') :
    with st.spinner('작성 중...'):
        result = chat_model.predict(contents +"에 대한 기능을 설명해줘")
        st.write(result)






