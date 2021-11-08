import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import font_init
from load_data import load_covid
# % matplotlib qt




df = load_covid(['2020.1.20', '2020.2.23'])

fig = plt.figure(figsize=(8, 6))
axes = fig.add_subplot(1, 1, 1)
axes.set_ylim(0, 1000)
plt.style.use('seaborn')


def animate(i):
    plt.bar(df.index, df.iloc[:, i], color='blue')
    plt.title('Day : {}'.format(df.columns[i]))


ani = FuncAnimation(fig, animate, interval=100)