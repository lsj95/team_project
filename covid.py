import pandas as pd
import numpy as np


def load_covid():
    missing_values = ['--', '-', 'na'] #nan값 설정

    df_covid = pd.read_csv('./resource/코로나바이러스감염증-19_확진환자_발생현황_211103.csv', index_col='일자', na_values=missing_values)
    df_covid = df_covid.transpose().fillna("0") # rows 지역, columns 일자로 전치함
    df_covid = df_covid.apply(lambda x: x.apply(lambda y:y.replace(",",""))).astype(np.int64) # 데이터프레임 내부의 모든값을 숫자로 바꿈

    return df_covid