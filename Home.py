# 1. 수면 장애는 현대인이 앓고 있는 고질병
# - 세계 수면의 날 
# - 수면 장애의 위험 고지 (image/news link)

import streamlit as st
from streamlit_option_menu import option_menu
from st_pages import Page, show_pages

# side bar: pages link
show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Page("sleep_data.py", "Sleep's Data", "🪧"),
        Page("lifestyle.py", "Sleep for LifeStyle", "☀️")
    ]
)

# title
st.title("2024 World Sleep Day")
st.caption('Sleep Equity for Global Health. by_WASM')
st.image('home_sleepday.jpg')
st.caption('URL: https://www.sleepnet.or.kr/board/notice/686')
st.subheader("2024년 3월 15일 세계 수면의 날")
st.text("""세계수면학회(WASM)가 수면에 대한 올바른 이해와 수면질환 예방 및 관리의 중요성을 알려, 수면장애 질환으로 인한
사회적 관심을 환기시키고 질병 부담등을 줄이고자 2007년에 제정한 날로 매년 3월 우리나라를 비롯한 세계 70여개
회원국에서 기념 행사를 진행하고 있다.
""")

st.divider()  # 구분선

# page title
st.header("수면장애는 현대인의 고질병")

# page main
st.image('home_image1.jpg')
st.subheader("‘잠 못드는 현대인’ 수면장애 116만명 돌파…50대 이상 가장 많아")
st.caption('작성: 2023.10.02 ')
st.link_button("Click news 🗞️", "http://www.mkhealth.co.kr/news/articleView.html?idxno=65984")
txt = st.text_area(
    "preview",
    "지난해 수면장애로 진료받은 사람이 116만명을 넘어선 것으로 나타났다. 국민건강보험공간에서 조사한 수면장애,: "
    "비기질성 수면장애 진료현황 자료에 따르면 2018년 91만 606명에서 2020년 103만 7279명으로 증가하면서 "
    "처음으로 100만명을 넘어섰다. 특히 이중 50대 이상 중장년층이 전체 인원의 70%에 달해....")

st.image('home_image2.jpg')
st.subheader("일상의 파괴자, 수면장애")
st.caption('작성: 2024.03.09')
st.link_button("Click news 🗞️", "https://news.sbs.co.kr/news/endPage.do?news_id=N1007565525&plink=SHARE&cooper=COPY")
txt = st.text_area(
    "preview",
    "'수면장애 사회' 대한민국 "
    "인생의 3분의 1을 차지하는 수면. 그만큼 일상생활을 유지하는 데 중요한 부분을 차지하고 있지만, "
    "날이 갈수록 수면장애를 겪는 환자들은 늘어나는 추세다. "
    "국민건강보험에 따르면 2022년 수면장애 진료 인원은 109만 8천819명으로 110만 명에 육박했다...."
)


