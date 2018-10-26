# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'theAwesomeTollDrawer_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(631, 591)
        Form.setMinimumSize(QtCore.QSize(631, 591))
        Form.setMaximumSize(QtCore.QSize(633, 594))
        Form.setWindowTitle("大班会抽奖器 by hejk2008 (https://hejk2008.github.io/theAwesomeTollDrawer)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 30, 581, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.student = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student.sizePolicy().hasHeightForWidth())
        self.student.setSizePolicy(sizePolicy)
        self.student.setMinimumSize(QtCore.QSize(284, 265))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(48)
        self.student.setFont(font)
        self.student.setText("测 试")
        self.student.setAlignment(QtCore.Qt.AlignCenter)
        self.student.setObjectName("student")
        self.gridLayout.addWidget(self.student, 0, 0, 3, 2)
        self.klass3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.klass3.setFont(font)
        self.klass3.setText("3班")
        self.klass3.setObjectName("klass3")
        self.gridLayout.addWidget(self.klass3, 2, 2, 1, 1)
        self.klass1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.klass1.sizePolicy().hasHeightForWidth())
        self.klass1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.klass1.setFont(font)
        self.klass1.setText("1班")
        self.klass1.setObjectName("klass1")
        self.gridLayout.addWidget(self.klass1, 0, 2, 1, 1)
        self.stopbutton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopbutton.sizePolicy().hasHeightForWidth())
        self.stopbutton.setSizePolicy(sizePolicy)
        self.stopbutton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stopbutton.setFont(font)
        self.stopbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopbutton.setText("停止")
        self.stopbutton.setObjectName("stopbutton")
        self.gridLayout.addWidget(self.stopbutton, 3, 1, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setText("开始")
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 3, 0, 1, 1)
        self.klass2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.klass2.setFont(font)
        self.klass2.setText("2班")
        self.klass2.setObjectName("klass2")
        self.gridLayout.addWidget(self.klass2, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dial = QtWidgets.QDial(self.gridLayoutWidget)
        self.dial.setMinimum(1)
        self.dial.setMaximum(100)
        self.dial.setSliderPosition(100)
        self.dial.setObjectName("dial")
        self.verticalLayout.addWidget(self.dial)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 3, 2, 1, 1)
        self.statusLabel = QtWidgets.QLabel(Form)
        self.statusLabel.setGeometry(QtCore.QRect(0, 570, 54, 12))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.statusLabel.setFont(font)
        self.statusLabel.setText("就绪")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")

        self.retranslateUi(Form)
        self.startButton.clicked.connect(Form.drawStart)
        self.stopbutton.clicked.connect(Form.drawStop)
        self.dial.valueChanged['int'].connect(Form.changeSpeed)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.klass1, self.klass2)
        Form.setTabOrder(self.klass2, self.klass3)
        Form.setTabOrder(self.klass3, self.dial)
        Form.setTabOrder(self.dial, self.startButton)
        Form.setTabOrder(self.startButton, self.stopbutton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "速度"))

