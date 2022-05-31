import sys
from application import *

if __name__ == '__main__':

    qt= QApplication(sys.argv)
    app = Aplicacao()
    app.show()
    qt.exec()



