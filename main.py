import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton , QLineEdit , QDialog , QVBoxLayout , QWidget , QListWidget , QListWidgetItem , QHBoxLayout , QComboBox
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

        boxP = QComboBox()
        boxP.addItem("1080p")
        boxP.addItem("720p")
        boxP.addItem("480p")
        boxP.addItem("360p")
        boxP.addItem("240p")
        boxP.addItem("144p")
        boxP.setFixedSize(100,20)

        boxM = QComboBox()
        boxM.addItem("mp3")
        boxM.addItem("mp4")
        boxM.setFixedSize(100,20)

        layout_h = QHBoxLayout()
        layout_h.addWidget(boxP)
        layout_h.addWidget(boxM)

        layout = QVBoxLayout()
        layout.addWidget(text)
        layout.addLayout(layout_h)
        layout.addWidget(button)

        layout.setAlignment(button , Qt.AlignCenter)
        layout.setAlignment(text , Qt.AlignCenter)
        layout_h.setAlignment(boxM , Qt.AlignLeft)
        layout_h.setAlignment(boxP , Qt.AlignRight)
        
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