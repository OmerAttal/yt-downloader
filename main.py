import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton , QLineEdit , QDialog , QVBoxLayout , QWidget , QListWidget , QListWidgetItem , QHBoxLayout
from PySide6.QtCore import Slot,Signal,QObject , Qt 

class Yt_app(QDialog):
    def __init__(self , parent = None):
        super().__init__(parent)

        self.setWindowTitle("YT downloader")
        self.setGeometry(600 , 600 , 500 , 300)

        button = QPushButton("click")
        button.setFixedSize(200,25)
        button.clicked.connect(self.button_click)
        
        text = QLineEdit()
        text.setFixedSize(350 , 25)

        layout = QVBoxLayout()
        layout.addWidget(text)
        layout.addWidget(button)

        layout.setAlignment(button , Qt.AlignCenter)
        layout.setAlignment(text , Qt.AlignCenter)

        self.setLayout(layout)

    def button_click(self):
        print("clicked")
        

if __name__ == '__main__':
    app = QApplication()

    window = Yt_app()
    window.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())