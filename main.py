import font_init
import matplotlib.pyplot as plt
from load_data import load_covid


def main():

    # 전체 데이터 가져올때
    # df_covid = load_covid()
    # plt.bar(df_covid.index[1:], df_covid['누적(명)'][1:], align='center')
    # plt.show()

    # df_covid = load_covid(['2020.1.20'])
    # print(df_covid)

    df_covid = load_covid(['2020.1.20', '2020.2.23'])
    print(df_covid)


main()