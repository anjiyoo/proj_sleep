import numpy as np
import pandas as pd
from data_module import *
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc
import streamlit as st

# 모듈에서 데이터프레임 로드
df = load_sleep_data()

# 데이터프레임 출력
# print(df)

# 컴퓨터 폰트 확인
# for font in fm.fontManager.ttflist:
#     print(font)
#     if '한글' in font.name or 'Korean' in font.name:
#         print(font.name)

# 그래프 폰트 설정
rc('font', family='GyeonggiTitle')



# x, y축 데이터
x = df['진료년도']
y = df['진료인원(명)'].astype(int)

# 선 그래프 그리기
plt.plot(x, y)

# 그래프 제목과 축 레이블 설정
plt.title('2017년부터 2022년까지 수면장애로 진료를 받은 인원')
plt.xlabel('진료년도')
plt.ylabel('진료인원(명)')

# y축 눈금 설정
plt.yticks(range(0, max(y)+1, 500))

# 그래프 출력
plt.show()
