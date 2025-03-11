from PySide6.QtWidgets import QMessageBox

def verificar_login(self):
        usuario = self.input_usuario.text()
        senha = self.input_senha.text()

        if usuario == "adm" and senha == "123":
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
            self.close()

        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")