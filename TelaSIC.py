from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(800, 500)
        self.setMaximumSize(800, 500)

        #criação do painel vermelho esquerdo
        self.painelEsquerdo = QLabel(self)
        self.painelEsquerdo.setStyleSheet('background-color: #FF3131;')  # cor do fundo do painel
        self.painelEsquerdo.setGeometry(0, 20, 320, 40)  # posição e tamanho do painel
        # Defina a propriedade **Qt.AlignLeft** para o painel
        self.painelEsquerdo.setAlignment(Qt.AlignLeft)

        # criação do painel vermelho direito
        self.painelDireito = QLabel(self)
        self.painelDireito.setStyleSheet('background-color: #FF3131;')  # cor do fundo do painel
        self.painelDireito.setGeometry(600, 0, 300, 600)  # posição e tamanho do painel
        # Defina a propriedade **Qt.AlignLeft** para o painel
        self.painelDireito.setAlignment(Qt.AlignRight)


        # Função do botão "conversar agora"
        self.conversarAgora = lambda: print("O botão chat foi clicado!")
        self.voltarHome = lambda: print("O botão home foi clicado!")
        self.consultarCursos = lambda : print("O botão cursos foi clicado")
        self.ajuda = lambda : print("O botão ajuda foi clicado")

        # Definindo a fonte Poppins
        self.poppins_font = QFont("Poppins", 12)

        # Propriedades do botão "conversar agora"
        self.botaoConversar = QPushButton("Conversar agora!", self)
        self.botaoConversar.setFont(self.poppins_font)
        self.botaoConversar.clicked.connect(self.conversarAgora)
        self.botaoConversar.setStyleSheet('''
            background-color: #FF3131;
            color: black;
            border: round;
            border-radius: 10px;
             /* Sombra branca */
            box-shadow: 0 0 10px 5px white;
        ''')
        self.botaoConversar.setGeometry(40, 400, 150, 30)  # posição e tamanho do botão


        # Propriedades do "botão" home
        self.botaoHome = QPushButton("Home", self)
        self.botaoHome.setFont(self.poppins_font)
        self.botaoHome.clicked.connect(self.voltarHome)
        self.botaoHome.setStyleSheet('background-color: transparent; color: black; border: none;') # cor do fundo e do texto do botão
        self.botaoHome.setGeometry(20, 25, 60, 30) # posição e tamanho do botão

        # Propriedades do "botão" chat
        self.botaoChat = QPushButton("Chat", self)
        self.botaoChat.setFont(self.poppins_font)
        self.botaoChat.clicked.connect(self.conversarAgora)
        self.botaoChat.setStyleSheet('background-color: transparent; color: black; border: none;') # cor do fundo e do texto do botão
        self.botaoChat.setGeometry(90, 25, 60, 30) # posição e tamanho do botão

        # Propriedades do "botão" cursos
        self.botaoCursos = QPushButton("Cursos", self)
        self.botaoCursos.setFont(self.poppins_font)
        self.botaoCursos.clicked.connect(self.consultarCursos)
        self.botaoCursos.setStyleSheet('background-color: transparent; color: black; border: none;')
        self.botaoCursos.setGeometry(160, 25, 80, 30)  # posição e tamanho do botão

        # Propriedades do "botão" cursos
        self.botaoAjuda = QPushButton("Ajuda", self)
        self.botaoAjuda.setFont(self.poppins_font)
        self.botaoAjuda.clicked.connect(self.ajuda)
        self.botaoAjuda.setStyleSheet('background-color: transparent; color: black; border: none;')
        self.botaoAjuda.setGeometry(230, 25, 80, 30)  # posição e tamanho do botão
        #self.imagem = QLabel(self)
        #self.imagem.setPixmap(
         #   QPixmap(r"C:\Users\user\Downloads\SIC-NWSRM-Featured-Image-798-_-500-px-removebg-preview.png"))
        #self.imagem.setGeometry(400, 20, 200, 40) '''
        self.adjustSize()



# Declaração dos elementos da tela
app = QApplication([])
window = MainWindow()
window.setWindowTitle("Tela inicial") # título da janela
window.setGeometry(100, 100, 800, 500) # tamanho e posição da janela
window.setStyleSheet('background-color: black;') # cor do fundo da janela
window.show()


sys.exit(app.exec_())
