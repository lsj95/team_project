import font_init
import matplotlib.pyplot as plt
from load_data import load_covid, load_hospital


def main():

    # 전체 데이터 가져올때
    # df_covid = load_covid()
    # plt.bar(df_covid.index[1:], df_covid['누적(명)'][1:], align='center')
    # plt.show()

    # 특정 날짜만 데이터 가져올때
    # df_covid = load_covid(['2020.1.20'])
    # print(df_covid)

    #기간에 대한 데이터 가져올때 Warning은 확인 필요함
    df_covid = load_covid(['2020.1.20', '2020.2.23'])
    print(df_covid)

    df_hospital = load_hospital()
    print(df_hospital)


main()