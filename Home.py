import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from st_pages import Page, show_pages, add_page_title
from sleep_disorder_module import *
from sleep_disorder_module1 import *
import matplotlib.pyplot as plt
from matplotlib import rc

# side bar: pages link
show_pages(
    [
        Page("Home.py", "Home", "🏠"),
        Page("Data.py", "Sleep's Data", "🪧"),
        Page("LifeStyle.py", "Sleep for LifeStyle", "☀️")
    ]
)

# title
st.title("건강한 수면 위한 라이프스타일 지침서 🛌")
st.caption('I want sleep....💤')
st.image('intro.jpg')
st.header("건강하지 못한 수면")
st.text("""현대 사회에서는 바쁜 일상과 스트레스로 인해 충분한 수면을 취하기 어려운 경우가 많습니다. 수면 부족은 다양한
신체적, 정신적 문제를 초래할 수 있습니다. 충분한 수면을 취하지 못하면 신진대사가 감소하여 체중 증가와 비만의
위험을 증가시킬 수 있습니다. 또한 혈압 상승, 심혈관 질환, 당뇨병 등의 질병 위험도 증가할 수 있습니다.  
""")

st.header("건강한 수면의 중요성")
st.text("""수면은 우리 건강에 있어서 매우 중요한 역할을 합니다. 충분한 수면을 취하면 신체의 기능과 회복력이 향상되어
건강을 유지하는 데 도움이 되며 신체 대사에도 긍정적인 영향을 줍니다. 또한 정신적인 안정과 감정 조절이 강화되어
정신질환을 예방하는데 도움이 되고 학습 능력과 기억력이 향상되기도 합니다. 충분한 수면을 취하는 것은 우리의
건강을 위해 매우 중요합니다. 일반적으로 성인은 하루에 7~9시간의 수면을 취하는 것이 권장됩니다.
""")


# main_text1
st.divider()
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

# 막대 그래프 그리기
fig, ax = plt.subplots()
ax.bar(df['진료년도'], df['진료인원합계(명)'], edgecolor='black')

# y축 범위 설정
y_min = 0
y_max = "800000"
ax.set_ylim(y_min, y_max)  

# 마커 추가
ax.plot(df['진료년도'], df['진료인원합계(명)'], marker='o', markersize=5, color='red', linestyle='-', linewidth=1, label='진료인원합계(명)')

# 그래프 제목 및 축 레이블 설정
ax.set_title('수면장애로 진료받는 인원 수')
ax.set_xlabel('진료년도')
ax.set_ylabel('진료인원수(명)')
# 범례 추가
ax.legend()

st.title("최근 5년간 수면장애로 진료를 받은 인원")
st.text("""자료기간:2017년~2022년
조사연령:20대~80대이상
조사지역:전국
        """)

# 그래프를 streamlit에서 표시
st.pyplot(fig)

st.header("나날이 증가하는 수면장애")
st.text("""국민건강보험공단에서 조사한 데이터를 확인해보면 최근 5년간 수면장애로 진료를 받은 인원이 증가하고있다.
해당 자료는 전국을 대상으로 20대부터 80대 이상의 연령을 조사하였다. 연령으로는 확인해보면 50대 이상이
수면 장애로 인한 진료를 많이 받았다는 수치를 알 수 있다.
""")


# 모듈에서 데이터프레임 로드
df = load_sleep_data1()

# 그래프 폰트 설정
rc('font', family='GyeonggiTitle')

# 막대 그래프 그리기
fig, ax = plt.subplots()
ax.bar(df['연령'], df['진료인원합계(명)'], edgecolor='black')

# y축 범위 설정
y_min = 0
y_max = "900000"
ax.set_ylim(y_min, y_max)  

# 마커 추가
ax.plot(df['연령'], df['진료인원합계(명)'], marker='o', markersize=5, color='red', linestyle='-', linewidth=1, label='진료인원합계(명)')

# 그래프 제목 및 축 레이블 설정
ax.set_title('수면장애로 진료받는 연령별 인원')
ax.set_xlabel('연령')
ax.set_ylabel('진료인원수(명)')
# 범례 추가
ax.legend()

# 그래프를 streamlit에서 표시
st.pyplot(fig)


# main_text2
st.divider()
st.image('intro1.jpg')
st.header("일상의 파괴자, 수면장애")
st.link_button("Click news 🗞️", "https://news.sbs.co.kr/news/endPage.do?news_id=N1007565525&plink=SHARE&cooper=COPY")
txt = st.text_area(
    "preview",
    "'수면장애 사회' 대한민국 "
    "인생의 3분의 1을 차지하는 수면. 그만큼 일상생활을 유지하는 데 중요한 부분을 차지하고 있지만, "
    "날이 갈수록 수면장애를 겪는 환자들은 늘어나는 추세다. "
    "국민건강보험에 따르면 2022년 수면장애 진료 인원은 109만 8천819명으로 110만 명에 육박했다...."
    )

# main_text3
st.divider()
st.image('intro2.jpg')
st.header("‘잠 못드는 현대인’ 수면장애 116만명 돌파…50대 이상 가장 많아")
st.link_button("Click news 🗞️", "http://www.mkhealth.co.kr/news/articleView.html?idxno=65984")
txt = st.text_area(
    "preview",
    "지난해 수면장애로 진료받은 사람이 116만명을 넘어선 것으로 나타났다. "
    "의료계에서는 매년 증가하는 수면장애 환자와 진료비를 줄이기 위해 국가차원의 관심과 지원이 중요하다고 강조한다. "
    "수면이 부족하면 만성피로, 두통, 인지기능 저하, 치매 발생 위험도 증가할 수 있다는 연구 결과가 발표되면서 중요성이 커지고 있다. ...."
    )