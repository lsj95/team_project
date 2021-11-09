import numpy as np
import pandas as pd
from load_data import load_nurse


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

