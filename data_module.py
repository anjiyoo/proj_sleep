# 데이터 처리를 위한 함수 정의
import numpy as np
import pandas as pd

def load_sleep_data():
    # 파일 가져오기
    df = pd.read_csv('sleep_disorder.csv', encoding='cp949')

    # 열 삭제
    columns_to_drop = ['주상병코드', '시도', '시군구']
    df = df.drop(columns_to_drop, axis=1)

    # '진료인원(명)' 열에서 NaN 값 변경 (NaN -> 0)
    df['진료인원(명)'].fillna("0", inplace=True)

    # 2017년 ~ 2022년 수면장애 필터링
    df.drop(df.index[0:44254], inplace=True)

    # 10대 미만, 10대 연령별 데이터 필터링
    df = df[~df['연령'].isin(['10대 미만', '10대'])]

    # 진료년도열의 값에서 '년' 글자 제거
    df['진료년도'] = df['진료년도'].str.replace('년', '')

    # 진료인원(명) 열의 값에서 쉼표(,) 제거
    df['진료인원(명)'] = df['진료인원(명)'].str.replace(',', '')

    # 데이터를 텍스트 파일로 저장
    # df.to_csv('sleep_data.txt', sep='\t', index=False)

    return df

# print(load_sleep_data())

def aggregate_sleep_data(df):
    # 진료연도별 같은 연령의 진료인원(명) 값을 더해서 중복되는 값을 없애는 작업
    df_agg = df.groupby(['진료년도', '연령'])['진료인원(명)'].sum().reset_index()

    return df_agg

# 데이터를 로드하고 전처리한 후의 DataFrame을 가져오기
df = load_sleep_data()

# 진료연도별 같은 연령의 진료인원(명) 값을 더해서 중복되는 값을 없앤 DataFrame
def aggregate_sleep_data(df):
    df['진료인원(명)'].fillna(0, inplace=True)  # NaN 값을 0으로 대체
    
    # 진료연도별 같은 연령의 진료인원(명) 값을 더해서 중복되는 값을 없애는 작업
    df['진료인원(명)'] = df['진료인원(명)'].astype(int)  # 진료인원(명) 열의 값을 정수형으로 변환
    df_agg = df.groupby(['진료년도', '연령'])['진료인원(명)'].sum().reset_index()
    df['진료인원(명)'] = df['진료인원(명)'].astype(str)  # 진료인원(명) 열의 값을str로 변환
    return df_agg

df_agg = aggregate_sleep_data(df)

print(df_agg)