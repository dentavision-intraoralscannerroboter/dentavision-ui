# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 659)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #f5f5f5;")
        self.topPanel = QFrame(self.centralwidget)
        self.topPanel.setObjectName(u"topPanel")
        self.topPanel.setGeometry(QRect(10, 10, 1069, 64))
        self.topPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.topPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.topPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.topPanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(2)
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLabel = QLabel(self.topPanel)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(175, 19))
        self.titleLabel.setStyleSheet(u"color: #0E7772;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"font-family: \"Helvetica\"")
        self.titleLabel.setMidLineWidth(1)

        self.titleLayout.addWidget(self.titleLabel)

        self.subtitleLabel = QLabel(self.topPanel)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        self.subtitleLabel.setMinimumSize(QSize(175, 0))
        self.subtitleLabel.setStyleSheet(u"color: #455360;\n"
"font-size: 17px;\n"
"font-family: \"Helvetica\"\n"
"")

        self.titleLayout.addWidget(self.subtitleLabel)


        self.horizontalLayout.addLayout(self.titleLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.startButton = QPushButton(self.topPanel)
        self.startButton.setObjectName(u"startButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setStyleSheet(u"background-color: #0E7772;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 10px;\n"
"padding: 6px 20px;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.startButton)

        self.leftPanel = QFrame(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setGeometry(QRect(12, 89, 283, 490))
        self.leftPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.leftPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.toothLabel = QLabel(self.leftPanel)
        self.toothLabel.setObjectName(u"toothLabel")
        self.toothLabel.setGeometry(QRect(10, 10, 251, 21))
        self.toothLabel.setAutoFillBackground(False)
        self.toothLabel.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.toothIconLabel = QLabel(self.leftPanel)
        self.toothIconLabel.setObjectName(u"toothIconLabel")
        self.toothIconLabel.setGeometry(QRect(10, 50, 63, 63))
        self.toothIconLabel.setPixmap(QPixmap(u"../tooth_circle.svg"))
        self.toothIconLabel.setScaledContents(True)
        self.selectATooth = QLabel(self.leftPanel)
        self.selectATooth.setObjectName(u"selectATooth")
        self.selectATooth.setGeometry(QRect(82, 83, 181, 16))
        self.selectATooth.setStyleSheet(u"color: #768599;\n"
"font-family: \"Helvetica\";")
        self.noToothSelected = QLabel(self.leftPanel)
        self.noToothSelected.setObjectName(u"noToothSelected")
        self.noToothSelected.setGeometry(QRect(83, 62, 147, 21))
        self.noToothSelected.setStyleSheet(u"font-size: 17px;\n"
"font-weight: 450;\n"
"color: #455360;\n"
"")
        self.toothTargetFrame = QFrame(self.leftPanel)
        self.toothTargetFrame.setObjectName(u"toothTargetFrame")
        self.toothTargetFrame.setGeometry(QRect(0, 130, 281, 161))
        self.toothTargetFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.toothTargetFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.toothTargetFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toothTarget = QLabel(self.toothTargetFrame)
        self.toothTarget.setObjectName(u"toothTarget")
        self.toothTarget.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.verticalLayout.addWidget(self.toothTarget)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, 10, -1)
        self.Y = QLabel(self.toothTargetFrame)
        self.Y.setObjectName(u"Y")
        self.Y.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";\n"
"")
        self.Y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.Y, 0, 1, 1, 1)

        self.X = QLabel(self.toothTargetFrame)
        self.X.setObjectName(u"X")
        self.X.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.X.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.X, 0, 0, 1, 1)

        self.Z = QLabel(self.toothTargetFrame)
        self.Z.setObjectName(u"Z")
        self.Z.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.Z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.Z, 0, 2, 1, 1)

        self.labelX = QLabel(self.toothTargetFrame)
        self.labelX.setObjectName(u"labelX")
        self.labelX.setStyleSheet(u"color: #0E7772")
        self.labelX.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.labelX, 1, 0, 1, 1)

        self.labelY = QLabel(self.toothTargetFrame)
        self.labelY.setObjectName(u"labelY")
        self.labelY.setStyleSheet(u"color: #0E7772")
        self.labelY.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.labelY, 1, 1, 1, 1)

        self.labelZ = QLabel(self.toothTargetFrame)
        self.labelZ.setObjectName(u"labelZ")
        self.labelZ.setStyleSheet(u"color: #0E7772")
        self.labelZ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.labelZ, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, 10, -1)
        self.RY = QLabel(self.toothTargetFrame)
        self.RY.setObjectName(u"RY")
        self.RY.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.RY.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.RY, 0, 1, 1, 1)

        self.RZ = QLabel(self.toothTargetFrame)
        self.RZ.setObjectName(u"RZ")
        self.RZ.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.RZ.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.RZ, 0, 2, 1, 1)

        self.labelX_2 = QLabel(self.toothTargetFrame)
        self.labelX_2.setObjectName(u"labelX_2")
        self.labelX_2.setStyleSheet(u"color: #0E7772")
        self.labelX_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.labelX_2, 1, 0, 1, 1)

        self.labelY_2 = QLabel(self.toothTargetFrame)
        self.labelY_2.setObjectName(u"labelY_2")
        self.labelY_2.setStyleSheet(u"color: #0E7772")
        self.labelY_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.labelY_2, 1, 1, 1, 1)

        self.labelZ_2 = QLabel(self.toothTargetFrame)
        self.labelZ_2.setObjectName(u"labelZ_2")
        self.labelZ_2.setStyleSheet(u"color: #0E7772")
        self.labelZ_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.labelZ_2, 1, 2, 1, 1)

        self.RX = QLabel(self.toothTargetFrame)
        self.RX.setObjectName(u"RX")
        self.RX.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.RX.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.RX, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.motionControl = QFrame(self.leftPanel)
        self.motionControl.setObjectName(u"motionControl")
        self.motionControl.setGeometry(QRect(0, 290, 281, 191))
        self.motionControl.setFrameShape(QFrame.Shape.StyledPanel)
        self.motionControl.setFrameShadow(QFrame.Shadow.Raised)
        self.toothTarget_2 = QLabel(self.motionControl)
        self.toothTarget_2.setObjectName(u"toothTarget_2")
        self.toothTarget_2.setGeometry(QRect(12, 10, 151, 41))
        self.toothTarget_2.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.centerPanel = QFrame(self.centralwidget)
        self.centerPanel.setObjectName(u"centerPanel")
        self.centerPanel.setGeometry(QRect(310, 89, 458, 490))
        self.centerPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.centerPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.centerPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.maxilla = QLabel(self.centerPanel)
        self.maxilla.setObjectName(u"maxilla")
        self.maxilla.setGeometry(QRect(160, 10, 141, 16))
        self.maxilla.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.mandibula = QLabel(self.centerPanel)
        self.mandibula.setObjectName(u"mandibula")
        self.mandibula.setGeometry(QRect(160, 460, 171, 16))
        self.mandibula.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.mouthFrame = QFrame(self.centerPanel)
        self.mouthFrame.setObjectName(u"mouthFrame")
        self.mouthFrame.setGeometry(QRect(10, 30, 431, 411))
        self.mouthFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mouthFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.rightTopPanel = QFrame(self.centralwidget)
        self.rightTopPanel.setObjectName(u"rightTopPanel")
        self.rightTopPanel.setGeometry(QRect(783, 89, 285, 279))
        self.rightTopPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.rightTopPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightTopPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.headPositionLabel = QLabel(self.rightTopPanel)
        self.headPositionLabel.setObjectName(u"headPositionLabel")
        self.headPositionLabel.setGeometry(QRect(10, 10, 111, 16))
        self.headPositionLabel.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.leftBottomPanel = QFrame(self.centralwidget)
        self.leftBottomPanel.setObjectName(u"leftBottomPanel")
        self.leftBottomPanel.setGeometry(QRect(783, 410, 285, 166))
        self.leftBottomPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;\n"
