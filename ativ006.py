from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QWidget
import sys
from PySide6.QtCore import Qt

class Login(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 400, 400)


        central_widget = QWidget()
        self.setCentralWidget(central_widget) 

        layout = QVBoxLayout(central_widget) 

        self.label_usuario = QLabel("Usuário:")
        self.label_usuario.setAlignment(Qt.Alignment)
        self.input_usuario = QLineEdit()
        self.label_senha = QLabel("Senha:")
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        self.botao_entrar = QPushButton("Entrar")
        self.botao_cancelar = QPushButton("Cancelar")


        self.botao_entrar.clicked.connect(self.verificar_login)
        self.botao_cancelar.clicked.connect(self.close) 

        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(self.label_senha)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.botao_entrar)
        layout.addWidget(self.botao_cancelar)


    def verificar_login(self):
        usuario = self.input_usuario.text()
        senha = self.input_senha.text()

        if usuario == "adm" and senha == "123":
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
            self.close()

        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())