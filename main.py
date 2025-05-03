import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton , QLineEdit , QDialog , QVBoxLayout , QWidget , QListWidget , QListWidgetItem , QHBoxLayout
from PySide6.QtCore import Slot,Signal,QObject , Qt 

class Yt_app(QDialog):
    print("")

if __name__ == '__main__':
    app = QApplication()

    window = Yt_app()
    window.show()

    sys.exit(app.exec())