from layouts.layout import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class Aplicacao(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnCalcular.clicked.connect(self.calcular)

    def calcular(self):
        va, vb, x1, x2 = self.recebe_valores()
        print(f'Va = {va},Vb = {vb}, x1= {x1}')

    def recebe_valores(self):
        va = float(self.vaInput.text())
        vb = float(self.vbInput.text())
        x1 = float(self.x1Input.text())
        x2 = float(self.x2Input.text())

        return va, vb, x1, x2

    def forca_cortante(va, vb, x1, x2):
        vac0 = va - 0  # para x = 0
        vac1 = va - x1  # para x = x1
        vbc0 = vb - 0  # para x = 0
        vbc1 = vb - x2  # para x = 1

        return vac0, vac1, vbc0, vbc1

    def reacoes_de_apoio(va, vb, vc, x1, x2):
        vc = va + vb
        ma = (vc * x1) - (vb * (x2 + x1))

        return vc, ma

    def momento_fletor(va, vb, x1, x2):
        mac0 = va - 0
        mac1 = va - ((x1 ** 2) / 2)
        mbc0 = vb - 0
        mbc1 = vb - ((x2 ** 2) / 2)

        return mac0, mac1, mbc0, mbc1
