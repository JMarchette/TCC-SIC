from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
import sys
#from skimage.transform import resize
#import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(800, 500)
        self.setMaximumSize(800, 500)

        # criação do painel cinza superior
        self.painelEsquerdo = QLabel(self)
        self.painelEsquerdo.setStyleSheet('background-color: #545454;')  # cor do fundo do painel
        self.painelEsquerdo.setGeometry(150, 0, 610, 60)  # posição e tamanho do painel
        self.painelEsquerdo.setAlignment(Qt.AlignCenter)

        # criação do painel cinza inferior
        self.painelEsquerdo = QLabel(self)
        self.painelEsquerdo.setStyleSheet('background-color: #545454;')  # cor do fundo do painel
        self.painelEsquerdo.setGeometry(150, 440, 610, 60)  # posição e tamanho do painel
        self.painelEsquerdo.setAlignment(Qt.AlignCenter)

        # Declaração do campo de texto
        self.campoTexto = QLineEdit(self)
        self.campoTexto.setGeometry(160, 450, 530, 40)
        self.campoTexto.setStyleSheet(
            'background-color: #ffffff;'
            'color: #000000;'
            'font-size: 16px;'
            'border-radius: 5px;'
            'border-style: solid;'
            'border-width: 1px;'
            'border-color: #000000;'
        )

        # criação do painel vermelho direito
        self.painelDireito = QLabel(self)
        self.painelDireito.setStyleSheet('background-color: #CE0010;')  # cor do fundo do painel
        self.painelDireito.setGeometry(750, 0, 50, 500)  # posição e tamanho do painel

        # criação do painel preto direito
        self.painelPretoDireito = QLabel(self)
        self.painelPretoDireito.setStyleSheet(
            'background-color: #00000;' 'border-radius: 5px;')  # cor do fundo do painel
        self.painelPretoDireito.setGeometry(756, 0, 38, 205)  # posição e tamanho do painel

        # criação do painel branco direito
        self.painelBrancoDireito = QLabel(self)
        self.painelBrancoDireito.setStyleSheet('background-color: #ffffff;' 'border-radius: 5px;')  # cor do fundo do painel
        self.painelBrancoDireito.setGeometry(760, 0, 30, 200)  # posição e tamanho do painel



        # criação do painel vermelho esquerdo
        self.painelEsquerdo = QLabel(self)
        self.painelEsquerdo.setStyleSheet('background-color: #CE0010;')  # cor do fundo do painel
        self.painelEsquerdo.setGeometry(30, 20, 120, 500)  # posição e tamanho do painel
        self.painelEsquerdo.setAlignment(Qt.AlignLeft)

        ###########################################

        # Definindo a fonte padrão
        self.fontePadrao = QFont("Montserrat", 12)


# Declaração dos elementos da tela
app = QApplication([])
window = MainWindow()
window.setWindowTitle("Tela inicial") # título da janela
window.setGeometry(100, 100, 800, 500) # tamanho e posição da janela
window.setStyleSheet('background-color: black;') # cor do fundo da janela
window.show()


sys.exit(app.exec_())