import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton , QLineEdit , QDialog , QVBoxLayout , QWidget , QListWidget , QListWidgetItem , QHBoxLayout , QComboBox
from PySide6.QtCore import Slot,Signal,QObject , Qt 
from pytube import YouTube

class Yt_app(QDialog):
    def __init__(self , parent = None):
        super().__init__(parent)

        self.setWindowTitle("YT downloader")
        self.setGeometry(500 , 250 , 500 , 300)

        button = QPushButton("Install")
        button.setFixedSize(200,25)
        button.clicked.connect(self.button_click)
        
        self.text = QLineEdit()
        self.text.setPlaceholderText("Video Link")
        self.text.setFixedSize(350 , 25)

        self.file = QLineEdit()
        self.file.setPlaceholderText("File Name")
        self.file.setFixedSize(350 , 25)

        self.boxP = QComboBox()
        self.boxP.addItem("1080p")
        self.boxP.addItem("720p")
        self.boxP.addItem("480p")
        self.boxP.addItem("360p")
        self.boxP.addItem("240p")
        self.boxP.addItem("144p")
        self.boxP.setFixedSize(100,20)

        self.boxM = QComboBox()
        self.boxM.addItem("mp3")
        self.boxM.addItem("mp4")
        self.boxM.setFixedSize(100,20)

        label = QLabel("yt-downloader")

        layout_h = QHBoxLayout()
        layout_h.addWidget(self.boxP)
        layout_h.addWidget(self.boxM)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.text)
        layout.addWidget(self.file)
        layout.addLayout(layout_h)
        layout.addWidget(button)

        layout.setAlignment(label , Qt.AlignCenter)
        layout.setAlignment(button , Qt.AlignCenter)
        layout.setAlignment(self.text , Qt.AlignBottom | Qt.AlignCenter)
        layout_h.setAlignment(self.boxM , Qt.AlignLeft)
        layout_h.setAlignment(self.boxP , Qt.AlignRight)
        layout.setAlignment(self.file , Qt.AlignCenter)

        self.setLayout(layout)

    def button_click(self):
        link = self.text.text()
        format = self.boxM.currentText()
        quality = self.boxP.currentText()
        file = self.file.text()


if __name__ == '__main__':
    app = QApplication()

    window = Yt_app()
    window.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())