# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\yushirui_python\yushirui_01_tools\yu0404_消息轰炸\ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(253, 95)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_data = QtWidgets.QComboBox(Dialog)
        self.comboBox_data.setEditable(True)
        self.comboBox_data.setObjectName("comboBox_data")
        self.gridLayout.addWidget(self.comboBox_data, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.doubleSpinBox_speed = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_speed.setObjectName("doubleSpinBox_speed")
        self.gridLayout.addWidget(self.doubleSpinBox_speed, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_send = QtWidgets.QPushButton(Dialog)
        self.pushButton_send.setObjectName("pushButton_send")
        self.gridLayout.addWidget(self.pushButton_send, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "数据"))
        self.label_2.setText(_translate("Dialog", "速度"))
        self.pushButton_send.setText(_translate("Dialog", "发送"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
