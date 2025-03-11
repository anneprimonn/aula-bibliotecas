from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from verificar import verificar_login  # Importe a função verificar_login

class Login(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.label_usuario = QLabel("Usuário:")
        self.label_usuario.setAlignment(Qt.AlignCenter)
        self.input_usuario = QLineEdit()

        self.label_senha = QLabel("Senha:")
        self.label_senha.setAlignment(Qt.AlignCenter)
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password) 
        self.botao_entrar = QPushButton("Entrar")
        self.botao_cancelar = QPushButton("Cancelar")

        self.botao_entrar.clicked.connect(lambda: verificar_login(self)) 
        self.botao_cancelar.clicked.connect(self.close)

        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(self.label_senha)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.botao_entrar)
        layout.addWidget(self.botao_cancelar)