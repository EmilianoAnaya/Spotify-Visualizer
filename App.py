from backend.visualizer_song import Visualizer_Song
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Main = Visualizer_Song()
    Main.show()
    sys.exit(App.exec())