from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys

class NameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
       
    def init_ui(self):
        
        self.setWindowTitle('inverter nome') 

        self.label_name = QLabel('Digite seu nome:')
        self.input_name = QLineEdit()

        self.button_reverse = QPushButton('inverter')
        self.button_reverse.clicked.connect(self.reverse_name)
        self.result_label = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.button)
        layout.addWidget(self.result_name)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        def reverse_name(self):
            name = self.input_name.text()
            reversed_name = ""
            for i in range(len(name) -1):
                reversed_name += name[i]
            self.result_name.setText (f'Nome invertido: {reversed_name} ')

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NameWindow()
    window.show()
    sys.exit(app.exec())