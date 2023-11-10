import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QFont, QPixmap, QIcon, QDesktopServices
from PyQt5.QtCore import Qt, QSize, QUrl
import sys

#from skimage.transform import resize
#import matplotlib.pyplot as plt

class TelaChat(QMainWindow):

    def solicitarSuporte(self):
        QDesktopServices.openUrl(QUrl("www.sp.senai.br/fale-conosco?menu=39&idescola=109"))
    def consultarCursos(self):
        QDesktopServices.openUrl(QUrl("https://sp.senai.br/cursos/"))
    def chamarTelaHome(telaHome):
        """Chama outra tela e oculta a atual.

        Args:
          nome_tela: O nome da tela a ser chamada.

        Returns:
          None.
        """

        # Obtém a tela atual.
        telaChat = app.active_screen()

        # Chama a outra tela.
        app.open_screen(telaHome)

        # Oculta a tela atual.
        telaChat.hide()

        # Conecta o sinal 'destroyed' da nova tela à função que mostra a tela atual.
        telaHome.destroyed.connect(telaChat.show)

    def enviarPergunta(self):
        mensagem = self.campoTexto.text()  # Obter o texto do campo de texto
        self.campoTexto.clear()
        if mensagem:
            # Chamar a API apenas se houver uma mensagem
            API_KEY = "INSERIR A API AQUI"
            response = requests.post(
                "https://api.openai.com/v1/engines/text-davinci-002/completions",
                headers={"Authorization": f"Bearer {API_KEY}"},
                json={"prompt": mensagem, "temperature": 0.9, "max_tokens": 100},
            )

            if response.status_code == 200:
                response_json = response.json()
                if "choices" in response_json:
                    resposta = response_json["choices"][0]["text"]
                    # Exibir a resposta (você pode exibi-la onde desejar)
                    print("Resposta da API:", resposta)
                else:
                    print("Erro: Resposta inesperada da API.")
            else:
                print(f"Erro na solicitação à API: {response.status_code}")
                print(response.text)

    def __init__(self):
        super(TelaChat, self).__init__()
        self.setMinimumSize(800, 500)
        self.setMaximumSize(800, 500)

        # Definindo a fonte padrão
        self.fontePadrao = QFont("Montserrat", 12)

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

        ###############################

        # botão enviar
        self.botaoEnviar = QPushButton(self)
        self.botaoEnviar.clicked.connect(self.enviarPergunta)
        self.botaoEnviar.setStyleSheet(
            'background-color: transparent; color: black; border: none;')  # cor do fundo e do texto do botão
        self.botaoEnviar.setGeometry(170, 455, 1100, 30)  # posição e tamanho do botão
        # Criando o ícone de casa
        iconeEnviar = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeEnviar.png")

        # Definindo o ícone do botão "enviar" e seu tamanho
        self.botaoEnviar.setIcon(iconeEnviar)
        self.botaoEnviar.setIconSize(QSize(30, 30))
        self.botaoEnviar.setCursor(Qt.PointingHandCursor) # Muda o cursor do mouse para cursor de mão

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

        ###############################

        # criação do painel vermelho direito
        self.painelDireito = QLabel(self)
        self.painelDireito.setStyleSheet('background-color: #CE0010;')  # cor do fundo do painel
        self.painelDireito.setGeometry(750, 0, 50, 500)  # posição e tamanho do painel

        # criação do painel preto direito
        self.painelPretoDireito = QLabel(self)
        self.painelPretoDireito.setStyleSheet(
            'background-color: #00000;' 'border-radius: 5px;')  # cor do fundo do painel
        self.painelPretoDireito.setGeometry(756, 0, 38, 125)  # posição e tamanho do painel

        # criação do painel branco direito
        self.painelBrancoDireito = QLabel(self)
        self.painelBrancoDireito.setStyleSheet('background-color: #ffffff;' 'border-radius: 5px;')  # cor do fundo do painel
        self.painelBrancoDireito.setGeometry(760, 0, 30, 120)  # posição e tamanho do painel

        ###############################

        #criação do botão HOME
        self.botaoHome = QPushButton(self)
        self.botaoHome.setFont(self.fontePadrao)
        #self.botaoHome.clicked.connect(self.telaHome)
        self.botaoHome.clicked.connect(self.chamarTelaHome)
        self.botaoHome.setStyleSheet(
            'background-color: transparent; color: black; border: none;')  # cor do fundo e do texto do botão
        self.botaoHome.setGeometry(735, 5, 80, 30)  # posição e tamanho do botão
        # Criando o ícone de casa
        iconeCasa = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeCasa.png")

        # Definindo o ícone do botão "Home" e seu tamanho
        self.botaoHome.setIcon(iconeCasa)
        self.botaoHome.setIconSize(QSize(30, 30))
        self.botaoHome.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão

        ###############################

        # Propriedades do "botão" cursos
        self.botaoCursos = QPushButton(self)
        self.botaoCursos.setFont(self.fontePadrao)
        self.botaoCursos.clicked.connect(self.consultarCursos)
        self.botaoCursos.setStyleSheet('background-color: transparent; color: black; border: none;')
        self.botaoCursos.setGeometry(735, 45, 80, 30)  # posição e tamanho do botão
        # Icone do botão cursos
        iconeCursos = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeCursos.png")
        self.botaoCursos.setIcon(iconeCursos)
        self.botaoCursos.setIconSize(QSize(30, 30))
        self.botaoCursos.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão

        ###############################

        # Propriedades do "botão" Ajuda
        self.botaoAjuda = QPushButton(self)
        self.botaoAjuda.setFont(self.fontePadrao)
        self.botaoAjuda.clicked.connect(self.solicitarSuporte)
        self.botaoAjuda.setStyleSheet('background-color: transparent; color: black; border: none;')
        self.botaoAjuda.setGeometry(735, 75, 80, 40)  # posição e tamanho do botão

        iconeAjuda = QIcon(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeAjuda.png")
        self.botaoAjuda.setIcon(iconeAjuda)
        self.botaoAjuda.setIconSize(QSize(40, 40))
        self.botaoAjuda.setCursor(Qt.PointingHandCursor)  # Muda o cursor do mouse para cursor de mão

        ###############################

        # criação do painel vermelho esquerdo
        self.painelEsquerdo = QLabel(self)
        self.painelEsquerdo.setStyleSheet('background-color: #CE0010;')  # cor do fundo do painel
        self.painelEsquerdo.setGeometry(30, 20, 120, 500)  # posição e tamanho do painel
        self.painelEsquerdo.setAlignment(Qt.AlignLeft)

        # Criação do painel preto esquerdo
        self.painelPretoEsquerdo = QLabel(self)
        self.painelPretoEsquerdo.setStyleSheet(
            'background-color: #000000; border-radius: 5px;')  # cor do fundo do painel
        self.painelPretoEsquerdo.setGeometry(45, 23, 103, 25)  # posição e tamanho do painel
        self.painelPretoEsquerdo.setAlignment(Qt.AlignLeft)

        #Criação do painel branco esquerdo
        self.painelBrancoEsquerdo = QLabel(self)
        self.painelBrancoEsquerdo.setStyleSheet('background-color: #FFFFFF; border-radius: 5px;')  # cor do fundo do painel
        self.painelBrancoEsquerdo.setGeometry(45, 25, 100, 20)  # posição e tamanho do painel
        self.painelBrancoEsquerdo.setAlignment(Qt.AlignLeft)

        # Círculo para foto
        circuloFoto = QLabel(self)
        circuloFoto.setGeometry(0, 2, 65, 65)  # Posição e tamanho do QLabel
        circuloFoto.setStyleSheet('border-radius: 32px; background: transparent;')

        # Carrega a imagem
        foto = QPixmap(r"C:\Users\user\Desktop\Projeto senai\Desenvolvimento\Imagens\iconeSeleneRedondo.png")
        foto = foto.scaled(60, 60, Qt.KeepAspectRatio)

        # Aplica a imagem ao QLabel
        circuloFoto.setPixmap(foto)

        # Nome da assistente
        nomeAssistente = QLabel("SELENE", self)
        nomeAssistente.setFont(QFont("Montserrat", 14))
        nomeAssistente.setGeometry(65, 20, 200, 32)  # Posição e tamanho do QLabel
        nomeAssistente.setStyleSheet('color: #FF3131; background-color: transparent')

        ###########################################


# Declaração dos elementos da tela
app = QApplication([])
window = TelaChat()
window.setWindowTitle("Tela de chat") # título da janela
window.setGeometry(100, 100, 800, 500) # tamanho e posição da janela
window.setStyleSheet('background-color: black;') # cor do fundo da janela
window.show()
sys.exit(app.exec_())
