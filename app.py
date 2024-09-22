import streamlit as st

# 페이지 제목 설정
st.set_page_config(page_title="시작 페이지", page_icon=":🍊:", layout="wide")

# CSS 파일 불러오기
with open('style/start_page.css', encoding='utf-8') as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# 로고 말풍선
st.markdown("""
    <div class="chat-container">
        <img src="imgs/dolhareubang.png" class="chat-icon" alt="돌하르방">
        <div class="chat-bubble">
            <img src="imgs/title.png" class="title-image" alt="Title Image">
        </div>
    </div>
""", unsafe_allow_html=True)

# 텍스트 말풍선
st.markdown("""
    <div class="chat-container">
        <img src="imgs/dolhareubang.png" class="chat-icon" alt="돌하르방">
        <div class="chat-bubble">
            <div class="chat-text">
                hihi.<br>
                서비스를 소개하는 말
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 시작하기 버튼
st.markdown("<div class='chat-bubble'>", unsafe_allow_html=True)
if st.button("시작하기"):
    st.write("다음 페이지로 이동합니다.")
st.markdown("</div>", unsafe_allow_html=True)
