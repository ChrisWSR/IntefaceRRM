# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 440)
        MainWindow.setStyleSheet("*{\n"
"   border: none;\n"
"   background-color: transparent;\n"
"   background: transparent;\n"
"   padding: 0;\n"
"   margin: 0 ;\n"
"   color: #fff;\n"
"}\n"
"#body{\n"
"   background-color: transparent;\n"
"}\n"
"#centralwidget{\n"
"   background-color: #212121;\n"
"}\n"
"#header{\n"
"   background-color: #303030;\n"
"}\n"
"#leftMenuContainer {\n"
"   background-color: #303030;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"    text-align: left;\n"
"    padding: 7px 12px ;\n"
"}\n"
"#rightMenuContainer_main {\n"
"   background-color: #303030;\n"
"}\n"
"#rightMenuContainer_camera{\n"
"   background-color: #303030;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QFrame(self.header)
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.logo)
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.imgLogo = QtWidgets.QLabel(self.logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgLogo.sizePolicy().hasHeightForWidth())
        self.imgLogo.setSizePolicy(sizePolicy)
        self.imgLogo.setMinimumSize(QtCore.QSize(220, 0))
        self.imgLogo.setText("")
        self.imgLogo.setPixmap(QtGui.QPixmap(":/logo/logo.png"))
        self.imgLogo.setObjectName("imgLogo")
        self.horizontalLayout_7.addWidget(self.imgLogo)
        self.horizontalLayout.addWidget(self.logo)
        self.txtLaboratory = QtWidgets.QFrame(self.header)
        self.txtLaboratory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.txtLaboratory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.txtLaboratory.setObjectName("txtLaboratory")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.txtLaboratory)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txtLaboratory_2 = QtWidgets.QLabel(self.txtLaboratory)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtLaboratory_2.sizePolicy().hasHeightForWidth())
        self.txtLaboratory_2.setSizePolicy(sizePolicy)
        self.txtLaboratory_2.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        self.txtLaboratory_2.setFont(font)
        self.txtLaboratory_2.setAlignment(QtCore.Qt.AlignCenter)
        self.txtLaboratory_2.setObjectName("txtLaboratory_2")
        self.horizontalLayout_4.addWidget(self.txtLaboratory_2)
        self.horizontalLayout.addWidget(self.txtLaboratory)
        self.windowButtonFrame = QtWidgets.QFrame(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowButtonFrame.sizePolicy().hasHeightForWidth())
        self.windowButtonFrame.setSizePolicy(sizePolicy)
        self.windowButtonFrame.setMinimumSize(QtCore.QSize(220, 0))
        self.windowButtonFrame.setAcceptDrops(False)
        self.windowButtonFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.windowButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.windowButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windowButtonFrame.setObjectName("windowButtonFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.windowButtonFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.windowButtonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3.addWidget(self.frame)
        self.btns = QtWidgets.QFrame(self.windowButtonFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btns.sizePolicy().hasHeightForWidth())
        self.btns.setSizePolicy(sizePolicy)
        self.btns.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btns.setObjectName("btns")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.btns)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnMinimize = QtWidgets.QPushButton(self.btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMinimize.sizePolicy().hasHeightForWidth())
        self.btnMinimize.setSizePolicy(sizePolicy)
        self.btnMinimize.setMinimumSize(QtCore.QSize(0, 0))
        self.btnMinimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMinimize.setIcon(icon)
        self.btnMinimize.setIconSize(QtCore.QSize(18, 24))
        self.btnMinimize.setObjectName("btnMinimize")
        self.horizontalLayout_5.addWidget(self.btnMinimize)
        self.btnRestore = QtWidgets.QPushButton(self.btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRestore.sizePolicy().hasHeightForWidth())
        self.btnRestore.setSizePolicy(sizePolicy)
        self.btnRestore.setMinimumSize(QtCore.QSize(30, 0))
        self.btnRestore.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRestore.setIcon(icon1)
        self.btnRestore.setIconSize(QtCore.QSize(16, 16))
        self.btnRestore.setObjectName("btnRestore")
        self.horizontalLayout_5.addWidget(self.btnRestore)
        self.btnClose = QtWidgets.QPushButton(self.btns)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setMinimumSize(QtCore.QSize(30, 0))
        self.btnClose.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon2)
        self.btnClose.setIconSize(QtCore.QSize(12, 12))
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_5.addWidget(self.btnClose)
        self.horizontalLayout_3.addWidget(self.btns)
        self.horizontalLayout.addWidget(self.windowButtonFrame)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.body = QtWidgets.QWidget(self.centralwidget)
        self.body.setObjectName("body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftMenuContainer = QtWidgets.QWidget(self.body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leftMenuSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sectionsMenuFrame = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sectionsMenuFrame.sizePolicy().hasHeightForWidth())
        self.sectionsMenuFrame.setSizePolicy(sizePolicy)
        self.sectionsMenuFrame.setMinimumSize(QtCore.QSize(0, 130))
        self.sectionsMenuFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sectionsMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sectionsMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sectionsMenuFrame.setObjectName("sectionsMenuFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sectionsMenuFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.homeBtn = QtWidgets.QPushButton(self.sectionsMenuFrame)
        self.homeBtn.setStyleSheet("background-color: #3E3E3E")
        self.homeBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/align.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon3)
        self.homeBtn.setIconSize(QtCore.QSize(24, 24))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_4.addWidget(self.homeBtn)
        self.cameraBtn = QtWidgets.QPushButton(self.sectionsMenuFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.cameraBtn.setFont(font)
        self.cameraBtn.setObjectName("cameraBtn")
        self.verticalLayout_4.addWidget(self.cameraBtn)
        self.sensorsBtn = QtWidgets.QPushButton(self.sectionsMenuFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensorsBtn.sizePolicy().hasHeightForWidth())
        self.sensorsBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sensorsBtn.setFont(font)
        self.sensorsBtn.setObjectName("sensorsBtn")
        self.verticalLayout_4.addWidget(self.sensorsBtn)
        self.rocksBdBtn = QtWidgets.QPushButton(self.sectionsMenuFrame)
        self.rocksBdBtn.setText("")
        self.rocksBdBtn.setObjectName("rocksBdBtn")
        self.verticalLayout_4.addWidget(self.rocksBdBtn)
        self.verticalLayout_3.addWidget(self.sectionsMenuFrame, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.systemMenuFrame = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.systemMenuFrame.sizePolicy().hasHeightForWidth())
        self.systemMenuFrame.setSizePolicy(sizePolicy)
        self.systemMenuFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.systemMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.systemMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.systemMenuFrame.setObjectName("systemMenuFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.systemMenuFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.systemInfoBtn = QtWidgets.QPushButton(self.systemMenuFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.systemInfoBtn.setFont(font)
        self.systemInfoBtn.setObjectName("systemInfoBtn")
        self.verticalLayout_5.addWidget(self.systemInfoBtn)
        self.verticalLayout_3.addWidget(self.systemMenuFrame, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.leftMenuSubContainer, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_2.addWidget(self.leftMenuContainer, 0, QtCore.Qt.AlignLeft)
        self.centerContainer = QtWidgets.QWidget(self.body)
        self.centerContainer.setObjectName("centerContainer")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centerContainer)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.stackedWidgetCenter = QtWidgets.QStackedWidget(self.centerContainer)
        self.stackedWidgetCenter.setObjectName("stackedWidgetCenter")
        self.mainSection = QtWidgets.QWidget()
        self.mainSection.setObjectName("mainSection")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.mainSection)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mainSection_container = QtWidgets.QWidget(self.mainSection)
        self.mainSection_container.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mainSection_container.setObjectName("mainSection_container")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mainSection_container)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_8.addWidget(self.mainSection_container)
        self.stackedWidgetCenter.addWidget(self.mainSection)
        self.sensorSection = QtWidgets.QWidget()
        self.sensorSection.setObjectName("sensorSection")
        self.stackedWidgetCenter.addWidget(self.sensorSection)
        self.cameraSection = QtWidgets.QWidget()
        self.cameraSection.setObjectName("cameraSection")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.cameraSection)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cameraContainer = QtWidgets.QWidget(self.cameraSection)
        self.cameraContainer.setObjectName("cameraContainer")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.cameraContainer)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.stackedWidget_camera = QtWidgets.QStackedWidget(self.cameraContainer)
        self.stackedWidget_camera.setObjectName("stackedWidget_camera")
        self.cameraPage = QtWidgets.QWidget()
        self.cameraPage.setObjectName("cameraPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.cameraPage)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cameraFramePage = QtWidgets.QLabel(self.cameraPage)
        self.cameraFramePage.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.cameraFramePage.setFrameShadow(QtWidgets.QLabel.Raised)
        self.cameraFramePage.setObjectName("cameraFramePage")
        self.verticalLayout_6.addWidget(self.cameraFramePage)
        self.stackedWidget_camera.addWidget(self.cameraPage)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget_camera.addWidget(self.page_3)
        self.verticalLayout_12.addWidget(self.stackedWidget_camera)
        self.horizontalLayout_9.addWidget(self.cameraContainer)
        self.rightMenuContainer_camera = QtWidgets.QWidget(self.cameraSection)
        self.rightMenuContainer_camera.setObjectName("rightMenuContainer_camera")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.rightMenuContainer_camera)
        self.verticalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.rightMenuSections_camera = QtWidgets.QFrame(self.rightMenuContainer_camera)
        self.rightMenuSections_camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightMenuSections_camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightMenuSections_camera.setObjectName("rightMenuSections_camera")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.rightMenuSections_camera)
        self.verticalLayout_9.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.turnOnCamera = QtWidgets.QPushButton(self.rightMenuSections_camera)
        self.turnOnCamera.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/turnOn.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.turnOnCamera.setIcon(icon4)
        self.turnOnCamera.setObjectName("turnOnCamera")
        self.verticalLayout_9.addWidget(self.turnOnCamera)
        self.turnOffCamera = QtWidgets.QPushButton(self.rightMenuSections_camera)
        self.turnOffCamera.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/turnOff.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.turnOffCamera.setIcon(icon5)
        self.turnOffCamera.setIconSize(QtCore.QSize(19, 19))
        self.turnOffCamera.setObjectName("turnOffCamera")
        self.verticalLayout_9.addWidget(self.turnOffCamera)
        self.pauseCamera = QtWidgets.QPushButton(self.rightMenuSections_camera)
        self.pauseCamera.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseCamera.setIcon(icon6)
        self.pauseCamera.setIconSize(QtCore.QSize(20, 20))
        self.pauseCamera.setObjectName("pauseCamera")
        self.verticalLayout_9.addWidget(self.pauseCamera)
        self.screenshot = QtWidgets.QPushButton(self.rightMenuSections_camera)
        self.screenshot.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/capture.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenshot.setIcon(icon7)
        self.screenshot.setIconSize(QtCore.QSize(20, 20))
        self.screenshot.setObjectName("screenshot")
        self.verticalLayout_9.addWidget(self.screenshot)
        self.verticalLayout_8.addWidget(self.rightMenuSections_camera)
        self.frame_camera = QtWidgets.QFrame(self.rightMenuContainer_camera)
        self.frame_camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_camera.setObjectName("frame_camera")
        self.verticalLayout_8.addWidget(self.frame_camera)
        self.horizontalLayout_9.addWidget(self.rightMenuContainer_camera, 0, QtCore.Qt.AlignRight)
        self.stackedWidgetCenter.addWidget(self.cameraSection)
        self.horizontalLayout_6.addWidget(self.stackedWidgetCenter)
        self.horizontalLayout_2.addWidget(self.centerContainer)
        self.verticalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





        self.turnOnCamera.clicked.connect(self.start_video)


    def start_video(self):
        self.ThreadClass = ThreadClass()
        self.ThreadClass.start()
        self.ThreadClass.Imageupd.connect(self.Imageupd_slot)

    def stop_video(self):
        if hasattr(self, 'ThreadClass') and self.ThreadClass.isRunning():
            self.ThreadClass.stop()
            self.ThreadClass.wait()
            self.camera_running = False


