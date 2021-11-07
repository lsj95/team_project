import font_init
import matplotlib.pyplot as plt
from covid import load_covid


def main():
    df_covid = load_covid()
    plt.bar(df_covid.index[1:], df_covid['누적(명)'][1:], align='center')
    plt.show()


main()