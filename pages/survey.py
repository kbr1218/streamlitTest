# survey.py: 사용자 질문 페이지
import streamlit as st

# 페이지 제목 설정
st.set_page_config(page_title="survey", page_icon=":clipboard:", layout="wide")

# CSS 파일 불러오기
with open('style/survey_page.css', encoding='utf-8') as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# 페이지 내용
st.title("✒️시작 하기 전에")
st.caption("🚀 caption을 작성하는 부분임다")
st.markdown("<hr>", unsafe_allow_html=True)


# 첫 인사말 말풍선
st.markdown("""
    <div class="chat-container">
        <img src="https://raw.githubusercontent.com/kbr1218/streamlitTest/main/imgs/dolhareubang.png" class="chat-icon" alt="돌하르방">
        <div class="chat-bubble">
            <div class="chat-text">
                Hi there! <br>
                이름을 알려줘
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 이름 입력 칸
name = st.text_input(" ", placeholder="이름을 입력해주세요", 
                     key="name_input",
                     label_visibility="hidden")

# 이름 입력 후 엔터 키를 눌렀을 때
if name or st.session_state.name_input != "":
    st.session_state['show_next_bubble'] = True
    # 이름 입력 칸 숨기기
    st.session_state.name_input_visible = False

# 이름 인풋 숨기기
if 'name_input_visible' in st.session_state and not st.session_state.name_input_visible:
    st.markdown("<style>div[data-testid='stTextInput'] { display: none; }</style>", unsafe_allow_html=True)


if 'show_next_bubble' in st.session_state and st.session_state['show_next_bubble']:
    st.markdown(f"""
    <div class="user-chat-container">
        <div class="chat-bubble">
            <div class="chat-text">
                {name}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# 두 번째 말풍선
if 'show_next_bubble' in st.session_state and st.session_state['show_next_bubble']:
    st.markdown("""
        <div class="chat-container">
        <img src="https://raw.githubusercontent.com/kbr1218/streamlitTest/main/imgs/dolhareubang.png" class="chat-icon" alt="돌하르방">
        <div class="chat-bubble">
            <div class="chat-text">
                질문입니다
            </div>
            <a href="#" class="button">🛫 선택지1</a>
            <a href="#" class="button">📅 선택지2</a>
            <a href="#" class="button">❓ 선택지3</a>
            <a href="#" class="button">📞 선택지4</a>
        </div>
        </div>
    """, unsafe_allow_html=True)

