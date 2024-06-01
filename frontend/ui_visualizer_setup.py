# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_VisualizerSetup(object):
    def setupUi(self, VisualizerSetup):
        if not VisualizerSetup.objectName():
            VisualizerSetup.setObjectName(u"VisualizerSetup")
        VisualizerSetup.resize(440, 303)
        VisualizerSetup.setMinimumSize(QSize(440, 303))
        VisualizerSetup.setMaximumSize(QSize(440, 303))
        self.centralwidget = QWidget(VisualizerSetup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	border-image: url(resources/images/Spotify_visualizer_logo.png);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(440, 450))
        self.widget.setStyleSheet(u"#widget{\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.502699, fy:0.495, stop:0 rgba(37, 37, 37, 246), stop:1 rgba(45, 45, 45, 224));\n"
"}\n"
"\n"
"#lbl_Title{\n"
"	font-weight: bold;\n"
"	font-size:20px;\n"
"}\n"
"\n"
"#lbl_Description{\n"
"	font-size:11px\n"
"}\n"
"\n"
"QLabel{\n"
"	font-family:Verdana;\n"
"}\n"
"\n"
"QPushButton{\n"
"	font-family:verdana;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_Title = QLabel(self.widget_4)
        self.lbl_Title.setObjectName(u"lbl_Title")

        self.verticalLayout_4.addWidget(self.lbl_Title, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lbl_Description = QLabel(self.widget_4)
        self.lbl_Description.setObjectName(u"lbl_Description")

        self.verticalLayout_4.addWidget(self.lbl_Description, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_2.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_ClientID = QLabel(self.widget_2)
        self.lbl_ClientID.setObjectName(u"lbl_ClientID")
        self.lbl_ClientID.setMinimumSize(QSize(70, 15))
        self.lbl_ClientID.setMaximumSize(QSize(54, 15))

        self.verticalLayout_3.addWidget(self.lbl_ClientID, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.txt_ClientID = QLineEdit(self.widget_2)
        self.txt_ClientID.setObjectName(u"txt_ClientID")
        self.txt_ClientID.setMinimumSize(QSize(250, 0))

        self.verticalLayout_3.addWidget(self.txt_ClientID, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_ClientSecret = QLabel(self.widget_3)
        self.lbl_ClientSecret.setObjectName(u"lbl_ClientSecret")

        self.verticalLayout_5.addWidget(self.lbl_ClientSecret)

        self.txt_ClientSecret = QLineEdit(self.widget_3)
        self.txt_ClientSecret.setObjectName(u"txt_ClientSecret")
        self.txt_ClientSecret.setMinimumSize(QSize(250, 0))

        self.verticalLayout_5.addWidget(self.txt_ClientSecret, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_Submit = QPushButton(self.widget)
        self.btn_Submit.setObjectName(u"btn_Submit")
        self.btn_Submit.setMinimumSize(QSize(100, 40))

        self.verticalLayout_2.addWidget(self.btn_Submit, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.widget)

        VisualizerSetup.setCentralWidget(self.centralwidget)

        self.retranslateUi(VisualizerSetup)

        QMetaObject.connectSlotsByName(VisualizerSetup)
    # setupUi

    def retranslateUi(self, VisualizerSetup):
        VisualizerSetup.setWindowTitle(QCoreApplication.translate("VisualizerSetup", u"Setup", None))
        self.lbl_Title.setText(QCoreApplication.translate("VisualizerSetup", u"Spotify Visualizer", None))
        self.lbl_Description.setText(QCoreApplication.translate("VisualizerSetup", u"Insert your Spotify Credentials so you the widget can authenticate the \n"
"session at your dashboard app", None))
        self.lbl_ClientID.setText(QCoreApplication.translate("VisualizerSetup", u"CLIENT_ID", None))
        self.txt_ClientID.setText("")
        self.lbl_ClientSecret.setText(QCoreApplication.translate("VisualizerSetup", u"CLIENT_SECRET", None))
        self.btn_Submit.setText(QCoreApplication.translate("VisualizerSetup", u"Submit", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    App = QApplication(sys.argv)
    Main = QMainWindow()
    Ui = Ui_VisualizerSetup()
    Ui.setupUi(Main)
    Main.show()
    sys.exit(App.exec())