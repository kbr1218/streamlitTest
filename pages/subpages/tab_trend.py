# tab_trend.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import time

# 제주도 중심 위도경도 변수 선언
LAT = 33.38032
LONG = 126.55

# 데이터프레임 가져오기
df = pd.read_csv("testdata\local_over_80.csv", encoding='cp949')

def show_tab_trend(): 
  # 변수 초기화
  if 'selected_ym' not in st.session_state:
      st.session_state.selected_ym = None
  if 'selected_type' not in st.session_state:
      st.session_state.selected_type = None
  if 'random_seed' not in st.session_state:
      st.session_state.random_seed = int(time.time())

  col1, col2 = st.columns(2)
  with col1:
    # selectbox
    ym_options = df['MONTH'].unique()
    type_options = df['TYPE_NAME'].unique()

    col1_1, col1_2 = st.columns(2)
    with col1_1:
      selected_ym = st.selectbox('Select Month', ym_options)
    with col1_2:
        selected_type = st.selectbox('Select Type', type_options)
    
    # 기본 아이콘 설정
    icon_name='utensils'

    # MONTH/TYPE이 변경된 경우에만 random_seed 갱신
    if (selected_ym != st.session_state.selected_ym) or (selected_type != st.session_state.selected_type):
      st.session_state.random_seed = int(time.time())
      st.session_state.selected_ym = selected_ym
      st.session_state.selected_type = selected_type
    
    if st.session_state.selected_type == '커피':
      icon_name='coffee'
    elif st.session_state.selected_type == '디저트/간식':
        icon_name='ice-cream'
    elif st.session_state.selected_type == '베이커리':
      icon_name='bread-slice'
    elif st.session_state.selected_type == '세계 요리':
      icon_name='globe'
    elif st.session_state.selected_type == '맥주/요리주점':
      icon_name='beer'
    elif st.session_state.selected_type == '치킨':
      icon_name='drumstick-bite'
    elif st.session_state.selected_type == '패스트푸드/간단한 식사':
      icon_name='hamburger'
    elif st.session_state.selected_type == '피자':
      icon_name='pizza-slice'



    # 선택한 MONTH과 TYPE_NAME에 따라 데이터 필터링
    filtered_data = df[(df['MONTH'] == selected_ym) & (df['TYPE_NAME'] == selected_type)]
    # 현지인 비중 백분율로 변환
    filtered_data['LOCAL_UE_CNT_RAT'] = (filtered_data['LOCAL_UE_CNT_RAT'] * 100).round(2).astype(str) + '%'

    # 데이터는 최대 5개로 제한 & 랜덤으로 추출
    filtered_data = filtered_data.sample(n=min(5, len(filtered_data)), random_state=st.session_state.random_seed)

    # 지도 초기화
    m = folium.Map(location=[LAT, LONG], zoom_start=10)

    # 필터링된 위치에 마커 추가
    for _, row in filtered_data.iterrows():
      folium.Marker(
         # 중심 위치는 평균으로 설정
        location=[row['latitude'], row['longitude']],
        popup=(f"{row['MCT_NM']}"),
        icon=folium.Icon(color="orange", icon=icon_name, prefix='fa')
      ).add_to(m)
    
    # folium 지도를 streamlit에 표시
    st_folium(m, width=800, height=350)

    # 선택한 식당 정보를 테이블로 출력
    st.subheader("📍매장 정보")
    filtered_data_display = filtered_data[['MCT_NM', 'ADDR', 'LOCAL_UE_CNT_RAT']].rename(
       columns={
          'MCT_NM': '매장명',
          'ADDR': '주소',
          'LOCAL_UE_CNT_RAT': '현지인 이용 비중'
          }
    ).reset_index(drop=True)
    st.table(filtered_data_display)