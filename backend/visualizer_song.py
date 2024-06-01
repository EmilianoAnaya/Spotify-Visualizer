from frontend.ui_visualizer_song import Ui_Visualizer_Song
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation
from backend.SpotifyAuth import get_Spotify
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
import tempfile
import requests
import json
import os

class Visualizer_Song(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Visualizer_Song()
        self.ui.setupUi(self)
        self.ui.widget_Song.setMaximumHeight(210)
        icon = QIcon("resources/images/Spotify_visualizer_logo.png")
        self.setWindowIcon(icon)
        with open('resources/credentials/data.json',"r") as file:
            credentials = json.load(file)
            CLIENT_ID = credentials["Client_ID"]
            CLIENT_SECRET = credentials["Client_Secret"]

        self.spotify = get_Spotify(CLIENT_ID,CLIENT_SECRET)
        self.CurrentTrack:str = ""
        self.tmp_file_path: str = ""

        self.mouse_pressed = False
        self.old_pos = None
        self.flagdelete = False

        self.CheckTimer = QTimer()
        self.CheckTimer.setInterval(3000)
        self.CheckTimer.timeout.connect(self.CheckCurrentTrack)
        self.CheckTimer.start()

        self.Animation = QPropertyAnimation(self.ui.widget_Song, b"maximumHeight")
        self.Animation.setDuration(300)

    def truncate_text(self, text: str, label) -> str:
        font_metrics = label.fontMetrics()
        elided_text = font_metrics.elidedText(text, Qt.ElideRight, label.width())
        return elided_text
    
    def setSongInfo(self, SongName:str, Artists:list) -> None:
        Truncate_song_name = self.truncate_text(SongName, self.ui.label_SongName)
        self.ui.label_SongName.setText(Truncate_song_name)

        results = ' - '.join(artists['name'] for artists in Artists)
        self.ui.label_SongArtist.setText(results)
    
    def setAlbumCover(self, AlbumCover: str):
        getImage = requests.get(AlbumCover)
        tmp_dir = tempfile.mkdtemp(dir="resources/images/")
        tmp_file_path = os.path.join(tmp_dir, "cover.jpg")
        with open(tmp_file_path, 'wb') as file:
            file.write(getImage.content)
        
        tmp_file_path = tmp_file_path.replace('\\', '/')
        self.ui.widget_AlbumCover.setStyleSheet(u"#widget_AlbumCover{\n"
                                                f"border-image: url({tmp_file_path});\n"
                                                "}")
        
        self.ui.widget_Song.setStyleSheet(u"#widget_Song{\n"
                                          f"border-image: url({tmp_file_path});\n"
                                          "}\n"
                                          "\n"
                                          "")
        return tmp_file_path
        

    def CheckSameSong(self, results:str) -> bool:
        if self.CurrentTrack == results:
            return True
        self.CurrentTrack = results
        return False
    
    def CheckCurrentTrack(self):
        results = self.spotify.current_user_playing_track()
        if not results:
            self.CheckTimer.setInterval(4000)
            return
        if not self.CheckSameSong(results['item']['id']):
            self.WidgetAnimation(210,0, lambda:self.InsertInfo(results))

    def closeEvent(self,event):
        if self.flagdelete:
            self.DeleteTmpImage(self.tmp_file_path)
        event.accept()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = True
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = False

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            delta = event.globalPos() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPos()

    def InsertInfo(self,results):
        self.Animation.finished.disconnect()
        self.WidgetAnimation(0,210)
        delete_tmp_file = self.tmp_file_path
        self.tmp_file_path = self.setAlbumCover(results['item']['album']['images'][1]["url"])
        self.setSongInfo(results['item']['name'],results['item']['artists'])
        self.flagdelete = True
        if delete_tmp_file != "":
            self.DeleteTmpImage(delete_tmp_file)
    
    def WidgetAnimation(self,StartValue: int, EndValue: int, callback=None):
        self.Animation.setStartValue(StartValue)
        self.Animation.setEndValue(EndValue)
        if callback: 
            self.Animation.finished.connect(callback)
        self.Animation.start()
    
    def DeleteTmpImage(self, tmp_file: str) -> None:
        os.remove(tmp_file)
        os.rmdir(os.path.dirname(tmp_file))