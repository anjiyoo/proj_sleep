# 2. 수면 장애를 겪는 현대인들
# - 수면 장애/비기질성수면장애 진료인원 데이터세트 활용
# - 현대인의 수면 장애 진료인원을 진료년도&연령별로 데이터 시각화
# - 수면 장애를 일으키는 요인을 보기 쉬운 이미지로 표현

import matplotlib.pyplot as plt
from matplotlib import rc
from sleep_disorder_module import *
from sleep_disorder_module1 import *
import streamlit as st

# page title
st.title("건강하지 못한 수면 🥊 건강한 수면")
st.caption('I want sleep....💤')
st.image('data_image.jpg')
st.markdown("<h3> 건강하지 못한 수면 </h3>", unsafe_allow_html=True)
st.text("""현대 사회에서는 바쁜 일상과 스트레스로 인해 충분한 수면을 취하기 어려운 경우가 많습니다. 수면 부족은 다양한
신체적, 정신적 문제를 초래할 수 있습니다. 충분한 수면을 취하지 못하면 신진대사가 감소하여 체중 증가와 비만의
위험을 증가시킬 수 있습니다. 또한 혈압 상승, 심혈관 질환, 당뇨병 등의 질병 위험도 증가할 수 있습니다.
""")

st.markdown("<h3> 건강한 수면의 중요성 </h3>", unsafe_allow_html=True)
st.text("""수면은 우리 건강에 있어서 매우 중요한 역할을 합니다. 충분한 수면을 취하면 신체의 기능과 회복력이 향상되어
건강을 유지하는 데 도움이 되며 신체 대사에도 긍정적인 영향을 줍니다. 또한 정신적인 안정과 감정 조절이 강화되어
정신질환을 예방하는데 도움이 되고 학습 능력과 기억력이 향상되기도 합니다. 충분한 수면을 취하는 것은 우리의
건강을 위해 매우 중요합니다. 일반적으로 성인은 하루에 7~9시간의 수면을 취하는 것이 권장됩니다.
""")

st.divider()  # 구분선


# page main1
st.header("🗂️ 데이터로 보는 수면 건강")
# 그래프 폰트 설정
rc('font', family='GyeonggiTitle')


# 최근 5년간 수면장애로 진료를 받은 인원 그래프
df = load_sleep_data()  # 데이터 불러오기

fig, ax = plt.subplots()
bars = ax.bar(df['진료년도'], df['진료인원합계(명)'], edgecolor='black', width=0.5) 

colors = ['powderblue', 'deepskyblue', 'steelblue', 'lightslategray']  # 막대 색상
for i, bar in enumerate(bars):
    bar.set_color(colors[i % len(colors)])

ax.set_title('최근 5년간 수면장애 진료를 받은 인원수')
ax.set_xlabel('진료년도')
ax.set_ylabel('진료인원수(명)')
ax.legend()  # 범례
# y축 범위를 변경 (min0 max 1.3)
ax.set_ylim(0, df['진료인원합계(명)'].max() * 1.3)
# y축 레이블을 표시하지 않음
ax.set_yticklabels([])
# 막대 끝에 진료인원합계(명) 수치
ax.bar_label(bars, fmt='%d명', label_type='edge', fontsize=10)

# 데이터 자료 설명
st.markdown("<h3> 1.최근 5년간 수면장애 진료를 받은 인원수 </h3>", unsafe_allow_html=True)
st.text("""자료기간: 2017년~2022년
조사연령: 20대~80대이상
조사지역: 전국""")
st.pyplot(fig)  # 그래프 출력

st.markdown("<h4> 늘어나는 수면장애 진료환자 </h4>", unsafe_allow_html=True)
st.text(""" 수면장애 질환으로는 수면 무호흡증, 불면증, 기면증, 주간졸림증, 사건수면, 일주기 리듬수면장애 등 다양하다.
그 중 가장 흔한 형태의 수면장애는 수면 무호흡증이다. 수면 무호흡증은 잠잘 때 기도가 심하게 좁아져 공기가
기도를 통과하는 것을 막기 때문에 코골이와 함께 발생한다. 좁아진 기도로 숨을 쉬기 위해 횡경막과 가슴근육은
더욱 힘을 주게 되고 결과적으로 잠에서 자주 깬다. 이러한 수면중단은 기도의 근육을 자극하여 기도가 더 좁아지게
되는 악숙한이 반복된다. 하지만 수면중단 시간이 너무 짧아서 다음날 잠에서 깨었을 때 자주 깬 사실을 기억하지
못한다. 대체로 수면 무호흡은 하루 밤에 수십번에서 수백번 정도 발생한다. 
""")
st.text(""" 수면 무호흡증의 원인으로는 신체적인 원인들도 있지만, 생활 습관으로 인한 원인들도 있다.
안좋은 생활 습관으로 체중이 과체중인 경우 목의 지방조직으로 인하여 기도를 좁게 만들게 되는 경우가 흔하며,
비만, 나이가 많은 경우, 남자, 당뇨병, 폐경 여성, 코에 문제가 있는 사람들에서 폐쇄성 수면 무호흡증이 더 많이
발생한다. 술, 수면제, 안정제등은 근육의 긴장도를 더욱 떨어뜨려서 기도가 더 잘 막히게 하기 때문에
수면 무호흡증이 있는 사람은 피하거나 주의하는 것이 좋다.
""")

