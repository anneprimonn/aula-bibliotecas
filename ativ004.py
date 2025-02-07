from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys

class AnnePrimonButtonWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Capivara ou Macaco")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.image_label = QLabel()  
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        capybara_button = QPushButton("Mostrar Capivara")
        capybara_button.clicked.connect(self.show_capivara) 
        layout.addWidget(capybara_button)

        monkey_button = QPushButton("Mostrar Macaco")
        monkey_button.clicked.connect(self.show_macaco) 
        layout.addWidget(monkey_button)

        self.setCentralWidget(central_widget)

    def show_capivara(self):
        pixmap = QPixmap(r'C:\Users\suporte\Documents\GitHub\aula-bibliotecas\capivara.jpg')
        self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))

    def show_macaco(self):
        pixmap = QPixmap(r'C:\Users\suporte\Documents\GitHub\aula-bibliotecas\macaco.jpg')
        self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnnePrimonButtonWindow()
    window.show()
    sys.exit(app.exec())