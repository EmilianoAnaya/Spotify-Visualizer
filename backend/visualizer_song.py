from resources.constants.SPOTIFY_CREDENTIALS import CLIENT_ID, CLIENT_SECRET, REDIRECT_UI
from PySide6.QtCore import QTimer, Qt
from frontend.ui_visualizer_song import Ui_Visualizer_Song
from PySide6.QtWidgets import QMainWindow
from spotipy.oauth2 import SpotifyOAuth
import tempfile
import requests
import spotipy
import os

class Visualizer_Song(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Visualizer_Song()
        self.ui.setupUi(self)

        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_UI, scope="user-read-playback-state"))
        self.CurrentTrack:str = ""
        self.tmp_file_path: str = ""

        self.ui.label_SongArtist.setVisible(False)
        self.ui.label_SongName.setVisible(False)
        self.mouse_pressed = False
        self.old_pos = None

        self.CheckTimer = QTimer()
        self.CheckTimer.setInterval(4000)
        self.CheckTimer.timeout.connect(self.CheckCurrentTrack)
        self.CheckTimer.start()

    def truncate_text(self, text: str, label) -> str:
        font_metrics = label.fontMetrics()
        elided_text = font_metrics.elidedText(text, Qt.ElideRight, label.width())
        return elided_text
    
    def setSongInfo(self, SongName:str, Artists:list) -> None:
        self.ui.label_SongArtist.setVisible(True)
        self.ui.label_SongName.setVisible(True)

        Truncate_song_name = self.truncate_text(SongName, self.ui.label_SongName)
        self.ui.label_SongName.setText(Truncate_song_name)

        results = ' - '.join(artists['name'] for artists in Artists)
        self.ui.label_SongArtist.setText(results)
    
    def setAlbumCover(self, AlbumCover: str):
        getImage = requests.get(AlbumCover)
        tmp_dir = tempfile.mkdtemp(dir="resources/images/tmp_covers")
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
            delete_tmp_file = self.tmp_file_path
            self.tmp_file_path = self.setAlbumCover(results['item']['album']['images'][1]["url"])
            self.setSongInfo(results['item']['name'],results['item']['artists'])
            if delete_tmp_file != "":
                self.DeleteTmpImage(delete_tmp_file)

    def closeEvent(self,event):
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

    def DeleteTmpImage(self, tmp_file: str) -> None:
        os.remove(tmp_file)
        os.rmdir(os.path.dirname(tmp_file))