st.divider()  # 구분선

# 수면장애로 진료를 받은 연령별 인원 그래프
df = load_sleep_data1()  # 데이터 불러오기

fig, ax = plt.subplots()
bars = ax.barh(df['연령'], df['진료인원합계(명)'], edgecolor='black', height=0.5) 

colors = ['palevioletred', 'plum', 'thistle', 'crimson']  # 막대 색상
for i, bar in enumerate(bars):
    bar.set_color(colors[i % len(colors)])

ax.set_title('수면장애 진료를 받은 연령별 인원수')
ax.set_xlabel('진료인원수(명)')
ax.set_ylabel('연령')
ax.legend()  # 범례
# x축 범위를 변경 (min0 max 1.2)
ax.set_xlim(0, df['진료인원합계(명)'].max() * 1.2)
# x축 레이블을 표시하지 않음
ax.set_xticklabels([])
# 막대 끝에 진료인원합계(명) 수치
for bar in bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width}명', ha='left', va='center')

# 데이터 자료 설명
st.markdown("<h3> 2.수면장애 진료를 받은 연령별 인원수 </h3>", unsafe_allow_html=True)
st.text("""자료기간: 2017년~2022년
조사연령: 20대~80대이상
조사지역: 전국""")
st.pyplot(fig)  # 그래프 출력

st.markdown("<h4> 고연령일수록 수면장애가 심해져... </h4>", unsafe_allow_html=True)
st.text("""일반적으로 나이가 들수록 수면장애의 발생 빈도와 심각성이 증가하는 경항이 보인다. 수면장애는 다양한 원인에 의해
발생할 수 있다. 나이가 들면서 생리적인 변화와 건강 상태에 따라 수면에 영향을 미칠 수 있는데 노화 과정에서
수면의 구조와 패턴이 변화하게 되고, 이로인해 수면의 양과 질이 저하될 수 있다. 또한, 노화로 인해 생기는 질환과
건강 문제도 수면에 영향을 줄 수 있는데 만성통증, 호흡기질환, 요통, 폐질환 등은 수면의 질을 저하시킬 수 있다.
""")
st.text("""하지만 모든 노인이 수면장애를 경험하는 것은 아니다. 개인마다 건강 상태와 생활습관 등이 다르기 때문에
수면장애의 정도와 발생 빈도는 다를 수 있다. 수면장애를 경함하지 않으려면 규칙적인 생활습관이 중요하다.
스트레스를 관리하고 건강한 식습관과 규칙적인 운동, 규칙적인 수면 시간 등이 건강한 수면 생활에 도움이 된다.
""")

st.divider()  # 구분선



# page main2
st.header("🧘🏻 수면장애 요인이 되는 생활습관  ")
col1, col2, col3 = st.columns(3)

with col1:
   st.markdown("<h4> 1.체중 BMI 관리 </h4>", unsafe_allow_html=True)
   st.image("https://img.freepik.com/free-photo/person-with-eating-disorder-having-weight-problems_23-2149243010.jpg?t=st=1710490760~exp=1710494360~hmac=ff0674240d5890ace1c26d54a60c6afde60a8fae8d93aab0e6250b597bb99d4f&w=740")

with col2:
   st.markdown("<h4> 2.활동수치 </h4>", unsafe_allow_html=True)
   st.image("https://img.freepik.com/free-photo/young-woman-enjoying-swimming-pool_23-2148700002.jpg?t=st=1710505340~exp=1710508940~hmac=3b8f6e5b71d6b8335f0666991200f956877ff5d5de423f3068bb8bb340afafff&w=740")

with col3:
   st.markdown("<h4> 3.하루 걸음수 </h4>", unsafe_allow_html=True)
   st.image("https://img.freepik.com/free-photo/side-view-man-running-outdoors_23-2149596342.jpg?t=st=1710490809~exp=1710494409~hmac=46114f4d3d663e9e8bf342b747bc1c24cfa3731f26e112ea07e318ad2605a0a5&w=740")

