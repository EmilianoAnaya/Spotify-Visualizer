from frontend.ui_visualizer_setup import Ui_VisualizerSetup
from backend.SpotifyAuth import get_Spotify
from PySide6.QtWidgets import QMainWindow
import json
import os

class Visualizersetup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VisualizerSetup()
        self.ui.setupUi(self)
        self.spotify = None
        if os.path.exists(".cache"):    
            os.remove(".cache")

        print("DO NOT CLOSE THIS WINDOW, YOU'LL NEED IT FOR THE REDIRECT URI FOR THE AUTHENTICATION!")

        self.ui.btn_Submit.pressed.connect(self.Submit)

    def CheckUser(self, CLIENT_ID, CLIENT_SECRET):
        self.spotify.current_user()
        if os.path.exists(".cache"):
            data =  {
                        "Client_ID": CLIENT_ID,
                        "Client_Secret": CLIENT_SECRET
                    }
            with open('resources/credentials/data.json',"w") as file:
                json.dump(data,file,indent=4)
            print("Success, you may now close this window and execute App.vbs\nWARNING: If you open up this file again, the Access Token will be lost and you'll have to\nregister your credentials again.")

    
    def Submit(self):
        CLIENT_ID = self.ui.txt_ClientID.text().strip()
        CLIENT_SECRET = self.ui.txt_ClientSecret.text().strip()
        if not CLIENT_ID or not CLIENT_SECRET:
            print("ERROR, FILL ALL THE FIELDS CORRECTLY")
            return
        self.spotify = get_Spotify(CLIENT_ID,CLIENT_SECRET)
        self.CheckUser(CLIENT_ID, CLIENT_SECRET)