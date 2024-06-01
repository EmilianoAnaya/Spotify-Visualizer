from backend.visualizer_setup import Visualizersetup
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Main = Visualizersetup()
    Main.show()
    sys.exit(App.exec())