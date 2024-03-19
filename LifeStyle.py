# 3. 건강한 수면을 위한 생활습관
#  - 대한수면연구학회에서 건강한 수면을 10계명 CheckList로 사용자가 직접 체크해볼 수 있도록 제작

import streamlit as st

# page title
st.title("건강한 수면 위한 라이프스타일 지침서 🛌")
st.caption('URL: https://www.sleepnet.or.kr/sleep/commandment')
st.image('lifestyle_image.jpg')

st.header("건강한 수면을 위한 첫 번째 걸음 ☀️")
st.subheader("건강한 수면을 위한 생활습관 Check List 🔖")

# Check List
ch1 = st.checkbox('1. 잠자리에 드는 시간과 아침에 일어나는 시간을 규칙적으로 하기')
ch2 = st.checkbox("2. 잠자리에 소음을 없애고, 온도와 조명을 안락하게 하기")
ch3 = st.checkbox("3. 낮잠은 피하고 자더라도 15분 이내로 제한하기")
ch4 = st.checkbox("4. 낮에 40분 동안 땀이 날 정도의 운동하기")
ch5 = st.checkbox("5. 카페인이 함유된 음식, 알코올 그리고 니코틴 피하기")
ch6 = st.checkbox("6. 잠자기 전 과도한 식사를 피하고 적당한 수분 섭취 하기")
ch7 = st.checkbox("7. 수면제의 일상적 사용을 피하기")
ch8 = st.checkbox("8. 과도한 스트레스와 긴장을 피하고 이완하는 것을 배우기")
ch9 = st.checkbox("9. 잠자리에 누워서 책을 보거나 TV를 보는 것을 피하기")
ch10 = st.checkbox("10. 잠자리에 들어 20분 이내 잠이 오지 않는다면, 잠자리에서 일어나 이완하고 있다가 피곤한 느낌이 들 때 다시 잠자리에 들기")

# Check List -> 메시지
if ch1 and ch2 and ch3 and ch4 and ch5 and ch6 and ch7 and ch8 and ch9 and ch10:
  st.markdown("<h1 style='text-align: center;'>🎉</h1>", unsafe_allow_html=True)
  st.markdown("<h1 style='text-align: center;'>좋아요! 모든 항목을 체크하셨네요</h1>", unsafe_allow_html=True)
  st.markdown("<h2 style='text-align: center;'>건강한 수면을 위해 Check List를 꼭 실천해보세요 😎</h2>", unsafe_allow_html=True)
  st.balloons()



