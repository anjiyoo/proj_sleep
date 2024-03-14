# 데이터 처리를 위한 함수 정의
import numpy as np
import pandas as pd

def load_sleep_data1():
    # 파일 가져오기
    df = pd.read_csv('sleep_disorder.csv', encoding='cp949')

    # 열 삭제
    columns_to_drop = ['주상병코드', '시도', '시군구', '진료년도']
    df = df.drop(columns_to_drop, axis=1)

    # '진료인원(명)' 열에서 NaN 값 변경 (NaN -> 0)
    df['진료인원(명)'].fillna("0", inplace=True)

    # 2017년 ~ 2022년 수면장애 필터링
    df.drop(df.index[0:44254], inplace=True)

    # 진료인원(명) 열의 값에서 쉼표(,) 제거
    df['진료인원(명)'] = df['진료인원(명)'].str.replace(',', '')

    # 10대 미만, 10대 연령별 데이터 필터링
    df = df[~df['연령'].isin(['10대 미만', '10대'])]

    # 진료년도가 2017인 진료인원(명)의 값을 모두 더하여 진료인원합계(명) 열에 할당
    df.loc[df['연령'] == '20대', '진료인원합계(명)'] = df[df['연령'] == '20대']['진료인원(명)'].astype(int).sum()
    df.loc[df['연령'] == '30대', '진료인원합계(명)'] = df[df['연령'] == '30대']['진료인원(명)'].astype(int).sum()
    df.loc[df['연령'] == '40대', '진료인원합계(명)'] = df[df['연령'] == '40대']['진료인원(명)'].astype(int).sum()
    df.loc[df['연령'] == '50대', '진료인원합계(명)'] = df[df['연령'] == '50대']['진료인원(명)'].astype(int).sum()
    df.loc[df['연령'] == '60대', '진료인원합계(명)'] = df[df['연령'] == '60대']['진료인원(명)'].astype(int).sum()
    df.loc[df['연령'] == '70대', '진료인원합계(명)'] = df[df['연령'] == '70대']['진료인원(명)'].astype(int).sum()
    df.loc[df['연령'] == '80대 이상', '진료인원합계(명)'] = df[df['연령'] == '80대 이상']['진료인원(명)'].astype(int).sum()

    # 열 삭제
    columns_to_drop = ['진료인원(명)']
    df = df.drop(columns_to_drop, axis=1)

    # 진료인원합계(명) int로 변환
    df['진료인원합계(명)'] = df['진료인원합계(명)'].astype(int)

    # 진료인원합계(명)열의 값을 문자열로 변환
    df['진료인원합계(명)'] = df['진료인원합계(명)'].astype(str)

    # 중복되는 값 제거
    df.drop_duplicates(inplace=True)

    return df

print(load_sleep_data1())