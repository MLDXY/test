#########
#21312313
#Compatibility: python3.8
#IDE:PyCharm2019.2
#####


import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets ,QtMultimedia
import tkinter
from scipy import signal
import numpy as np
import wave
import struct
import sys
import os

class Ui_Digital_Audio_Processing(object):
    def setupUi(self, Digital_Audio_Processing):
        Digital_Audio_Processing.setObjectName("Digital_Audio_Processing")
        Digital_Audio_Processing.resize(866, 673)
        Digital_Audio_Processing.setFixedSize(866,673)
        Digital_Audio_Processing.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(Digital_Audio_Processing)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 40, 231, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(50, 30, 100, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 60, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 90, 100, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(50, 120, 100, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 200, 231, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 60, 131, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.MaintabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.MaintabWidget.setGeometry(QtCore.QRect(310, 30, 481, 521))
        self.MaintabWidget.setObjectName("MaintabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.AudiotabWidget = QtWidgets.QTabWidget(self.tab)
        self.AudiotabWidget.setGeometry(QtCore.QRect(20, 20, 431, 451))
        self.AudiotabWidget.setMouseTracking(False)
        self.AudiotabWidget.setTabletTracking(False)
        self.AudiotabWidget.setAutoFillBackground(True)
        self.AudiotabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.AudiotabWidget.setUsesScrollButtons(False)
        self.AudiotabWidget.setObjectName("AudiotabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.graphicsView = QtWidgets.QGraphicsView(self.tabWidgetPage1)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView.setObjectName("graphicsView")
        self.AudiotabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.tabWidgetPage2)
        self.graphicsView_3.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.AudiotabWidget.addTab(self.tabWidgetPage2, "")
        self.MaintabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.FiltertabWidget = QtWidgets.QTabWidget(self.tab_2)
        self.FiltertabWidget.setGeometry(QtCore.QRect(20, 20, 431, 451))
        self.FiltertabWidget.setObjectName("FiltertabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.FiltertabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.tab_4)
        self.graphicsView_4.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.FiltertabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.tab_6)
        self.graphicsView_5.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.FiltertabWidget.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.tab_5)
        self.graphicsView_6.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.FiltertabWidget.addTab(self.tab_5, "")
        self.MaintabWidget.addTab(self.tab_2, "")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(50, 400, 231, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 30, 131, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 60, 131, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 60, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 90, 131, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 120, 131, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 41, 16))
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 300, 231, 91))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 30, 51, 20))
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 60, 51, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(80, 30, 131, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 60, 131, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        Digital_Audio_Processing.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Digital_Audio_Processing)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 22))
        self.menubar.setObjectName("menubar")
        self.menubar.setNativeMenuBar(False)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setGeometry(QtCore.QRect(447, 351, 97, 80))
        self.menu.setObjectName("menu")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuSound = QtWidgets.QMenu(self.menubar)
        self.menuSound.setObjectName("menuSound")
        Digital_Audio_Processing.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Digital_Audio_Processing)
        self.statusbar.setObjectName("statusbar")
        Digital_Audio_Processing.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Digital_Audio_Processing)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Digital_Audio_Processing)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionUsage = QtWidgets.QAction(Digital_Audio_Processing)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.actionUsage.setFont(font)
        self.actionUsage.setObjectName("actionUsage")
        self.actionAbout_us = QtWidgets.QAction(Digital_Audio_Processing)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.actionAbout_us.setFont(font)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.actionProcessing = QtWidgets.QAction(Digital_Audio_Processing)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.actionProcessing.setFont(font)
        self.actionProcessing.setObjectName("actionProcessing")
        self.actionProcessing_2 = QtWidgets.QAction(Digital_Audio_Processing)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.actionProcessing_2.setFont(font)
        self.actionProcessing_2.setObjectName("actionProcessing_2")
        self.actionBeforre_Processing = QtWidgets.QAction(Digital_Audio_Processing)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.actionBeforre_Processing.setFont(font)
        self.actionBeforre_Processing.setObjectName("actionBeforre_Processing")
        self.actionAfter_Processing = QtWidgets.QAction(Digital_Audio_Processing)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.actionAfter_Processing.setFont(font)
        self.actionAfter_Processing.setObjectName("actionAfter_Processing")
        self.menu.addAction(self.actionOpen)
        self.menu.addAction(self.actionSave)
        self.menuAbout.addAction(self.actionUsage)
        self.menuAbout.addAction(self.actionAbout_us)
        self.menuRun.addAction(self.actionProcessing)
        self.menuRun.addAction(self.actionProcessing_2)
        self.menuSound.addAction(self.actionBeforre_Processing)
        self.menuSound.addAction(self.actionAfter_Processing)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuSound.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.lineEdit_2.setValidator(QtGui.QIntValidator())
        self.lineEdit_3.setValidator(QtGui.QIntValidator())
        self.lineEdit_4.setValidator(QtGui.QIntValidator())
        self.lineEdit_5.setValidator(QtGui.QIntValidator())
        self.lineEdit_6.setValidator(QtGui.QIntValidator())

        self.actionSave.setEnabled(False)
        self.actionProcessing_2.setEnabled(False)
        self.actionAfter_Processing.setEnabled(False)
        self.actionBeforre_Processing.setEnabled(False)

        self.retranslateUi(Digital_Audio_Processing)
        self.MaintabWidget.setCurrentIndex(0)
        self.AudiotabWidget.setCurrentIndex(0)
        self.FiltertabWidget.setCurrentIndex(0)
        self.label_5.hide()
        self.label_6.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.label_3.setText('Fp')
        self.label_4.setText('Fst')

        self.radioButton.clicked.connect(self.lineEdit_5.hide)
        self.radioButton.clicked.connect(self.label_5.hide)
        self.radioButton.clicked.connect(self.label_6.hide)
        self.radioButton.clicked.connect(self.lineEdit_6.hide)
        self.radioButton.clicked.connect(lambda :self.label_3.setText('Fp'))
        self.radioButton.clicked.connect(lambda :self.label_4.setText('Fst'))
        self.radioButton_2.clicked.connect(self.label_5.hide)
        self.radioButton_2.clicked.connect(self.lineEdit_5.hide)
        self.radioButton_2.clicked.connect(self.label_6.hide)
        self.radioButton_2.clicked.connect(self.lineEdit_6.hide)
        self.radioButton_2.clicked.connect(lambda :self.label_3.setText('Fst'))
        self.radioButton_2.clicked.connect(lambda :self.label_4.setText('Fp'))
        self.radioButton_3.clicked.connect(self.label_5.show)
        self.radioButton_3.clicked.connect(self.lineEdit_5.show)
        self.radioButton_3.clicked.connect(self.label_6.show)
        self.radioButton_3.clicked.connect(self.lineEdit_6.show)
        self.radioButton_3.clicked.connect(lambda :self.label_3.setText('Fst1'))
        self.radioButton_3.clicked.connect(lambda :self.label_4.setText('Fp1'))
        self.radioButton_3.clicked.connect(lambda :self.label_5.setText('Fp2'))
        self.radioButton_3.clicked.connect(lambda :self.label_6.setText('Fst2'))
        self.radioButton_4.clicked.connect(self.label_5.show)
        self.radioButton_4.clicked.connect(self.lineEdit_5.show)
        self.radioButton_4.clicked.connect(self.label_6.show)
        self.radioButton_4.clicked.connect(self.lineEdit_6.show)
        self.radioButton_4.clicked.connect(lambda :self.label_3.setText('Fp1'))
        self.radioButton_4.clicked.connect(lambda :self.label_4.setText('Fst1'))
        self.radioButton_4.clicked.connect(lambda :self.label_5.setText('Fst2'))
        self.radioButton_4.clicked.connect(lambda :self.label_6.setText('Fp2'))
        self.radioButton_5.clicked.connect(self.label.show)
        self.radioButton_5.clicked.connect(self.lineEdit_2.show)
        self.radioButton_6.clicked.connect(self.label.hide)
        self.radioButton_6.clicked.connect(self.lineEdit_2.hide)
        self.comboBox.currentIndexChanged.connect(lambda :self.radioButton_5.setChecked(True))
        self.comboBox_2.currentIndexChanged.connect(lambda :self.radioButton_6.setChecked(True))
        QtCore.QMetaObject.connectSlotsByName(Digital_Audio_Processing)
        Digital_Audio_Processing.setTabOrder(self.radioButton, self.radioButton_2)
        Digital_Audio_Processing.setTabOrder(self.radioButton_2, self.radioButton_3)
        Digital_Audio_Processing.setTabOrder(self.radioButton_3, self.radioButton_4)
        Digital_Audio_Processing.setTabOrder(self.radioButton_4, self.lineEdit)
        Digital_Audio_Processing.setTabOrder(self.lineEdit, self.lineEdit_2)
        Digital_Audio_Processing.setTabOrder(self.lineEdit_2, self.radioButton_5)
        Digital_Audio_Processing.setTabOrder(self.radioButton_5, self.comboBox)
        Digital_Audio_Processing.setTabOrder(self.comboBox, self.radioButton_6)
        Digital_Audio_Processing.setTabOrder(self.radioButton_6, self.comboBox_2)
        Digital_Audio_Processing.setTabOrder(self.comboBox_2, self.lineEdit_3)
        Digital_Audio_Processing.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        Digital_Audio_Processing.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        Digital_Audio_Processing.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        Digital_Audio_Processing.setTabOrder(self.lineEdit_6, self.AudiotabWidget)
        Digital_Audio_Processing.setTabOrder(self.AudiotabWidget, self.FiltertabWidget)
        Digital_Audio_Processing.setTabOrder(self.FiltertabWidget, self.MaintabWidget)
        Digital_Audio_Processing.setTabOrder(self.MaintabWidget, self.graphicsView)
        Digital_Audio_Processing.setTabOrder(self.graphicsView, self.graphicsView_3)
        Digital_Audio_Processing.setTabOrder(self.graphicsView_3, self.graphicsView_2)
        Digital_Audio_Processing.setTabOrder(self.graphicsView_2, self.graphicsView_4)
        Digital_Audio_Processing.setTabOrder(self.graphicsView_4, self.graphicsView_5)
        Digital_Audio_Processing.setTabOrder(self.graphicsView_5, self.graphicsView_6)

        self.pA1 = pg.PlotWidget()
        self.layout1 = QtWidgets.QGridLayout()
        self.layout1.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView.setLayout((self.layout1))
        self.layout1.addWidget(self.pA1)
        self.pA2= pg.PlotWidget()
        self.layout2 = QtWidgets.QGridLayout()
        self.layout2.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_3.setLayout((self.layout2))
        self.layout2.addWidget(self.pA2)
        self.pF1= pg.PlotWidget()
        self.layout3 = QtWidgets.QGridLayout()
        self.layout3.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_2.setLayout((self.layout3))
        self.layout3.addWidget(self.pF1)
        self.pF2= pg.PlotWidget()
        self.layout4 = QtWidgets.QGridLayout()
        self.layout4.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_4.setLayout((self.layout4))
        self.layout4.addWidget(self.pF2)
        self.pF3= pg.PlotWidget()
        self.layout5 = QtWidgets.QGridLayout()
        self.layout5.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_5.setLayout((self.layout5))
        self.layout5.addWidget(self.pF3)
        self.pF4= pg.PlotWidget()
        self.layout6 = QtWidgets.QGridLayout()
        self.layout6.setGeometry(QtCore.QRect(20, 20, 391, 381))
        self.graphicsView_6.setLayout((self.layout6))
        self.layout6.addWidget(self.pF4)


        self.sound1 = QtMultimedia.QSoundEffect()
        self.sound2 = QtMultimedia.QSoundEffect()
        global check_file
        global check_design
        check_file=0
        check_design=0

    def retranslateUi(self, Digital_Audio_Processing):
        _translate = QtCore.QCoreApplication.translate
        Digital_Audio_Processing.setWindowTitle(_translate("Digital_Audio_Processing", "Digital Audio Processing"))
        self.groupBox_2.setTitle(_translate("Digital_Audio_Processing", "Response Type"))
        self.radioButton.setText(_translate("Digital_Audio_Processing", "Lowpass"))
        self.radioButton_2.setText(_translate("Digital_Audio_Processing", "Highpass"))
        self.radioButton_3.setText(_translate("Digital_Audio_Processing", "Bandpass"))
        self.radioButton_4.setText(_translate("Digital_Audio_Processing", "Bandstop"))
        self.groupBox_3.setTitle(_translate("Digital_Audio_Processing", "Magnitude Specifications [dB]"))
        self.label.setText(_translate("Digital_Audio_Processing", "Rp"))
        self.label_2.setText(_translate("Digital_Audio_Processing", "Rs(As)"))
        self.AudiotabWidget.setTabText(self.AudiotabWidget.indexOf(self.tabWidgetPage1), _translate("Digital_Audio_Processing", "Time Domain"))
        self.AudiotabWidget.setTabText(self.AudiotabWidget.indexOf(self.tabWidgetPage2), _translate("Digital_Audio_Processing", "Frequency Domain"))
        self.MaintabWidget.setTabText(self.MaintabWidget.indexOf(self.tab), _translate("Digital_Audio_Processing", "Audio"))
        self.FiltertabWidget.setTabText(self.FiltertabWidget.indexOf(self.tab_3), _translate("Digital_Audio_Processing", "Magnitude Response"))
        self.FiltertabWidget.setTabText(self.FiltertabWidget.indexOf(self.tab_4), _translate("Digital_Audio_Processing", "Phase Response"))
        self.FiltertabWidget.setTabText(self.FiltertabWidget.indexOf(self.tab_6), _translate("Digital_Audio_Processing", "Pole/Zero"))
        self.FiltertabWidget.setTabText(self.FiltertabWidget.indexOf(self.tab_5), _translate("Digital_Audio_Processing", "Group Delay"))
        self.MaintabWidget.setTabText(self.MaintabWidget.indexOf(self.tab_2), _translate("Digital_Audio_Processing", "Filter"))
        self.groupBox_4.setTitle(_translate("Digital_Audio_Processing", "Frequency Specifications [Hz] (Fs=8000)"))
        self.label_3.setText(_translate("Digital_Audio_Processing", "Fp1"))
        self.label_4.setText(_translate("Digital_Audio_Processing", "Fst1"))
        self.label_5.setText(_translate("Digital_Audio_Processing", "Fp2"))
        self.label_6.setText(_translate("Digital_Audio_Processing", "Fst2"))
        self.groupBox.setTitle(_translate("Digital_Audio_Processing", "Design Method"))
        self.radioButton_5.setText(_translate("Digital_Audio_Processing", "IIR"))
        self.radioButton_6.setText(_translate("Digital_Audio_Processing", "FIR"))
        self.comboBox.setItemText(0, _translate("Digital_Audio_Processing", "Butterworth"))
        self.comboBox.setItemText(1, _translate("Digital_Audio_Processing", "Chebyshev Type Ⅰ"))
        self.comboBox.setItemText(2, _translate("Digital_Audio_Processing", "Chebyshev Type ⅠⅠ"))
        self.comboBox.setItemText(3, _translate("Digital_Audio_Processing", "Elliptic"))
        self.comboBox_2.setItemText(0, _translate("Digital_Audio_Processing", "Rectangle"))
        self.comboBox_2.setItemText(1, _translate("Digital_Audio_Processing", "Triangular"))
        self.comboBox_2.setItemText(2, _translate("Digital_Audio_Processing", "Hanning"))
        self.comboBox_2.setItemText(3, _translate("Digital_Audio_Processing", "Hamming"))
        self.comboBox_2.setItemText(4, _translate("Digital_Audio_Processing", "Blackman"))
        self.comboBox_2.setItemText(5, _translate("Digital_Audio_Processing", "Kaiser(beta=7.865)"))
        self.menu.setTitle(_translate("Digital_Audio_Processing", "File"))
        self.menuAbout.setTitle(_translate("Digital_Audio_Processing", "Help "))
        self.menuRun.setTitle(_translate("Digital_Audio_Processing", "Run"))
        self.menuSound.setTitle(_translate("Digital_Audio_Processing", "Sound"))
        self.actionOpen.setText(_translate("Digital_Audio_Processing", "Open File"))
        self.actionSave.setText(_translate("Digital_Audio_Processing", "Save File"))
        self.actionUsage.setText(_translate("Digital_Audio_Processing", "Application Instruction"))
        self.actionAbout_us.setText(_translate("Digital_Audio_Processing", "About us"))
        self.actionProcessing.setText(_translate("Digital_Audio_Processing", "Design Filter"))
        self.actionProcessing_2.setText(_translate("Digital_Audio_Processing", "Processing"))
        self.actionBeforre_Processing.setText(_translate("Digital_Audio_Processing", "Beforre Processing"))
        self.actionAfter_Processing.setText(_translate("Digital_Audio_Processing", "After Processing"))

        self.actionOpen.triggered.connect(lambda:self.Openfile())
        self.actionSave.triggered.connect(lambda:self.Savefile())
        self.actionProcessing.triggered.connect(lambda :self.FilterDesign())#design
        self.actionProcessing_2.triggered.connect(lambda :self.AudioProcessing())#processing
        self.actionBeforre_Processing.triggered.connect(lambda :self.Sound_BeforeProcessing())
        self.actionAfter_Processing.triggered.connect(lambda :self.Sound_AfterProcessing())
        self.lineEdit.textChanged.connect(lambda:self.WindowList())
        self.radioButton_6.toggled.connect(lambda :self.WindowList())
        self.actionUsage.triggered.connect(lambda :Application_Instruction.show())
        self.actionAbout_us.triggered.connect(lambda :About_Us.show())

    #Choose Audio
    def Openfile(self):
        global filename
        global NameWithoutPath
        global wave_data
        global check_file
        global check_design
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName()
        f = wave.open(filename)
        NameWithoutPath = ''
        for i in range(len(filename) - 1, -1, -1):
            if filename[i] != '/':
                NameWithoutPath = filename[i] + NameWithoutPath
            else:
                break

        params = f.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]
        str_data = f.readframes(nframes)
        f.close()

        wave_data = np.frombuffer(str_data, dtype=np.short)
        Fs = framerate

        #Time Domain
        t = np.linspace(0, len(wave_data) / Fs, len(wave_data))
        self.pA1.clear()
        self.pA1.plot(t,wave_data)
        self.pA1.setLabels(left='Normalized Amplitude', bottom='Time (s)',
                           title='Time Domain'+' ['+NameWithoutPath+']')
        self.pA1.setXRange(0,np.max(t))
        self.pA1.setYRange(-np.max(np.abs(wave_data)),np.max(np.abs(wave_data)))
        self.pA1.showGrid(x=True, y=True)
        self.layout1.update()
        self.MaintabWidget.setCurrentWidget(self.tab)

        #Frequency Domain
        short = wave_data[10001:10161]
        H = np.fft.fftshift(abs(np.fft.fft(short)))
        f = np.linspace(-Fs / 2, Fs / 2, 160)
        self.pA2.clear()
        self.pA2.plot(f,H)
        self.pA2.setLabels(left='Magnitude (dB)', bottom='Frequency  (Hz)',
                           title='Frequency Domain'+' ['+NameWithoutPath+']')
        self.pA2.setXRange(0, np.max(f))
        self.pA2.setYRange(0, np.max(H))
        self.pA2.showGrid(x=True, y=True)
        self.layout2.update()
        self.actionBeforre_Processing.setEnabled(True)
        check_file=1
        if check_design==1:
            self.actionProcessing_2.setEnabled(True)

    #Save New Audio
    def Savefile(self):
        filename_Save, filetype_Save = QtWidgets.QFileDialog.getSaveFileName(directory='untitled')
        global out
        out=out/max(np.abs(out))
        file = wave.open(filename_Save+'.wav', 'wb')
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(8000)
        file.setnframes(40000)
        file.setcomptype('NONE', 'not compressed')
        for v in out:
            file.writeframes(struct.pack('h', int(v * 64000 / 2)))
        file.close()

    #FIR List (Depend On As)
    def WindowList(self):
        if self.radioButton_6.isChecked():
            Rs=float(self.lineEdit.text())
            self.comboBox_2.removeItem(5)
            self.comboBox_2.removeItem(4)
            self.comboBox_2.removeItem(3)
            self.comboBox_2.removeItem(2)
            self.comboBox_2.removeItem(1)
            self.comboBox_2.removeItem(0)
            if Rs>=21:
                self.comboBox_2.addItem("Rectangle")
                self.comboBox_2.setItemText(0, "Rectangle")
            if Rs>=25:
                self.comboBox_2.addItem("Triangular")
                self.comboBox_2.setItemText(1, "Triangular")
            if Rs>=44:
                self.comboBox_2.addItem("Hanning")
                self.comboBox_2.setItemText(2, "Hanning")
            if Rs>=53:
                self.comboBox_2.addItem("Hamming")
                self.comboBox_2.setItemText(3,"Hamming")
            if Rs>=74:
                self.comboBox_2.addItem("Blackman")
                self.comboBox_2.setItemText(4,"Blackman")
            if Rs>=80:
                self.comboBox_2.addItem("Kaiser(beta=7.865)")
                self.comboBox_2.setItemText(5,"Kaiser(beta=7.865)")

    #Filter Design
    def FilterDesign(self):
        global Type
        global Method
        global a
        global b
        global check_file
        global check_design
        Method = 0
        if self.radioButton_5.isChecked():
            Method = 0  # IIR
        elif self.radioButton_6.isChecked():
            Method = 1  # FIR
        Type = 0
        if self.radioButton.isChecked():  # lowpass
            Type = 0
        elif self.radioButton_2.isChecked():  # highpass
            Type = 1
        elif self.radioButton_3.isChecked():  # bandpass
            Type = 2
        elif self.radioButton_4.isChecked():  ##bandstop
            Type = 3

        if str(self.lineEdit.text())=='' or (Method==0 and str(self.lineEdit_2.text())=='') or str(self.lineEdit_3.text())=='' or str(self.lineEdit_4.text())=='':
            input_error2.show()
            self.actionProcessing_2.setEnabled(False)
            self.actionAfter_Processing.setEnabled(False)
        elif float(self.lineEdit_3.text())>=float(self.lineEdit_4.text()):
            input_error1.show()
            self.actionProcessing_2.setEnabled(False)
            self.actionAfter_Processing.setEnabled(False)
        elif (Type==2 or Type==3) and (str(self.lineEdit_5.text())=='' or str(self.lineEdit_6.text())==''):
            input_error2.show()
            self.actionProcessing_2.setEnabled(False)
            self.actionAfter_Processing.setEnabled(False)
        elif (Type==2 or Type==3) and (float(self.lineEdit_4.text())>=float(self.lineEdit_5.text()) or float(self.lineEdit_5.text())>=float(self.lineEdit_6.text())):
            input_error1.show()
            self.actionProcessing_2.setEnabled(False)
            self.actionAfter_Processing.setEnabled(False)
        elif float(self.lineEdit_4.text())>=4000:
            input_error3.show()
            self.actionProcessing_2.setEnabled(False)
            self.actionAfter_Processing.setEnabled(False)
        elif (Type==2 or Type==3) and float(self.lineEdit_6.text())>=4000:
            input_error3.show()
            self.actionProcessing_2.setEnabled(False)
            self.actionAfter_Processing.setEnabled(False)
        else:
            Rs=float(self.lineEdit.text())
            if Method==0:
                Rp = float(self.lineEdit_2.text())
            if Type==0 or Type==3:
                fp1 = float(self.lineEdit_3.text())
                fst1 = float(self.lineEdit_4.text())
            else:
                fst1 = float(self.lineEdit_3.text())
                fp1 = float(self.lineEdit_4.text())

            As=Rs
            Fs = 8000
            Wp1 = 2 * fp1 / Fs
            Wst1 = 2 * fst1 / Fs



            IIRName=0
            IIRName=self.comboBox.currentIndex()
            FIRName=0
            FIRName=self.comboBox_2.currentIndex()

            if Method==0:
                if Type==0 or Type==1:
                    Wp=Wp1
                    Wst=Wst1
                else:
                    if Type==2:
                        fp2 = float(self.lineEdit_5.text())
                        fst2 = float(self.lineEdit_6.text())
                    else:
                        fst2 = float(self.lineEdit_5.text())
                        fp2 = float(self.lineEdit_6.text())
                    Wst2 = 2 * fst2 / Fs
                    Wp2 = 2 * fp2 / Fs
                    Wp=[Wp1,Wp2]
                    Wst=[Wst1,Wst2]

                if IIRName==0:
                    if Type==0:
                        N, Wn = signal.buttord(Wp, Wst, Rp, Rs)
                        b, a = signal.butter(N, Wn, btype='lowpass')
                    elif Type==1:
                        N, Wn = signal.buttord(Wp, Wst, Rp, Rs)
                        b, a = signal.butter(N, Wn, btype='highpass')
                    elif Type==2:
                        N, Wn = signal.buttord(Wp, Wst, Rp, Rs)
                        b, a = signal.butter(N, Wn, btype='bandpass')
                    else:
                        N, Wn = signal.buttord(Wp, Wst, Rp, Rs)
                        b, a = signal.butter(N, Wn, btype='bandstop')
                elif IIRName==1:
                    if Type==0:
                        N, Wn = signal.cheb1ord(Wp, Wst, Rp, Rs)
                        b, a = signal.cheby1(N,Rp, Wn, btype='lowpass')
                    elif Type==1:
                        N, Wn = signal.cheb1ord(Wp, Wst, Rp, Rs)
                        b, a = signal.cheby1(N,Rp, Wn, btype='highpass')
                    elif Type==2:
                        N, Wn = signal.cheb1ord(Wp, Wst, Rp, Rs)
                        b, a = signal.cheby1(N,Rp, Wn, btype='bandpass')
                    else:
                        N, Wn = signal.cheb1ord(Wp, Wst, Rp, Rs)
                        b, a = signal.cheby1(N,Rp, Wn, btype='bandstop')
                elif IIRName==2:
                    if Type==0:
                        N, Wn = signal.cheb2ord(Wp, Wst, Rp, Rs)
                        b, a = signal.cheby2(N,Rs, Wn, btype='lowpass')
                    elif Type==1:
                        N, Wn = signal.cheb2ord(Wp, Wst, Rp, Rs)
                        b, a = signal.cheby2(N,Rs, Wn, btype='highpass')
                    elif Type==2:
                        N, Wn = signal.cheb2ord(Wp, Wst, Rp, Rs)
                        b, a = signal.cheby2(N,Rs, Wn, btype='bandpass')
                    else:
                        N, Wn = signal.cheb2ord(Wp, Wst, Rp, Rs)
                        b, a = signal.cheby2(N,Rs, Wn, btype='bandstop')
                else:
                    if Type==0:
                        N, Wn = signal.ellipord(Wp, Wst, Rp, Rs)
                        b, a = signal.ellip(N,Rp,Rs, Wn, btype='lowpass')
                    elif Type==1:
                        N, Wn = signal.ellipord(Wp, Wst, Rp, Rs)
                        b, a = signal.ellip(N,Rp,Rs, Wn, btype='highpass')
                    elif Type==2:
                        N, Wn = signal.ellipord(Wp, Wst, Rp, Rs)
                        b, a = signal.ellip(N,Rp,Rs, Wn, btype='bandpass')
                    else:
                        N, Wn = signal.ellipord(Wp, Wst, Rp, Rs)
                        b, a = signal.ellip(N,Rp,Rs, Wn, btype='bandstop')

                w, h = signal.freqz(b, a, fs=Fs)
                self.pF1.clear()
                self.pF1.plot(w,20 * np.log10(abs(h)))
                self.pF1.setXRange(0, np.max(w))
                self.pF1.setYRange(np.min(20 * np.log10(abs(h))),0)
                self.pF1.setLabels(left='Magnitude [dB]',bottom='Frequency [Hz]',title='Frequency Domain')
                self.pF1.showGrid(x=True,y=True)
                self.layout3.update()

                hp = np.unwrap(np.angle(h))
                self.pF2.clear()
                self.pF2.plot(w,hp)
                self.pF2.setXRange(0, np.max(w))
                self.pF2.setYRange(np.min(hp),np.max(hp))
                self.pF2.setLabels(left='Phase [Radians]',bottom='Frequency [Hz]',title='Phase Response')
                self.pF2.showGrid(x=True,y=True)
                self.layout4.update()

                z, p, k = signal.tf2zpk(b, a)
                self.pF3.clear()
                self.pF3.addLegend()
                self.pF3.plot(np.real(z), np.imag(z),pen=None,symbol='x',symbolBrush=(255,255,255),name='Zeros')
                self.pF3.plot(np.real(p), np.imag(p),pen=None,symbol='o',symbolBrush=(255,0,0),name='Poles')

                theta = np.linspace(0, 2 * np.pi, 1000)
                cx = np.cos(theta)
                cy = np.sin(theta)
                self.pF3.plot(cx, cy,style=QtCore.Qt.DotLine)


                self.pF3.showGrid(x=True,y=True)
                self.pF3.setXRange(-1.2,1.2)
                self.pF3.setYRange(-1.2,1.2)
                self.pF3.setLabels(left='Imaginary Part',bottom='Real Part',title='Pole / Zero Plot')
                self.layout5.update()

                w, gd = signal.group_delay((b, a), fs=Fs)
                self.pF4.clear()
                self.pF4.plot(w,gd)
                self.pF4.setXRange(0,np.max(w))
                self.pF4.setYRange(0,np.max(gd))
                self.pF4.setLabels(left='Group delay [samples]',bottom='Frequency [Hz]',title='Digital filter group delay')
                self.pF4.showGrid(x=True,y=True)
                self.layout6.update()
                Design_success.show()
                check_design=1

                if check_file==1:
                    self.actionProcessing_2.setEnabled(True)

            elif Method==1:
                if FIRName==0:
                    Wpi=1.8*np.pi
                elif FIRName==1:
                    Wpi=6.1*np.pi
                elif FIRName==2:
                    Wpi=6.2*np.pi
                elif FIRName==3:
                    Wpi=6.6*np.pi
                elif FIRName==4:
                    Wpi=11*np.pi
                elif FIRName==5:
                    Wpi=10*np.pi

                if Type==0 or Type==1:
                    Wp = Wp1
                    Wst = Wst1
                    delta_omega = abs((Wp - Wst))
                    N = int(np.ceil(Wpi / delta_omega))
                    Wc=(Wp+Wst)/2
                else:
                    if Type==2:
                        fp2 = float(self.lineEdit_5.text())
                        fst2 = float(self.lineEdit_6.text())
                    else:
                        fst2 = float(self.lineEdit_5.text())
                        fp2 = float(self.lineEdit_6.text())
                    Wst2 = 2 * fst2 / Fs
                    Wp2 = 2 * fp2 / Fs
                    delta_omega = min(abs(Wp1 - Wst1), abs(Wp2 - Wst2))
                    N = int(np.ceil(Wpi / delta_omega))
                    Wc = [(Wp1 + Wst1) / 2, (Wp2 + Wst2) / 2]

                if FIRName==0:
                    if Type==0:
                        b = signal.firwin(N, Wc, window='boxcar', pass_zero='lowpass')
                    elif Type==1:
                        b = signal.firwin(N, Wc, window='boxcar', pass_zero='highpass')
                    elif Type==2:
                        b = signal.firwin(N, Wc, window='boxcar', pass_zero='bandpass')
                    elif Type==3:
                        b = signal.firwin(N, Wc, window='boxcar', pass_zero='bandstop')
                elif FIRName==1:
                    if Type==0:
                        b = signal.firwin(N, Wc, window='triang', pass_zero='lowpass')
                    elif Type==1:
                        b = signal.firwin(N, Wc, window='triang', pass_zero='highpass')
                    elif Type==2:
                        b = signal.firwin(N, Wc, window='triang', pass_zero='bandpass')
                    elif Type==3:
                        b = signal.firwin(N, Wc, window='triang', pass_zero='bandstop')
                elif FIRName==2:
                    if Type==0:
                        b = signal.firwin(N, Wc, window='hann', pass_zero='lowpass')
                    elif Type==1:
                        b = signal.firwin(N, Wc, window='hann', pass_zero='highpass')
                    elif Type==2:
                        b = signal.firwin(N, Wc, window='hann', pass_zero='bandpass')
                    elif Type==3:
                        b = signal.firwin(N, Wc, window='hann', pass_zero='bandstop')
                elif FIRName==3:
                    if Type==0:
                        b = signal.firwin(N, Wc, window='hamming', pass_zero='lowpass')
                    elif Type==1:
                        b = signal.firwin(N, Wc, window='hamming', pass_zero='highpass')
                    elif Type==2:
                        b = signal.firwin(N, Wc, window='hamming', pass_zero='bandpass')
                    elif Type==3:
                        b = signal.firwin(N, Wc, window='hamming', pass_zero='bandstop')
                elif FIRName==4:
                    if Type==0:
                        b = signal.firwin(N, Wc, window='blackman', pass_zero='lowpass')
                    elif Type==1:
                        b = signal.firwin(N, Wc, window='blackman', pass_zero='highpass')
                    elif Type==2:
                        b = signal.firwin(N, Wc, window='blackman', pass_zero='bandpass')
                    elif Type==3:
                        b = signal.firwin(N, Wc, window='blackman', pass_zero='bandstop')
                elif FIRName==5:
                    if Type==0:
                        b = signal.firwin(N, Wc, window=('kaiser', 7.865), pass_zero='lowpass')
                    elif Type==1:
                        b = signal.firwin(N, Wc, window=('kaiser', 7.865), pass_zero='highpass')
                    elif Type==2:
                        b = signal.firwin(N, Wc, window=('kaiser', 7.865), pass_zero='bandpass')
                    elif Type==3:
                        b = signal.firwin(N, Wc, window=('kaiser', 7.865), pass_zero='bandstop')

                w, h = signal.freqz(b, fs=Fs)
                self.pF1.clear()
                self.pF1.plot(w, 20 * np.log10(abs(h)))
                self.pF1.setXRange(0, np.max(w))
                self.pF1.setYRange(np.min(20 * np.log10(abs(h))), 0)
                self.pF1.setLabels(left='Magnitude [dB]', bottom='Frequency [Hz]', title='Frequency Domain')
                self.pF1.showGrid(x=True, y=True)
                self.layout3.update()

                hp = np.unwrap(np.angle(h))
                self.pF2.clear()
                self.pF2.plot(w, hp)
                self.pF2.setXRange(0, np.max(w))
                self.pF2.setYRange(np.min(hp), np.max(hp))
                self.pF2.setLabels(left='Phase [Radians]', bottom='Frequency [Hz]', title='Phase Response')
                self.pF2.showGrid(x=True, y=True)
                self.layout4.update()

                z, p, k = signal.tf2zpk(b, 1)
                self.pF3.clear()
                self.pF3.addLegend()
                self.pF3.plot(np.real(z), np.imag(z), pen=None, symbol='x', symbolBrush=(255, 255, 255), name='Zeros')
                self.pF3.plot(np.real(p), np.imag(p), pen=None, symbol='o', symbolBrush=(255, 0, 0), name='Poles')

                theta = np.linspace(0, 2 * np.pi, 100)
                cx = np.cos(theta)
                cy = np.sin(theta)
                self.pF3.plot(cx, cy,style=QtCore.Qt.DashDotDotLine)

                self.pF3.showGrid(x=True, y=True)
                self.pF3.setXRange(-1.2, 1.2)
                self.pF3.setYRange(-1.2, 1.2)
                self.pF3.setLabels(left='Imaginary Part', bottom='Real Part', title='Pole / Zero Plot')
                self.layout5.update()

                w, gd = signal.group_delay((b, 1), fs=Fs)
                self.pF4.clear()
                self.pF4.plot(w, gd)
                self.pF4.setXRange(0, np.max(w))
                self.pF4.setYRange(0, 1.5*np.max(gd))
                self.pF4.setLabels(left='Group delay [samples]', bottom='Frequency [Hz]',
                                   title='Digital filter group delay')
                self.pF4.showGrid(x=True, y=True)
                self.layout6.update()
                Design_success.show()
                check_design=1
                if check_file==1:
                    self.actionProcessing_2.setEnabled(True)

            self.MaintabWidget.setCurrentWidget(self.tab_2)

    def AudioProcessing(self):
        global wave_data
        global Method
        global a
        global b
        global out
        global NameWithoutPath
        out=1
        if Method==0:
            out = signal.filtfilt(b, a, wave_data)
        elif Method==1:
            out = signal.filtfilt(b, 1, wave_data)
        Fs=8000

        #Time Domain
        t = np.linspace(0, len(wave_data) / Fs, len(wave_data))
        self.pA1.clear()
        self.pA1.showGrid(x=True, y=True)
        self.pA1.addLegend()
        self.pA1.plot(t, wave_data,name='Before Processing')
        self.pA1.plot(t,out,pen='r',name='After Processing')
        self.pA1.setLabels(left='Normalized Amplitude', bottom='Time (s)',
                           title='Time Domain'+' ['+NameWithoutPath+']')
        self.pA1.setXRange(0, np.max(t))
        self.pA1.setYRange(-np.max(np.abs(wave_data)), np.max(np.abs(wave_data)))
        self.pA1.showGrid(x=True, y=True)
        self.layout1.update()
        self.MaintabWidget.setCurrentWidget(self.tab)

        #Frequency Domain
        short = wave_data[10001:10161]
        short_out=out[10001:10161]
        H = np.fft.fftshift(abs(np.fft.fft(short)))
        H_out = np.fft.fftshift(abs(np.fft.fft(short_out)))
        f = np.linspace(-Fs / 2, Fs / 2, 160)
        self.pA2.clear()
        self.pA2.addLegend()
        self.pA2.plot(f, H,name='Before Processing')
        self.pA2.plot(f,H_out,pen='r',name='After Processing')
        self.pA2.setLabels(left='Magnitude (dB)', bottom='Frequency  (Hz)',
                           title='Frequency Domain'+' ['+NameWithoutPath+']')
        self.pA2.setXRange(0, np.max(f))
        self.pA2.setYRange(0, np.max(H))
        self.pA2.showGrid(x=True, y=True)
        self.layout2.update()

        self.actionAfter_Processing.setEnabled(True)
        self.actionSave.setEnabled(True)

    def Sound_BeforeProcessing(self):
        global filename
        self.sound1.setSource(QtCore.QUrl.fromLocalFile(filename))
        self.sound1.setLoopCount(QtMultimedia.QSoundEffect.Infinite)
        self.sound1.setVolume(1)
        self.sound1.setLoopCount(1)
        self.sound1.play()

    def Sound_AfterProcessing(self):
        global out
        global filename
        global NameWithoutPath
        out=out/max(np.abs(out))

        PathOnly = ''
        for i in range(len(filename) - 1, -1, -1):
            if filename[i] == '/':
                PathOnly = filename[0:i + 1]
                break

        file = wave.open(PathOnly+'temp.wav', 'wb')
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(8000)
        file.setnframes(40000)
        file.setcomptype('NONE', 'not compressed')
        for v in out:
            file.writeframes(struct.pack('h', int(v * 64000 / 2)))
        file.close()
        self.sound2.setSource(QtCore.QUrl.fromLocalFile(PathOnly+'temp.wav'))
        self.sound2.setLoopCount(QtMultimedia.QSoundEffect.Infinite)
        self.sound2.setVolume(1)
        self.sound2.setLoopCount(1)
        self.sound2.play()

