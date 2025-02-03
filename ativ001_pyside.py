from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys

class AnnePrimonWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Anne Primon")
        self.setGeometry(100, 100, 300, 200) 

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        label = QLabel("Anne Primon")
        label.setAlignment(Qt.AlignCenter)  # Centraliza o texto
        label.setStyleSheet("font-size: 24px; font-weight: bold;")

        layout.addWidget(label)
        self.setCentralWidget(central_widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnnePrimonWindow()
    window.show()
    sys.exit(app.exec())