"font-size:17px;\n"
"")
        self.leftBottomPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftBottomPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.statusLabel = QLabel(self.leftBottomPanel)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(10, 10, 91, 16))
        self.statusLabel.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.faceDetectedLabel = QLabel(self.leftBottomPanel)
        self.faceDetectedLabel.setObjectName(u"faceDetectedLabel")
        self.faceDetectedLabel.setGeometry(QRect(20, 40, 211, 16))
        self.faceDetectedLabel.setStyleSheet(u"   color: #11AC00;\n"
"   font-weight: 600;\n"
"   font-size: 11px;")
        self.stabilizationSuccessfulLabel = QLabel(self.leftBottomPanel)
        self.stabilizationSuccessfulLabel.setObjectName(u"stabilizationSuccessfulLabel")
        self.stabilizationSuccessfulLabel.setGeometry(QRect(20, 60, 211, 16))
        self.stabilizationSuccessfulLabel.setStyleSheet(u"   color: #11AC00;\n"
"   font-weight: 600;\n"
"   font-size: 11px;")
        self.jointsAreMovingLabel = QLabel(self.leftBottomPanel)
        self.jointsAreMovingLabel.setObjectName(u"jointsAreMovingLabel")
        self.jointsAreMovingLabel.setGeometry(QRect(20, 80, 211, 16))
        self.jointsAreMovingLabel.setStyleSheet(u"   color: #11AC00;\n"
"   font-weight: 600;\n"
"   font-size: 11px;")
        self.headIsNotStabilizedLabel = QLabel(self.leftBottomPanel)
        self.headIsNotStabilizedLabel.setObjectName(u"headIsNotStabilizedLabel")
        self.headIsNotStabilizedLabel.setGeometry(QRect(20, 60, 211, 16))
        self.headIsNotStabilizedLabel.setStyleSheet(u"   color: #FCAD09;\n"
"   font-weight: 600;\n"
"   font-size: 11px;")
        self.scanningLabel = QLabel(self.leftBottomPanel)
        self.scanningLabel.setObjectName(u"scanningLabel")
        self.scanningLabel.setGeometry(QRect(20, 80, 211, 16))
        self.scanningLabel.setStyleSheet(u"   color: #11AC00;\n"
"   font-weight: 600;\n"
"   font-size: 11px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1089, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DentaVision Control Panel", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>DentaVision<br/></p></body></html>", None))
        self.subtitleLabel.setText(QCoreApplication.translate("MainWindow", u"Control Panel", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.toothLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">SELECTED TOOTH</span></p></body></html>", None))
        self.toothIconLabel.setText("")
        self.selectATooth.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Select a tooth from the chart</span></p></body></html>", None))
        self.noToothSelected.setText(QCoreApplication.translate("MainWindow", u"No tooth selected", None))
        self.toothTarget.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">TOOTH TARGET</span></p></body></html>", None))
        self.Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.labelX.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.labelY.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.labelZ.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.RY.setText(QCoreApplication.translate("MainWindow", u"YAW", None))
        self.RZ.setText(QCoreApplication.translate("MainWindow", u"ROLL", None))
        self.labelX_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.labelY_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.labelZ_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.RX.setText(QCoreApplication.translate("MainWindow", u"PITCH", None))
        self.toothTarget_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">JOINT CONTROL</span></p></body></html>", None))
        self.maxilla.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>MAXILLA (UPPER JAW)</p><p><br/></p></body></html>", None))
        self.mandibula.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>MANDIBULA (LOWER JAW)</p></body></html>", None))
        self.headPositionLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">HEAD POSITION</span></p></body></html>", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">STATUS</span></p></body></html>", None))
        self.faceDetectedLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u25cf FACE DETECTED</span></p></body></html>", None))
        self.stabilizationSuccessfulLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u25cf STABILIZATION SUCCESSFUL</span></p></body></html>", None))
        self.jointsAreMovingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u25cf JOINTS ARE MOVING</span></p></body></html>", None))
        self.headIsNotStabilizedLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u25cf HEAD IS NOT STABILIZED</span></p></body></html>", None))
        self.scanningLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u25cf SCANNING...</span></p></body></html>", None))
    # retranslateUi

