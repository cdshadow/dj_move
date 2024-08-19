import streamlit as st
import pandas as pd
import plotly.express as px

tab1, tab2 = st.tabs(['순이동', '탭'])

# GitHub raw content URL의 data.csv 파일 경로
file_path = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data.csv'

# 데이터를 캐시하여 로딩
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='cp949')
    # 년도를 문자열로 변환
    data['년도'] = data['년도'].astype(str)
    return data

data = load_data(file_path)


with tab1:
    # Plotly를 이용한 꺾은선 그래프
    fig = px.line(data, x='년도', y='순이동 인구수', title='2001년~2023년 대전시 순이동 변화',
                  markers=True)
    
    # x축의 모든 연도를 표시하도록 수정
    fig.update_xaxes(tickmode='linear', tick0=data['년도'].min(), dtick=1)
    
    # y축의 간격을 5,000 단위로 설정
    fig.update_yaxes(tick0=0, dtick=5000)
    
    # 그래프 커스터마이징 (선택 사항)
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_title='년도', yaxis_title='순이동 인구수')
    
    # Streamlit에서 Plotly 그래프를 표시
    st.plotly_chart(fig)
    
    # 데이터 확인
    #st.write("2001년~2023년 대전시 순이동 인구수")
    st.table(data)


with tab2:
    st.table(data.head(5))
    
