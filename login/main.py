import sys
from PySide6.QtWidgets import QApplication
from login import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.showMaximized()
    sys.exit(app.exec())