import streamlit as st
import pandas as pd
import plotly.express as px

tab1, tab2 = st.tabs(['순이동', '탭'])

# Use the file uploaded by the user
uploaded_file = '/mnt/data/image.png'  # Update this with the correct file path

# 데이터를 캐시하여 로딩
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='cp949')
    # 년도를 문자열로 변환
    data['년도'] = data['년도'].astype(str)
    return data

# Load the first dataset
data = load_data('https://raw.githubusercontent.com/cdshadow/dj_move/main/data.csv')

# Load the uploaded file
data2 = load_data(uploaded_file)

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
    st.table(data)

with tab2:
    # Assume the data is in a wide format with '년도' as index and each region as columns
    data2 = data2.set_index('지역').T.reset_index()
    data2 = pd.melt(data2, id_vars=['index'], var_name='지역', value_name='순이동 인구수')
    data2.rename(columns={'index': '년도'}, inplace=True)
    
    # Plotly를 이용한 꺾은선 그래프
    fig = px.line(data2, x='년도', y='순이동 인구수', color='지역', title='2001년~2023년 대전시 지역별 순이동 변화',
                  markers=True)
    
    # x축의 모든 연도를 표시하도록 수정
    fig.update_xaxes(tickmode='linear', tick0=data2['년도'].min(), dtick=1)
    
    # y축의 간격을 5,000 단위로 설정
    fig.update_yaxes(tick0=0, dtick=5000)
    
    # 그래프 커스터마이징 (선택 사항)
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_title='년도', yaxis_title='순이동 인구수')
    
    # Streamlit에서 Plotly 그래프를 표시
    st.plotly_chart(fig)
    
    # 데이터 확인
    st.table(data2)
