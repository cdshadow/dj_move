import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import requests
from io import BytesIO

# GitHub에 업로드된 맑은고딕 폰트 파일 경로
font_url = "https://raw.githubusercontent.com/cdshadow/dj_move/main/malgun.ttf"

# 폰트 파일 다운로드 및 설정
response = requests.get(font_url)
if response.status_code == 200:
    font_file = BytesIO(response.content)
    
    # 폰트 임시 저장 및 설정
    with open("/tmp/malgun.ttf", "wb") as f:
        f.write(font_file.getbuffer())
    font_name = font_manager.FontProperties(fname="/tmp/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    st.write("폰트 파일을 로드하는 데 실패했습니다.")

# GitHub raw content URL의 data.csv 파일 경로
file_path = 'https://raw.githubusercontent.com/cdshadow/dj_move/main/data.csv'

# 데이터를 캐시하여 로딩
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='cp949')
    return data

data = load_data(file_path)

# 2001년~2023년 대전시 순이동 데이터에 대한 꺾은선 그래프
st.write("2001년~2023년 대전시 순이동")

# Seaborn을 이용한 꺾은선 그래프
plt.figure(figsize=(10, 6))
sns.lineplot(x='년도', y='순이동 인구수', data=data, marker='o')
plt.title('2001년~2023년 대전시 순이동 변화')
plt.xlabel('년도')
plt.ylabel('순이동 인구수')
plt.xticks(rotation=45)  # x축 레이블이 겹치지 않도록 회전
plt.grid(True)

# Streamlit에서 그래프를 표시
st.pyplot(plt)

# 데이터 확인
st.write("2001년~2003년 대전시 순이동 인구수")
st.table(data)
