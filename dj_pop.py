import streamlit as st
import pandas as pd
import plotly.express as px

# Tabs for different views
tab1, tab2, tab3, tab4 = st.tabs(['대전시 년도별 순이동', '대전시 년도별·지역별 순이동', '세종시 년도별 순이동', '세종시 년도별·지역별 순이동'])

# GitHub raw content URL's data.csv file paths
file_path = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data.csv'
file_path2 = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data2.csv'
file_path3 = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data3.csv'
file_path4 = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data4.csv'

# Caching the data loading process
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='cp949')
    data['년도'] = data['년도'].astype(str)  # Convert year to string
    return data

# Load data files
data = load_data(file_path)
data2 = load_data(file_path2)
data3 = load_data(file_path3)
data4 = load_data(file_path4)

# Sidebar for global filter selection
with st.sidebar:
    st.title('Filter Options')
    side_option = st.multiselect(
        label='Select regions',
        options=['강원특별자치도', '경기도', '경상남도', '경상북도', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '서울특별시', '세종특별자치시', '울산광역시', '인천광역시', '전라남도', '전북특별자치도', '제주특별자치도', '충청남도', '충청북도'],
        placeholder='Select regions to filter'
    )

with tab1:
    fig = px.line(data, x='년도', y='순이동 인구수', title='2001년~2023년 대전시 순이동 변화', markers=True)
    fig.update_xaxes(tickmode='linear', tick0=data['년도'].min(), dtick=1)
    fig.update_yaxes(tick0=0, dtick=5000)
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_title='년도', yaxis_title='순이동 인구수')
    st.plotly_chart(fig)
    st.table(data)

with tab2:
    if side_option:
        filtered_data2 = data2[data2['지역'].isin(side_option)]
    else:
        filtered_data2 = data2
    fig = px.line(filtered_data2, x='년도', y='순이동 인구수', color='지역', title='2001년~2023년 대전시 지역별 순이동 변화', markers=True)
    fig.update_xaxes(tickmode='linear', tick0=filtered_data2['년도'].min(), dtick=1)
    fig.update_yaxes(tick0=0, dtick=5000)
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_title='년도', yaxis_title='순이동 인구수')
    st.plotly_chart(fig)
    st.table(filtered_data2.groupby(['년도', '지역'])['순이동 인구수'].sum().reset_index())

with tab3:
    fig = px.line(data3, x='년도', y='순이동 인구수', title='2001년~2023년 세종시 순이동 변화', markers=True)
    fig.update_xaxes(tickmode='linear', tick0=data3['년도'].min(), dtick=1)
    fig.update_yaxes(tick0=0, dtick=5000)
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_title='년도', yaxis_title='순이동 인구수')
    st.plotly_chart(fig)
    st.table(data3)

with tab4:
    if side_option:
        filtered_data4 = data4[data4['지역'].isin(side_option)]
    else:
        filtered_data4 = data4
    fig = px.line(filtered_data4, x='년도', y='순이동 인구수', color='지역', title='2001년~2023년 세종시 지역별 순이동 변화', markers=True)
    fig.update_xaxes(tickmode='linear', tick0=filtered_data4['년도'].min(), dtick=1)
    fig.update_yaxes(tick0=0, dtick=5000)
    fig.update_traces(line=dict(width=2))
    fig.update_layout(xaxis_title='년도', yaxis_title='순이동 인구수')
    st.plotly_chart(fig)
    st.table(filtered_data4.groupby(['년도', '지역'])['순이동 인구수'].sum().reset_index())
