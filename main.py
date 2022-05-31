import sys
from application import *



if __name__ == '__main__':

    # va = input('insira VA:')
    # vb = input('insira VB:')
    # vc = input('insira VC:')
    # x1 = input('insira x1:')
    # x2 = input('insira x2:')

    va = 5; vb = 8; x1 = 10; x2 = 8

    qt= QApplication(sys.argv)
    app = Aplicacao()
    app.show()
    qt.exec()
    vc, ma = reacoes_de_apoio(va, vb, x1, x2)
    vac0, vac1, vbc0, vbc1 = forca_cortante(va, vb, x1, x2)
    mac0, mac1, mbc0, mbc1 = momento_fletor(va, vb, x1, x2)

    # print(f'Reações de apoio:\nVc = {vc} e Ma = {ma}')
    # print(f'\nForça cortante:\nVac (x = 0) = {vac0}')
    # print(f'Vac (x = x1) = {vac1}')
    # print(f'Vbc (x = 0) = {vbc0}')
    # print(f'Vbc (x = x2) = {vbc1}')
    # print(f'\nMomento fletor:\nMac (x = 0) = {mac0}')
    # print(f'Mac (x = x1) = {mac1}')
    # print(f'Mbc (x = 0) = {mbc0}')
    # print(f'Mbc (x = x2) = {mbc1}')



