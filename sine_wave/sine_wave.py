""" sample animation """
import math
import matplotlib.animation as anm
import matplotlib.pyplot as plt
import numpy as np

FRAME_NUM = 75                          # 30fps なので2.5秒で1周期

def draw():
    """
    描画情報設定しファイルへ保存する
    """
    fig = plt.figure(figsize=(5, 3))    # 5x3 inchの図を準備
    ani = anm.FuncAnimation(fig, update, fargs=('Sine wave ', 2.0), interval=33, frames=FRAME_NUM)
    ani.save("sine_wave.gif", writer='imagemagick')

def update(i, fig_title, amplitude):
    """
    フレームごとの描画
    """
#    if i != 0:
#        plt.cla()                      # Axesをクリア
    x_s = np.arange(0, 10, 0.1)         # 初項0, 公差0.1, 終点10の等差数列
    y_s = amplitude * np.sin(x_s-i*2*math.pi/FRAME_NUM)
    plt.plot(x_s, y_s, "r")
    plt.title(fig_title + 'i=' + str(i))
#    plt.savefig("fig.png")

if __name__ == '__main__':
    draw()
