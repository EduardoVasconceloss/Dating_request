# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_ui_uiCniXIn.ui'
##
# Created by: Qt User Interface Compiler version 6.3.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QSizePolicy, QWidget)
import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(462, 450)
        MainWindow.setMaximumSize(QSize(450, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
                                         "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 138, 173, 255), stop:0.55 rgba(235, 169, 221, 255), stop:0.98 rgba(214, 159, 195, 255), stop:1 rgba(0, 0, 0, 0));\n"
                                         "}\n"
                                         "\n"
                                         "QLabel#question{\n"
                                         "	font-size: 35px;\n"
                                         "	font-weight: bold;\n"
                                         "	color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton{\n"
                                         "   border: 2px solid white;\n"
                                         "	font-size: 20px;\n"
                                         "   font-weight: bold;\n"
                                         "	color: rgba(255, 138, 173, 255);\n"
                                         "	min-height: 45px;\n"
                                         "	border-radius: 20px;\n"
                                         "	background-color: white;\n"
                                         "}\n"
                                         "")
        self.question = QLabel(self.centralwidget)
        self.question.setObjectName(u"question")
        self.question.setGeometry(QRect(10, 10, 431, 71))
        self.question.setAlignment(Qt.AlignCenter)
        self.yes_frame = QFrame(self.centralwidget)
        self.yes_frame.setObjectName(u"yes_frame")
        self.yes_frame.setGeometry(QRect(70, 193, 141, 91))
        self.yes_frame.setFrameShape(QFrame.NoFrame)
        self.yes_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.yes_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_button = QPushButton(self.yes_frame)
        self.yes_button.setObjectName(u"yes_button")

        self.horizontalLayout.addWidget(self.yes_button)

        self.no_frame = QFrame(self.centralwidget)
        self.no_frame.setObjectName(u"no_frame")
        self.no_frame.setGeometry(QRect(254, 193, 141, 91))
        self.no_frame.setFrameShape(QFrame.NoFrame)
        self.no_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.no_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.no_button = QPushButton(self.no_frame)
        self.no_button.setObjectName(u"no_button")

        self.horizontalLayout_2.addWidget(self.no_button)

        self.heart = QLabel(self.centralwidget)
        self.heart.setObjectName(u"heart")
        self.heart.setGeometry(QRect(70, 120, 321, 281))
        self.heart.setStyleSheet(u"")
        self.heart.setPixmap(QPixmap(u":/icons/Heart.png"))
        self.heart.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.question.setText(QCoreApplication.translate(
            "MainWindow", u"Do you wanna date me?", None))
        self.yes_button.setText(
            QCoreApplication.translate("MainWindow", u"Yes", None))
        self.no_button.setText(
            QCoreApplication.translate("MainWindow", u"No", None))
        self.heart.setText("")
    # retranslateUi