#Qt.KeepAspectRatio

    # def Imageupd_slot(self, Image):
    #     label_size = self.cameraFramePage.size()
    #     scaled_image = Image.scaled(label_size, Qt.IgnoreAspectRatio)
    #     self.cameraFramePage.setPixmap(QPixmap.fromImage(scaled_image))

    def Imageupd_slot(self, Image):
        label_size = self.cameraFramePage.size()
        # Obtiene las dimensiones de la imagen y el contenedor
        image_size = Image.size()
        container_width, container_height = label_size.width(), label_size.height()
        # Calcula la escala para mantener la relación de aspecto
        width_ratio = container_width / image_size.width()
        height_ratio = container_height / image_size.height()
        scale_factor = min(width_ratio, height_ratio)
        # Escala la imagen proporcionalmente
        scaled_image = Image.scaled(image_size * scale_factor, Qt.KeepAspectRatio)
  
        # Calcula el área para centrar la imagen en el contenedor
        x_offset = (container_width - scaled_image.width()) / 2
        y_offset = (container_height - scaled_image.height()) / 2
        # Crea un pixmap y lo muestra en el QLabel
        pixmap = QPixmap.fromImage(scaled_image)
        self.cameraFramePage.setPixmap(pixmap)
        self.cameraFramePage.setAlignment(Qt.AlignCenter)

    def toggle_pause(self):
        self.paused = not self.paused
    




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txtLaboratory_2.setText(_translate("MainWindow", "Laboratory"))
        self.cameraBtn.setToolTip(_translate("MainWindow", "Camera"))
        self.cameraBtn.setText(_translate("MainWindow", "Camera"))
        self.sensorsBtn.setToolTip(_translate("MainWindow", "Sensors"))
        self.sensorsBtn.setText(_translate("MainWindow", "Sensors"))
        self.systemInfoBtn.setToolTip(_translate("MainWindow", "System Information"))
        self.systemInfoBtn.setText(_translate("MainWindow", "System Info."))




class ThreadClass(QThread):
    Imageupd = pyqtSignal(QImage)

    def run(self):
        self.thread = True
        cap = cv2.VideoCapture(0)
        while self.thread:
            ret, frame = cap.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flip = cv2.flip(Image, 1)
                convert_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
                pic = convert_QT.scaled(640, 480, Qt.KeepAspectRatio)
                self.Imageupd.emit(pic)

    def stop(self):
        self.thread = False
        self.quit()