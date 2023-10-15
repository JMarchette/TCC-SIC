from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
import sys
from skimage.transform import resize
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(800, 500)
        self.setMaximumSize(800, 500)

        #criação do painel vermelho esquerdo
        self.painelEsquerdo = QLabel(self)
        self.painelEsquerdo.setStyleSheet('background-color: #FF3131;')  # cor do fundo do painel
        self.painelEsquerdo.setGeometry(0, 20, 350, 40)  # posição e tamanho do painel
        self.painelEsquerdo.setAlignment(Qt.AlignLeft)

        # criação do painel vermelho direito
        self.painelDireito = QLabel(self)
        self.painelDireito.setStyleSheet('background-color: #FF3131;')  # cor do fundo do painel
        self.painelDireito.setGeometry(600, 0, 200, 500)  # posição e tamanho do painel

        #Propriedades da foto da SIC
        imagemDireita = QLabel(self)
        imagemDireita.setGeometry(600, 0, 100, 100)  # Posição e tamanho do QLabel
        pixmap = QPixmap(r"C:\Users\user\Desktop\testeee\Imagens\logoCinza.png")  # Substitua com o caminho para sua imagem PNG
        imagemDireita.setPixmap(pixmap)
        imagemDireita.setScaledContents(True)  # Configurar para lidar com imagens com canais alfa


        ###########################################

        # Função de teste dos botões
        self.conversarAgora = lambda: print("O botão chat foi clicado!")
        self.voltarHome = lambda: print("O botão home foi clicado!")
        self.consultarCursos = lambda : print("O botão cursos foi clicado")
        self.ajuda = lambda : print("O botão ajuda foi clicado")

        ###########################################

        # Definindo a fonte padrão
        self.fontePadrao = QFont("Montserrat", 12)

       # Propriedades do botão "conversar agora"
        self.botaoConversar = QPushButton("Conversar agora!", self)
        self.botaoConversar.setFont(self.fontePadrao)
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

        ###########################################

        # Nome da assistente
        nomeAssistente = QLabel("SELENE", self)
        nomeAssistente.setFont(QFont("Montserrat", 28))
        nomeAssistente.setGeometry(40, 190, 200, 32)  # Posição e tamanho do QLabel
        nomeAssistente.setStyleSheet('color: #FF3131;')

        # criação do painel BRANCO esquerdo
        self.painelCentral = QLabel(self)
        self.painelCentral.setStyleSheet('background-color: #FFFFFF;')  # cor do fundo do painel
        self.painelCentral.setGeometry(40, 230, 180, 1)  # posição e tamanho do painel

        #Subtítulo assistente
        subTitulo = QLabel("SENAI ASSISTANT", self)
        subTitulo.setFont(QFont("Montserrat", 14))
        subTitulo.setGeometry(40, 235, 250, 30)
        subTitulo.setStyleSheet('color: #FFFFFF;')

        ###########################################

        # Propriedades do "botão" home
        self.botaoHome = QPushButton("Home", self)
        self.botaoHome.setFont(self.fontePadrao)
        self.botaoHome.clicked.connect(self.voltarHome)
        self.botaoHome.setStyleSheet('background-color: transparent; color: black; border: none;') # cor do fundo e do texto do botão
        self.botaoHome.setGeometry(10, 25, 80, 30) # posição e tamanho do botão
        # Criando o ícone de casa
        iconeCasa = QIcon(r"C:\Users\user\Desktop\testeee\Imagens\iconeCasa.png")

        # Definindo o ícone do botão "Home" e seu tamanho
        self.botaoHome.setIcon(iconeCasa)
        self.botaoHome.setIconSize(QSize(20, 20))

        ###########################################

        # Propriedades do "botão" chat
        self.botaoChat = QPushButton("Chat", self)
        self.botaoChat.setFont(self.fontePadrao)
        self.botaoChat.clicked.connect(self.conversarAgora)
        self.botaoChat.setStyleSheet('background-color: transparent; color: black; border: none;') # cor do fundo e do texto do botão
        self.botaoChat.setGeometry(90, 25, 80, 30) # posição e tamanho do botão
        #Icone do botão chat
        iconeChat = QIcon(r"C:\Users\user\Desktop\testeee\Imagens\iconeChat.png")
        self.botaoChat.setIcon(iconeChat)
        self.botaoChat.setIconSize(QSize(20, 20))

        ###########################################

        # Propriedades do "botão" cursos
        self.botaoCursos = QPushButton("Cursos", self)
        self.botaoCursos.setFont(self.fontePadrao)
        self.botaoCursos.clicked.connect(self.consultarCursos)
        self.botaoCursos.setStyleSheet('background-color: transparent; color: black; border: none;')
        self.botaoCursos.setGeometry(170, 25, 80, 30)  # posição e tamanho do botão
        # Icone do botão cursos
        iconeCursos = QIcon(r"C:\Users\user\Desktop\testeee\Imagens\iconeCursos.png")
        self.botaoCursos.setIcon(iconeCursos)
        self.botaoCursos.setIconSize(QSize(20, 20))

        ###########################################


        # Propriedades do "botão" Ajuda
        self.botaoAjuda = QPushButton("Ajuda", self)
        self.botaoAjuda.setFont(self.fontePadrao)
        self.botaoAjuda.clicked.connect(self.ajuda)
        self.botaoAjuda.setStyleSheet('background-color: transparent; color: black; border: none;')
        self.botaoAjuda.setGeometry(260, 25, 80, 30)  # posição e tamanho do botão

        iconeAjuda = QIcon(r"C:\Users\user\Desktop\testeee\Imagens\iconeAjuda.png")
        self.botaoAjuda.setIcon(iconeAjuda)
        self.botaoAjuda.setIconSize(QSize(30, 30))




# Declaração dos elementos da tela
app = QApplication([])
window = MainWindow()
window.setWindowTitle("Tela inicial") # título da janela
window.setGeometry(100, 100, 800, 500) # tamanho e posição da janela
window.setStyleSheet('background-color: black;') # cor do fundo da janela
window.show()


sys.exit(app.exec_())
