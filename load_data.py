import pandas as pd
import numpy as np


def load_covid(period=None):
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

def load_hospital():
    pass



