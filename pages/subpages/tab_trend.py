# tab_trend.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import time
import altair as alt

# 제주도 중심 위도경도 변수 선언
LAT = 33.38032
LONG = 126.55

# 데이터프레임 가져오기
df_month = pd.read_csv("testdata/rank_by_month_type.csv", encoding='cp949')
df = pd.read_csv("testdata\local_over_80.csv", encoding='cp949')

def show_tab_trend(): 
  #### 01. 월별 타입별 방문객 순위 ###
  st.write("")
  type_options_1 = df_month['MCT_TYPE'].unique()
  # 컬럼 레이아웃 설정
  col0_1, col0_2 = st.columns([3, 1])
  # type 종류
  type_options_1 = sorted(df_month['MCT_TYPE'].unique())

  with col0_2:
    # multiselect
    selected_type_1 = st.multiselect('Select Type (최대 5개까지 선택 가능합니다)',
                                     type_options_1,
                                     default=[type_options_1[0]], # 기본값으로 하나 선택
                                     key='graph1'
                                     )
    
    # 선택한 MCT_TYPE이 5개를 넘으면 경고 메시지 표시
    if len(selected_type_1) > 5:
      st.warning("⚠️ 카테고리는 최대 5개까지 선택할 수 있습니다.")
      selected_type_1 = selected_type_1[:5]  # max 5
  
  with col0_1:
      if not selected_type_1:
        selected_type_1 = [type_options_1[0]]  # 선택된 type이 없으면 기본값으로 첫 번째 타입 그래프 출력
        
      choosen_types = df_month[df_month['MCT_TYPE'].isin(selected_type_1)]

      # 그래프 출력
      chart = alt.Chart(choosen_types).mark_line(point=True).encode(
        x=alt.X("MONTH:O", title="월"),
        y=alt.Y('RANK_CNT:Q', title='평균 이용 건수 분위수'),
        color='MCT_TYPE:N',                                    # 각 타입별 색상 구분
        tooltip=['MONTH', 'MCT_TYPE', 'RANK_CNT']
      ).properties(
        title=f'\n선택된 {", ".join(selected_type_1)}의 월별 평균 이용 건수 분위수',
      )
      st.altair_chart(chart, use_container_width=True)


  #### 02. 현지인 비중 상위 80% 식당 ###
  # 변수 초기화
  if 'selected_ym_2' not in st.session_state:
      st.session_state.selected_ym_2 = None
  if 'selected_type_2' not in st.session_state:
      st.session_state.selected_type_2 = None
  if 'random_seed' not in st.session_state:
      st.session_state.random_seed = int(time.time())

  col1, col2 = st.columns(2)
  with col1:
    # selectbox
    ym_options_2 = sorted(df['MONTH'].unique())
    type_options_2 = sorted(df['MCT_TYPE'].unique())

    col1_1, col1_2 = st.columns(2)
    with col1_1:
      selected_ym_2 = st.selectbox('Select Month', ym_options_2, key='map1')
    with col1_2:
        selected_type_2 = st.selectbox('Select Type', type_options_2, key='map2')
    
    # 기본 아이콘 설정
    icon_name='utensils'

    # MONTH/TYPE이 변경된 경우에만 random_seed 갱신
    if (selected_ym_2 != st.session_state.selected_ym_2) or (selected_type_2 != st.session_state.selected_type_2):
      st.session_state.random_seed = int(time.time())
      st.session_state.selected_ym_2 = selected_ym_2
      st.session_state.selected_type_2 = selected_type_2
    
    if st.session_state.selected_type_2 == '커피':
      icon_name='coffee'
    elif st.session_state.selected_type_2 == '디저트/간식':
        icon_name='ice-cream'
    elif st.session_state.selected_type_2 == '베이커리':
      icon_name='bread-slice'
    elif st.session_state.selected_type_2 == '세계 요리':
      icon_name='globe'
    elif st.session_state.selected_type_2 == '맥주/요리주점':
      icon_name='beer'
    elif st.session_state.selected_type_2 == '치킨':
      icon_name='drumstick-bite'
    elif st.session_state.selected_type_2 == '패스트푸드/간단한 식사':
      icon_name='hamburger'
    elif st.session_state.selected_type_2 == '피자':
      icon_name='pizza-slice'



    # 선택한 MONTH과 TYPE_NAME에 따라 데이터 필터링
    filtered_data = df[(df['MONTH'] == selected_ym_2) & (df['MCT_TYPE'] == selected_type_2)]
    # 현지인 비중 백분율로 변환
    filtered_data.loc[:, 'LOCAL_UE_CNT_RAT'] = filtered_data['LOCAL_UE_CNT_RAT'].astype(str) + '%'

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