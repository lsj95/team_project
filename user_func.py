import numpy as np
import pandas as pd
from load_data import load_nurse, load_hospital_bed


def nurse_diff(quarter_list): # 분기 2가지를 입력받아서 2개의 차이를 구해줌 예시 ['2020-1','2020-2']

    tmp_df = load_nurse(quarter_list[0], '시도별')
    tmp_df2 = load_nurse(quarter_list[1], '시도별')

    df_diff = tmp_df2 - tmp_df
    df_diff = df_diff.rename(columns={'간호사':'간호사 변동(명)', '간호조무사':'간호조무사 변동(명)','합계':'지역 총 변동(명)'})

    df_diff_percent = (tmp_df2 / tmp_df) - 1 # 기존 분기 대비 변화 퍼센트 / 양수-증가, 음수-감소
    df_diff_percent = df_diff_percent.rename(columns={'간호사':'간호사 변화율', '간호조무사':'간호조무사 변화율','합계':'지역 총 변화율'})

    # 데이터 프레임 합치고 순서만 좀 정렬함
    df_diff_all = pd.concat([df_diff,df_diff_percent], axis=1)
    df_diff_all = df_diff_all[['간호사 변동(명)','간호사 변화율','간호조무사 변동(명)','간호조무사 변화율', '지역 총 변동(명)','지역 총 변화율']]

    return df_diff_all


def hospital_bed_diff(): #8월 병상수 -> 11월 병상수 변화량 구하는 함수
    tmp_df = load_hospital_bed(0) #첫번째 데이터 로드
    tmp_df2 = load_hospital_bed(1) #두번째 데이터 로드

    columns_1_2 = tmp_df[['수도권 여부','상세 지역']] #앞부분만 따로 붙히려고
    hospital_bed_diff = tmp_df2.iloc[:,2:] - tmp_df.iloc[:,2:] # 숫자끼리만 연산

    df_hospital_bed_diff = pd.concat([columns_1_2,hospital_bed_diff], axis=1)

    return df_hospital_bed_diff #최종적으로 8월에서 10월 병상수 변화량을 보여줌
