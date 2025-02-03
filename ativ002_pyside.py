from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys

class AnnePrimonPhotoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Anne Primon with Photo")
        self.setGeometry(100, 100, 400, 350)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        label = QLabel("Anne Primon")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(label)

        pixmap = QPixmap(r'C:\Users\suporte\Documents\GitHub\aula-bibliotecas\paisagem.jpg')
        photo_label = QLabel()
        photo_label.setAlignment(Qt.AlignCenter)
        photo_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio)) # Redimensiona mantendo a proporção
        layout.addWidget(photo_label)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnnePrimonPhotoWindow()
    window.show()
    sys.exit(app.exec())