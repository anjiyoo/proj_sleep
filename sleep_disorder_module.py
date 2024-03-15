# 데이터 처리를 위한 함수 정의
import numpy as np
import pandas as pd

def load_sleep_data():
    # 파일 가져오기
    df = pd.read_csv('sleep_disorder.csv', encoding='cp949')

    # 열 삭제
    columns_to_drop = ['주상병코드', '시도', '시군구', '연령']
    df = df.drop(columns_to_drop, axis=1)

    # '진료인원(명)' 열에서 NaN 값 변경 (NaN -> 0)
    df['진료인원(명)'].fillna("0", inplace=True)

    # 2017년 ~ 2022년 수면장애 필터링
    df.drop(df.index[0:44254], inplace=True)

    # 진료년도열의 값에서 '년' 글자 제거
    df['진료년도'] = df['진료년도'].str.replace('년', '')

    # 진료인원(명) 열의 값에서 쉼표(,) 제거
    df['진료인원(명)'] = df['진료인원(명)'].str.replace(',', '')

    # 진료년도가 2017인 진료인원(명)의 값을 모두 더하여 진료인원합계(명) 열에 할당
    df.loc[df['진료년도'] == '2017', '진료인원합계(명)'] = df[df['진료년도'] == '2017']['진료인원(명)'].astype(int).sum()
    df.loc[df['진료년도'] == '2018', '진료인원합계(명)'] = df[df['진료년도'] == '2018']['진료인원(명)'].astype(int).sum()
    df.loc[df['진료년도'] == '2019', '진료인원합계(명)'] = df[df['진료년도'] == '2019']['진료인원(명)'].astype(int).sum()
    df.loc[df['진료년도'] == '2020', '진료인원합계(명)'] = df[df['진료년도'] == '2020']['진료인원(명)'].astype(int).sum()
    df.loc[df['진료년도'] == '2021', '진료인원합계(명)'] = df[df['진료년도'] == '2021']['진료인원(명)'].astype(int).sum()
    df.loc[df['진료년도'] == '2022', '진료인원합계(명)'] = df[df['진료년도'] == '2022']['진료인원(명)'].astype(int).sum()

    # 열 삭제
    columns_to_drop = ['진료인원(명)']
    df = df.drop(columns_to_drop, axis=1)

    # 진료인원합계(명) int로 변환
    df['진료인원합계(명)'] = df['진료인원합계(명)'].astype(int)

    # 중복되는 값 제거
    df.drop_duplicates(inplace=True)

    # 데이터를 텍스트 파일로 저장
    # df.to_csv('sleep_data.txt', sep='\t', index=False)

    return df

print(load_sleep_data())
