from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QIcon, QDesktopServices
from PyQt5.QtCore import Qt, QSize, QUrl
import sys
#from skimage.transform import resize
#import matplotlib.pyplot as plt

class TelaHome(QMainWindow):

    """def telaconversar(self):
        self.hide()  # Oculta a janela atual (Chat)
        telaChat.show()  # Mostra a janela "Conversar Agora"""
    def homeSenai(self):
        QDesktopServices.openUrl(QUrl("https://sp.senai.br/"))

    def sobreProjeto(self):
        QDesktopServices.openUrl(QUrl("https://github.com/JMarchette/TCC-SIC/blob/main/README.md"))


    #FUNÇÃO DO BOTÃO AJUDA
    def solicitarSuporte(self):
        QDesktopServices.openUrl(QUrl("www.sp.senai.br/fale-conosco?menu=39&idescola=109"))

    #FUNÇÃO DO BOTÃO CURSOS
    def consultarCursos(self):
        QDesktopServices.openUrl(QUrl("https://sp.senai.br/cursos/"))

    def direcionarSIC(self):
        QDesktopServices.openUrl(QUrl("https://sicbrasil.org.br/"))

    def __init__(self):
        super(TelaHome, self).__init__()
        self.setMinimumSize(800, 500)
        self.setMaximumSize(800, 500)
        # Definindo a fonte padrão
        self.fontePadrao = QFont("Montserrat", 12)
        self.setWindowIcon(QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeSelene.jpg"))

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
        #imagemDireita = QLabel(self)
        #imagemDireita.setGeometry(600, 0, 100, 100)  # Posição e tamanho do QLabel
        #pixmap = QPixmap(r"C:\Users\user\Desktop\testeee\Imagens\logoCinza.png")  # Substitua com o caminho para sua imagem PNG
        #imagemDireita.setPixmap(pixmap)
        #imagemDireita.setScaledContents(True)  # Configurar para lidar com imagens com canais alfa


        ###########################################

        # Função de teste dos botões
        self.conversarAgora = lambda: print("O botão chat foi clicado!")
        self.voltarHome = lambda: print("O botão home foi clicado!")

        ###########################################

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
        self.botaoConversar.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão


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
        self.botaoHome = QPushButton("Home", self.painelEsquerdo)
        self.botaoHome.setFont(self.fontePadrao)
        self.botaoHome.clicked.connect(self.homeSenai)
        self.botaoHome.setStyleSheet('background-color: transparent; color: black; border: none;') # cor do fundo e do texto do botão
        self.botaoHome.setGeometry(10, 5, 80, 30) # posição e tamanho do botão
        # Criando o ícone de casa
        iconeCasa = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeCasa.png")

        # Definindo o ícone do botão "Home" e seu tamanho
        self.botaoHome.setIcon(iconeCasa)
        self.botaoHome.setIconSize(QSize(20, 20))
        self.botaoHome.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão


        ###########################################

        # Propriedades do "botão" chat
        self.botaoChat = QPushButton("Chat", self.painelEsquerdo)
        self.botaoChat.setFont(self.fontePadrao)
        #self.botaoChat.clicked.connect(self.conversarAgora())
        self.botaoChat.setStyleSheet('background-color: transparent; color: black; border: none;') # cor do fundo e do texto do botão
        self.botaoChat.setGeometry(90, 5, 80, 30) # posição e tamanho do botão
        #Icone do botão chat
        iconeChat = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeChat.png")
        self.botaoChat.setIcon(iconeChat)
        self.botaoChat.setIconSize(QSize(20, 20))
        self.botaoChat.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão


        ###########################################

        # Propriedades do "botão" cursos
        self.botaoCursos = QPushButton("Cursos", self.painelEsquerdo)
        self.botaoCursos.setFont(self.fontePadrao)
        self.botaoCursos.clicked.connect(self.consultarCursos)
        self.botaoCursos.setStyleSheet('background-color: transparent; color: black; border: none;')
        self.botaoCursos.setGeometry(170, 5, 80, 30)  # posição e tamanho do botão
        # Icone do botão cursos
        iconeCursos = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeCursos.png")
        self.botaoCursos.setIcon(iconeCursos)
        self.botaoCursos.setIconSize(QSize(20, 20))
        self.botaoCursos.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão


        ###########################################


        # Propriedades do "botão" Ajuda
        self.botaoAjuda = QPushButton("Ajuda", self.painelEsquerdo)
        self.botaoAjuda.setFont(self.fontePadrao)
        self.botaoAjuda.clicked.connect(self.solicitarSuporte)
        self.botaoAjuda.setStyleSheet('background-color: transparent; color: black; border: none;')
        self.botaoAjuda.setGeometry(260, 5, 80, 30)  # posição e tamanho do botão

        iconeAjuda = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeAjuda.png")
        self.botaoAjuda.setIcon(iconeAjuda)
        self.botaoAjuda.setIconSize(QSize(30, 30))
        self.botaoAjuda.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão


        #Botão SIC
        self.botaoSIC = QPushButton(self.painelDireito)
        self.botaoSIC.setFont(self.fontePadrao)
        self.botaoSIC.clicked.connect(self.direcionarSIC)
        self.botaoSIC.setStyleSheet(
            'background-color: transparent; color: black; border: none;')  # cor do fundo e do texto do botão
        self.botaoSIC.setGeometry(5, 50, 200, 170)  # posição e tamanho do botão
        # Criando o ícone de casa
        iconeSIC = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\sicFundo.png")

        # Definindo o ícone do botão "Home" e seu tamanho
        self.botaoSIC.setIcon(iconeSIC)
        self.botaoSIC.setIconSize(QSize(170, 170))
        self.botaoSIC.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão

        # Logo Senai
        self.botaoSenai = QPushButton(self.painelDireito)  # Adicione o painel como o widget pai do botão
        self.botaoSenai.setFont(self.fontePadrao)
        self.botaoSenai.clicked.connect(self.conversarAgora)
        self.botaoSenai.setStyleSheet(
            'background-color: transparent; color: black; border: none;')  # cor do fundo e do texto do botão
        self.botaoSenai.setGeometry(25, -30, 150, 150)  # posição e tamanho do botão
        # Criando o ícone de casa
        iconeSIC = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\logoSenai.png")

        # Definindo o ícone do botão "Home" e seu tamanho
        self.botaoSenai.setIcon(iconeSIC)
        self.botaoSenai.setIconSize(QSize(150, 150))

        # Sobre o projeto
        self.botaoProjeto = QPushButton("Sobre o projeto", self.painelDireito)  # Adicione o painel como o widget pai do botão
        self.botaoProjeto.setFont(self.fontePadrao)
        self.botaoProjeto.clicked.connect(self.sobreProjeto)
        self.botaoProjeto.setStyleSheet(
            'background-color: transparent; color: black; border: none;')  # cor do fundo e do texto do botão
        self.botaoProjeto.setGeometry(25, 350, 150, 150)  # posição e tamanho do botão
        self.botaoProjeto.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão


# Declaração dos elementos da tela
app = QApplication([])
window = TelaHome()
window.setWindowTitle("Tela inicial") # título da janela
window.setGeometry(100, 100, 800, 500) # tamanho e posição da janela
window.setStyleSheet('background-color: black;') # cor do fundo da janela
window.show()


sys.exit(app.exec_())


