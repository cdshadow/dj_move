import streamlit as st
import pandas as pd
import plotly.express as px

tab1, tab2, tab3, tab4 = st.tabs(['대전시 년도별 순이동', '대전시 년도별·지역별 순이동', '세종시 년도별 순이동', '세종시 년도별·지역별 순이동'])

# GitHub raw content URL의 data.csv 파일 경로
file_path = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data.csv'
file_path2 = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data2.csv'
file_path3 = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data3.csv'
file_path4 = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data4.csv'

# 데이터를 캐시하여 로딩
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='cp949')
    # 년도를 문자열로 변환
    data['년도'] = data['년도'].astype(str)
    return data

# data.csv 파일 로드
data = load_data(file_path)

# data2.csv 파일 로드
data2 = load_data(file_path2)

# data3.csv 파일 로드
@st.cache_data
def load_data3(file_path3):
    data3 = pd.read_csv(file_path3, encoding='cp949')
    # 년도를 문자열로 변환
    data3['년도'] = data3['년도'].astype(str)
    return data3

data3 = load_data3(file_path3)

# data4.csv 파일 로드
@st.cache_data
def load_data4(file_path4):
    data4 = pd.read_csv(file_path4, encoding='cp949')
    # 년도를 문자열로 변환
    data4['년도'] = data4['년도'].astype(str)
    return data4

data4 = load_data4(file_path4)

with tab1:
    # Plotly를 이용한 꺾은선 그래프
    fig = px.line(data, x='년도', y='순이동 인구수', title='2001년~2023년 대전시 순이동 변화', markers=True)
    
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
    # 두 번째 탭에만 적용되는 multiselect
    side_option_tab2 = st.multiselect(
        label='대전시 지역을 선택하세요',
        options=['강원특별자치도', '경기도', '경상남도', '경상북도', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '서울특별시', '세종특별자치시', '울산광역시', '인천광역시', '전라남도', '전북특별자치도', '제주특별자치도', '충청남도', '충청북도'],
        placeholder='지역 선택'
    )
    
    # 선택된 지역이 있을 경우 데이터 필터링
    if side_option_tab2:
        filtered_data2 = data2[data2['지역'].isin(side_option_tab2)]
    else:
        filtered_data2 = data2

    # Plotly를 이용한 꺾은선 그래프
    fig = px.line(filtered_data2, x='년도', y='순이동 인구수', color='지역', title=f'2001년~2023년 대전시 지역별 순이동 변화', markers=True)
    
    # x축의 모든 연도를 표시하도록 수정
    fig.update_xaxes(tickmode='linear', tick0=filtered_data2['년도'].min(), dtick=1)
    
    # y축의 간격을 5,000 단위로 설정
    fig.update_yaxes(tick0=0, dtick=5000)
    
    # 그래프 커스터마이징 (선택 사항)
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_title='년도', yaxis_title='순이동 인구수')
    
    # Streamlit에서 Plotly 그래프를 표시
    st.plotly_chart(fig)
    
    # 데이터 확인
    st.table(filtered_data2.groupby(['년도', '지역'])['순이동 인구수'].sum().reset_index())

with tab3:
    # Plotly를 이용한 꺾은선 그래프
    fig = px.line(data3, x='년도', y='순이동 인구수', title='2001년~2023년 세종시 순이동 변화', markers=True)
    
    # x축의 모든 연도를 표시하도록 수정
    fig.update_xaxes(tickmode='linear', tick0=data3['년도'].min(), dtick=1)
    
    # y축의 간격을 5,000 단위로 설정
    fig.update_yaxes(tick0=0, dtick=5000)
    
    # 그래프 커스터마이징 (선택 사항)
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_title='년도', yaxis_title='순이동 인구수')
    
    # Streamlit에서 Plotly 그래프를 표시
    st.plotly_chart(fig)
    
    # 데이터 확인
    st.table(data3)

with tab4:
    # 네 번째 탭에만 적용되는 multiselect
    side_option_tab4 = st.multiselect(
        label='세종시 지역을 선택하세요',
        options=['강원특별자치도', '경기도', '경상남도', '경상북도', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '서울특별시', '세종특별자치시', '울산광역시', '인천광역시', '전라남도', '전북특별자치도', '제주특별자치도', '충청남도', '충청북도'],
        placeholder='지역 선택'
    )

    # 선택된 지역이 있을 경우 데이터 필터링
    if side_option_tab4:
        filtered_data4 = data4[data4['지역'].isin(side_option_tab4)]
    else:
        filtered_data4 = data4

    # Plotly를 이용한 꺾은선 그래프
    fig = px.line(filtered_data4, x='년도', y='순이동 인구수', color='지역', title=f'2001년~2023년 세종시 지역별 순이동 변화', markers=True)
    
    # x축의 모든 연도를 표시하도록 수정
    fig.update_xaxes(tickmode='linear', tick0=filtered_data4['년도'].min(), dtick=1)
    
    # y축의 간격을 5,000 단위로 설정
    fig.update_yaxes(tick0=0, dtick=5000)
    
    # 그래프 커스터마이징 (선택 사항)
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_title='년도', yaxis_title='순이동 인구수')
    
    # Streamlit에서 Plotly 그래프를 표시
    st.plotly_chart(fig)
    
    # 데이터 확인
    st.table(filtered_data4.groupby(['년도', '지역'])['순이동 인구수'].sum().reset_index())
