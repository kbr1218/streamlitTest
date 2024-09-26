# app.py
import streamlit as st

# 페이지 제목 설정
st.set_page_config(page_title="시작 페이지", page_icon=":🍊:", layout="wide")

# CSS 파일 불러오기
with open('style/start_page.css', encoding='utf-8') as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# 이미지 변수 선언
titleImgPath = 'https://raw.githubusercontent.com/kbr1218/streamlitTest/main/imgs/dolhareubang.png'
botImgPath = 'https://raw.githubusercontent.com/kbr1218/streamlitTest/main/imgs/dolhareubang.png'


# 타이틀 이미지
titleImg = (f"""
<div class=titleImg>
    <img src="{titleImgPath}" alt="title image" width="50%">
</div>
""")
st.markdown(titleImg, unsafe_allow_html=True)


# title
# st.title("🍊 시작페이지")
# st.caption("🚀 caption을 작성하는 부분임다")
# st.markdown("<hr>", unsafe_allow_html=True)

# 말풍선
st.markdown("""
    <div class="chat-container">
        <img src="https://raw.githubusercontent.com/kbr1218/streamlitTest/main/imgs/dolhareubang.png" class="chat-icon" alt="돌하르방">
        <div class="chat-bubble">
            <div class="chat-text">
                hihi.<br>
                서비스를 소개하는 말
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='button-container'>
        <a href="/survey">
        <button class="start_button">
            시작하기
        </button>
        </a>
    </div>
""", unsafe_allow_html=True)