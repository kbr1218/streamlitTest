# tab_map.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components

import pandas as pd

# 제주도 중심 위도경도 변수 선언
LAT = 33.38032
LONG = 126.55

def show_tab_map():
  map_col1, map_col2 = st.columns([3, 1])

  with map_col1:
    m = folium.Map(location=[LAT, LONG], zoom_start=10)

    # 필터링된 위치에 마커 추가
    # for _, row in filtered_data.iterrows():
    folium.Marker(
      # 중심 위치는 평균으로 설정
      location=[LAT, LONG],
      popup=("제주도"),
      icon=folium.Icon(color="red", icon='heart', prefix='fa')
    ).add_to(m)
    
    # folium 지도를 streamlit에 표시
    st_folium(m, width=1000, height=350)