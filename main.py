import sys
from application import *
import matplotlib.pyplot as plt


def graph_fc(x1, x2, vca0, vca1, vcb0, vcb1):
    X = [0, x1, x1, x1 + x2]
    Y = [vca0, vca1, vcb0, vcb1]
    plt.title("Força cortante")
    plt.xlabel("Tamanho em metros")
    plt.plot(X, Y)
    plt.show()

def graph_mf(x1, x2, mca0, mca1, mcb0, mcb1):
    X = [0, x1, x1, x1 + x2]
    Y = [mca0, mca1, mcb0, mcb1]
    plt.title("Momento fletor")
    plt.xlabel("Tamanho em metros")
    plt.plot(X, Y)
    plt.show()


if __name__ == '__main__':

    qt= QApplication(sys.argv)
    app = Aplicacao()
    app.show()
    qt.exec()

    vca0 = 500
    vca1 = 475
    vcb0 = 200
    vcb1 = 195
    x1 = 10
    x2 = 2

    graph_fc(x1, x2, vca0, vca1, vcb0, vcb1)

