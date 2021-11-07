import pandas as pd
import numpy as np


def load_covid(period=None): # 도별 확진환자수 데이터 로드
    missing_values = ['--', '-', 'na'] #nan값 설정

    df_covid = pd.read_csv('./resource/코로나바이러스감염증-19_확진환자_발생현황_211103.csv', index_col='일자',
                           na_values=missing_values)
    df_covid = df_covid.transpose().fillna("0") # rows 지역, columns 일자로 전치함
    df_covid = df_covid.apply(lambda x: x.apply(lambda y:y.replace(",",""))).astype(np.int64) # 데이터프레임 내부의 모든값을 숫자로 바꿈

    if period == None:
        return df_covid
    elif len(period) == 1: #하루만 보는 경우
        print(period)
        return df_covid[period[0]]
    else:
        tmp_df = df_covid.loc[:,period[0]:period[1]]
        tmp_df['기간 총합'] = tmp_df.sum(axis=1) # Warning 확인해볼 필요가 있음
        return tmp_df


def load_hospital(): # 도별 병원수 데이터 로드
    missing_values = ['--', '-', 'na']  # nan값 설정

    df_hospital = pd.read_csv('./resource/건강보험심사평가원_의료기관별 감염병 및 중증환자 치료시설 현황_20210630.csv', index_col='시도명',
                              na_values=missing_values)
    df_hospital = df_hospital.groupby('시도명').agg(sum)
    df_hospital['총 병상수'] = df_hospital.sum(axis=1)

    # covid 데이터 프레임과 인덱스명 통일시킴
    name_match = {'강원도':'강원','경기도':'경기','경상남도':'경남','경상북도':'경북','광주광역시':'광주','대구광역시':'대구',
                  '대전광역시':'대전','부산광역시':'부산','서울특별시':'서울','세종특별자치시':'세종','울산광역시':'울산',
                  '인천광역시':'인천','전라남도':'전남','전라북도':'전북','제주특별자치도':'제주','충청남도':'충남','충청북도':'충북'}
    df_hospital = df_hospital.rename(index=name_match)

    return df_hospital

