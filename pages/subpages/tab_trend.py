# tab_trend.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 제주도 중심 위도경도 변수 선언
LAT = 33.38032
LONG = 126.55

# 데이터프레임 가져오기
df = pd.read_csv("testdata\local_over_50.csv", encoding='cp949')

def show_tab_trend(): 
  # selectbox
  ym_options = df['YM'].unique()
  type_options = df['TYPE'].unique()

  col1, col2 = st.columns(2)
  with col1:
    selected_ym = st.selectbox('Select Month', ym_options)
  with col2:
      selected_type = st.selectbox('Select Type', type_options)


  # 선택한 YM과 TYPE에 따라 데이터 필터링
  filtered_data = df[(df['YM'] == selected_ym) & (df['TYPE'] == selected_type)]

  # 데이터는 최대 5개로 제한
  filtered_data = filtered_data.nlargest(5, 'LOCAL_UE_CNT_RAT')

  # folium map
  m = folium.Map(location=[LAT, LONG], zoom_start=10)

  # 필터링된 위치에 마커 추가
  for _, row in filtered_data.iterrows():
    folium.Marker(
      location=[row['latitude'], row['longitude']],
      popup=f"{row['MCT_NM']} (Rate: {row['LOCAL_UE_CNT_RAT']})"
    ).add_to(m)
  
  # folium 지도를 streamlit에 표시
  st_folium(m, width=600, height=350)