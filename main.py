import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton , QLineEdit , QDialog , QVBoxLayout , QWidget , QListWidget , QListWidgetItem , QHBoxLayout
from PySide6.QtCore import Slot,Signal,QObject , Qt 

class Yt_app(QDialog):
    def __init__(self , parent = None):
        super().__init__(parent)

        button = QPushButton("click")
        button.clicked.connect(self.button_click)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def button_click(self):
        print("clicked")
        

if __name__ == '__main__':
    app = QApplication()

    window = Yt_app()
    window.show()

    sys.exit(app.exec())