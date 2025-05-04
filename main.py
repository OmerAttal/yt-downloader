import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton , QLineEdit , QDialog , QVBoxLayout , QWidget , QListWidget , QListWidgetItem , QHBoxLayout , QComboBox
from PySide6.QtCore import Qt 
import yt_dlp
import os
from pytube import YouTube

os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

class Yt_app(QDialog):
    def __init__(self , parent = None):
        super().__init__(parent)

        self.setWindowTitle("YT downloader")
        self.setGeometry(500 , 250 , 500 , 300)

        self.button = QPushButton("Install")
        self.button.setFixedSize(200,25)
        self.button.clicked.connect(self.button_click)

        self.buttonAgain = QPushButton("Install Onether Video")
        self.buttonAgain.setFixedSize(200,25)
        self.buttonAgain.clicked.connect(self.returntomenu)
        
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

        self.loading_label = QLabel("Download Completed")

        self.layout_h = QHBoxLayout()
        self.layout_h.addWidget(self.boxP)
        self.layout_h.addWidget(self.boxM)

        self.layout = QVBoxLayout()
        self.layout.addWidget(label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.file)
        self.layout.addLayout(self.layout_h)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.loading_label)
        self.layout.addWidget(self.buttonAgain)
        self.loading_label.hide()
        self.buttonAgain.hide()


        self.layout.setAlignment(label , Qt.AlignCenter)
        self.layout.setAlignment(self.button , Qt.AlignCenter)
        self.layout.setAlignment(self.text , Qt.AlignBottom | Qt.AlignCenter)
        self.layout_h.setAlignment(self.boxM , Qt.AlignLeft)
        self.boxM.currentIndexChanged.connect(self.on_format_selected)
        self.layout_h.setAlignment(self.boxP , Qt.AlignRight)
        self.layout.setAlignment(self.file , Qt.AlignCenter)
        self.layout.setAlignment(self.loading_label , Qt.AlignTop | Qt.AlignCenter)
        self.layout.setAlignment(self.buttonAgain , Qt.AlignCenter)

        self.setLayout(self.layout)

    def button_click(self):
        link = self.text.text()
        format = self.boxM.currentText()
        file = self.file.text()

        if link and format and file:
            self.text.hide()
            self.file.hide()
            self.boxP.hide()
            self.boxM.hide()
            self.button.hide()
            self.loading_label.show()
            self.buttonAgain.show()
            self.Download(link,file,format)
        else:
            print("some bug")

    def on_format_selected(self):
        format = self.boxM.currentText()
        if format == "mp4":
            self.boxP.show()
        else:
            self.boxP.hide()


    def Download(self, link, file, format_choice):
        selected_res = self.boxP.currentText()  
        selected_height = int(selected_res.replace("p", ""))  
        
        if format_choice == 'mp3':  
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',   
                    'preferredquality': '192',
                }],
                'outtmpl': f"{file}.%(ext)s",  
            }
        elif format_choice == 'mp4':  
            ydl_opts = {
                'format': f"bestvideo[ext=mp4][height<={selected_height}]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                'outtmpl': f"{file}.%(ext)s",  
                'merge_output_format': 'mp4',
            }
        else:
            print("Uygun bir format seçilmedi.")
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([link])  
                print("İndirme tamamlandı.")
            except Exception as e:
                print(f"Bir hata oluştu: {e}")  

    def returntomenu(self):
        self.text.show()
        self.file.show()
        self.boxP.show()
        self.boxM.show()
        self.button.show()
        self.loading_label.hide()
        self.buttonAgain.hide()

if __name__ == '__main__':
    app = QApplication()

    window = Yt_app()
    window.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())