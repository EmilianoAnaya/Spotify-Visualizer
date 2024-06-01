# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'visualizer_song.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Visualizer_Song(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 300)
        MainWindow.setMinimumSize(QSize(1115, 300))
        MainWindow.setMaximumSize(QSize(1115, 300))
        MainWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1115, 300))
        self.centralwidget.setMaximumSize(QSize(1115, 300))
        self.centralwidget.setStyleSheet(u"#widget_AlbumCover{\n"
"	border-radius: 20px;\n"
"}\n"
"#widget_Song{\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"}\n"
"")

        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_AlbumCover = QWidget(self.centralwidget)
        self.widget_AlbumCover.setObjectName(u"widget_AlbumCover")
        self.widget_AlbumCover.setMinimumSize(QSize(300, 300))
        self.widget_AlbumCover.setMaximumSize(QSize(300, 300))
        self.widget_AlbumCover.setStyleSheet(u"#widget_AlbumCover{\n"
"	\n"
"	border-image: url(resources/images/Spotify_visualizer_logo.png);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_AlbumCover)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.widget_AlbumCover, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.widget_Song = QWidget(self.centralwidget)
        self.widget_Song.setObjectName(u"widget_Song")
        self.widget_Song.setMinimumSize(QSize(815, 0))
        self.widget_Song.setMaximumSize(QSize(0, 210))
        self.widget_Song.setStyleSheet(u"#widget_Song{\n"
"	border-image: url(resources/images/Spotify_visualizer_logo.png);\n"
"}\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_Song)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_InfoSong = QWidget(self.widget_Song)
        self.widget_InfoSong.setObjectName(u"widget_InfoSong")
        self.widget_InfoSong.setMinimumSize(QSize(815,210))
        self.widget_InfoSong.setMaximumSize(QSize(0,210))
        self.widget_InfoSong.setStyleSheet(u"#widget_InfoSong{\n"
"	/*background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.499963, fy:0.506, stop:0 rgba(1, 1, 1, 173), stop:1 rgba(111, 111, 111, 255));*/\n"
"	\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.499963, fy:0.506, stop:0 rgba(1, 1, 1, 173), stop:1 rgba(0, 0, 0, 255));\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#label_SongName{\n"
"	font-family: Verdana;\n"
"	font-size: 30px;\n"
"	font-style: italic;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#label_SongArtist{\n"
"	font-family: Verdana;\n"
"	font-size: 15px;\n"
"	font-weight: bold;	\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_InfoSong)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget_InfoSong)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(62, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_SongName = QLabel(self.widget_2)
        self.label_SongName.setObjectName(u"label_SongName")
        self.label_SongName.setMinimumSize(QSize(750, 0))
        self.label_SongName.setMaximumSize(QSize(750, 16777215))

        self.horizontalLayout_2.addWidget(self.label_SongName, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_InfoSong)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(62, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_SongArtist = QLabel(self.widget_3)
        self.label_SongArtist.setObjectName(u"label_SongArtist")
        self.label_SongArtist.setMinimumSize(QSize(750, 0))

        self.horizontalLayout_3.addWidget(self.label_SongArtist, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget_InfoSong)


        self.horizontalLayout.addWidget(self.widget_Song)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_SongName.setText(QCoreApplication.translate("MainWindow", u"Waiting for a Song to Track", None))
        self.label_SongArtist.setText(QCoreApplication.translate("MainWindow", u"Select a song from your Spotify", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    Ui = Ui_Visualizer_Song()
    Ui.setupUi(window)
    window.show()
    sys.exit(app.exec())