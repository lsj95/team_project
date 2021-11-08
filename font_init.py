import platform
import matplotlib.pyplot as plt

# seaborn 그릴때 폰트 없어서 글자 깨지는거 방지
if platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False
elif platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')