class Ui_input_error1(object):##order
    def setupUi(self, Dialog):
        Dialog.setObjectName("Filter Design error")
        Dialog.resize(400, 100)
        Dialog.setFixedSize(400,100)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 50, 100, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 400, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(lambda :Dialog.close())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Filter Design error"))
        Dialog.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton_2.setText(_translate("Dialog", "Ok"))
        self.label.setText(_translate("Dialog", "The frequency specification values must be in increasing order."))

class Ui_input_error2(object): #empty
    def setupUi(self, Dialog):
        Dialog.setObjectName("Filter Design error")
        Dialog.resize(300, 100)
        Dialog.setFixedSize(300,100)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 50, 100, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 180, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(lambda: Dialog.close())


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Filter Design error"))

        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)

        self.pushButton_2.setText(_translate("Dialog", "Ok"))
        self.label.setText(_translate("Dialog", "Edit boxes cannot be empty."))

class Ui_Application_instruction(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(820, 450)
        Dialog.setFixedSize(820,450)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 10, 220, 41))
        font = QtGui.QFont()
        font.setFamily("STIXIntegralsSm")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 640, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 70, 640, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 90, 640, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 130, 640, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 290, 640, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 150, 640, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(90, 170, 640, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(90, 190, 640, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(90, 210, 640, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(90, 230, 640, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(90, 270, 640, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(90, 250, 640, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(90, 310, 640, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(90, 330, 640, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(90, 350, 640, 20))
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(90, 370, 640, 20))
        self.label_19.setObjectName("label_19")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 400, 100, 33))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(lambda: Dialog.close())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Application Instruction"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.label.setText(_translate("Dialog", "Application Instruction"))
        self.label_2.setText(_translate("Dialog", "    Thank you for using the application. In order to let you experience the application swimmingly，a brief  "))
        self.label_3.setText(_translate("Dialog", "introduction is provided below the paragraph. Before using this application, please read it carefully, so"))
        self.label_4.setText(_translate("Dialog", "you can use it correctly."))
        self.label_5.setText(_translate("Dialog", "Steps:"))
        self.label_6.setText(_translate("Dialog", "frequency domain will also be calculated Automatically. It is clear to contract two pieces of audio in "))
        self.label_7.setText(_translate("Dialog", "1.Click ‘Open File’ button to choose an audio and the audio’s time domain and frequency domain will be "))
        self.label_8.setText(_translate("Dialog", "calculated Automatically."))
        self.label_9.setText(_translate("Dialog", "2.Choose the type of the filter you want and design method , input magnitude specifications in decibels "))
        self.label_10.setText(_translate("Dialog", "and frequency specifications in hertz. The default sampling frequency has been set to 8000Hz."))
        self.label_11.setText(_translate("Dialog", "3.Click ‘Design Filter’ button to calculate it. The magnitude response, phase response, pole/zero points"))
        self.label_12.setText(_translate("Dialog", "4.Click ‘Processing’ button to pass the audio signal through the filter. The new audio’s time domain and "))
        self.label_13.setText(_translate("Dialog", "and group delay of the filter will also be shown."))
        self.label_14.setText(_translate("Dialog", "one image."))
        self.label_15.setText(_translate("Dialog", "5.Click ‘Sound,Before Processing’ or ‘Sound,After Processing’ button to play two pieces of audios."))
        self.label_16.setText(_translate("Dialog", "Also:"))
        self.label_19.setText(_translate("Dialog", "You can click ‘Save File‘ button to save the new audio."))
        self.pushButton_2.setText(_translate("Dialog", "Ok"))

class Ui_About_Us(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 340)
        Dialog.setFixedSize(480,340)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 240, 41))
        font = QtGui.QFont()
        font.setFamily("STIXIntegralsSm")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 211, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 90, 200, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 120, 200, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 150, 300, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 180, 141, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(80, 200, 391, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(80, 230, 200, 20))
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 290, 100, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(80, 260, 200, 20))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(lambda: Dialog.close())
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About Us"))
        self.label.setText(_translate("Dialog", "Digital Audio Processing"))
        self.label_2.setText(_translate("Dialog", "Publish Date: August 10th, 2020"))
        self.label_3.setText(_translate("Dialog", "Version: 1.0"))
        self.label_4.setText(_translate("Dialog", "Language: English"))
        self.label_5.setText(_translate("Dialog", "Compatibility: python3.8(PyCharm2019.2)"))
        self.label_6.setText(_translate("Dialog", "Author: Junhong, Zhu "))
        self.label_7.setText(_translate("Dialog", "             GDUT, Commnunication Engineering Class 1 (2017)"))
        self.label_8.setText(_translate("Dialog", "Email: 1034670608@qq.com"))
        self.pushButton_2.setText(_translate("Dialog", "Ok"))
        self.label_9.setText(_translate("Dialog", "Welcome to Exchange!"))

class Ui_Design_success(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Design Success")
        Dialog.resize(300, 100)
        Dialog.setFixedSize(300,100)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 50, 100, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 20, 121, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(lambda: Dialog.close())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Design Success"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton_2.setText(_translate("Dialog", "Ok"))
        self.label.setText(_translate("Dialog", "Design success !"))

class Ui_input_error3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Filter Design error")
        Dialog.resize(340, 100)
        Dialog.setFixedSize(340,100)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 50, 100, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 311, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(lambda :Dialog.close())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Filter Design error"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton_2.setText(_translate("Dialog", "Ok"))
        self.label.setText(_translate("Dialog", "Frequency specifications must be less than 4000."))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_Digital_Audio_Processing()
    ui.setupUi(widgets)
    input_error1=QtWidgets.QDialog()
    input_error_ui1=Ui_input_error1()
    input_error_ui1.setupUi(input_error1)
    input_error2=QtWidgets.QDialog()
    input_error_ui2=Ui_input_error2()
    input_error_ui2.setupUi(input_error2)
    Application_Instruction=QtWidgets.QDialog()
    Application_Instruction_ui=Ui_Application_instruction()
    Application_Instruction_ui.setupUi(Application_Instruction)
    About_Us=QtWidgets.QDialog()
    About_Us_ui=Ui_About_Us()
    About_Us_ui.setupUi(About_Us)
    Design_success=QtWidgets.QDialog()
    Design_success_ui=Ui_Design_success()
    Design_success_ui.setupUi(Design_success)
    input_error3=QtWidgets.QDialog()
    input_error_ui3=Ui_input_error3()
    input_error_ui3.setupUi(input_error3)
    widgets.show()
    sys.exit(app.exec_())
