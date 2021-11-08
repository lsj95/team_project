import font_init
import matplotlib.pyplot as plt
from load_data import load_covid, load_hospital, load_nurse


def main():

    # 그냥 임시로 만든 함수들 적어놓음
    # 나중에는 main 안에 데이터 로드하고 plot 그리는 것만

    ## 전체 데이터 가져올때
    print('1')
    df_covid = load_covid()
    print(df_covid)
    plt.bar(df_covid.index[1:], df_covid['누적(명)'][1:], align='center')
    plt.show()

    print('2')
    ## 특정 날짜만 데이터 가져올때
    df_covid = load_covid(['2020.1.20'])
    print(df_covid)

    print('3')
    ## 기간에 대한 데이터 가져올때 Warning은 확인 필요함
    df_covid = load_covid(['2020.1.20', '2020.2.23'])
    print(df_covid)

    print('4')
    ## 시도별 병원수 가져오는 함수
    df_hospital = load_hospital()
    print(df_hospital)

    print('5')
    ## 간호사 데이터 가져오기 case 1 병원까지 나오는거
    df_nurse = load_nurse('2019-1')
    print(df_nurse)

    print('6')
    ## 간호사 데이터 가져오기 case 2
    df_nurse = load_nurse('2019-1','시도별')
    print(df_nurse)


main()