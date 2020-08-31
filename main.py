# -*- coding: utf-8 -*-

import os
import sys

# 线程
import threading

# 图片
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../../../')
sys.path.append('../../../../')

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 图片
import image_rc

# 暗黑主题
import qdarkstyle

# 数据库

# ui
from Ui_ui import Ui_Dialog

from PyQt5.QtWidgets import QFileDialog, QWidget, QMessageBox
from time import sleep

from loop import Loop
from queue import Queue
from threading import Thread


class Yu(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Yu, self).__init__(parent)
        self.setupUi(self)

        # 经典暗黑主题
        qApp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # 标题
        self.setWindowTitle('余时锐消息轰炸')

        # 图标
        self.setWindowIcon(QIcon(':/yu/yu.ico'))

        # 置顶
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # 窗口大小
        self.resize(275, 30)

        # 移动位置
        self.move(0, 0)

        # 数据源，下拉选设置值，从网上获取，下次加入大数据
        self.comboBox_data.addItems(['诗词', '甜言蜜语', '鸡汤', '马屁精'])

        # 数据源下拉选，当前值
        self.comboBox_data.setCurrentText('诗词')

        # 时间间隔
        self.doubleSpinBox_speed.setDecimals(0.02)

        # 循环
        self.loop = None

        # 线程
        self.thread = None

        # 队列
        self.queue = Queue()

    # 发送消息
    @pyqtSlot()
    def on_pushButton_send_clicked(self):
        # 若是发送按钮
        if self.pushButton_send.text() == '发送':
            # 按钮名改为停止
            self.pushButton_send.setText('停止')

            # 队列不为空
            while not self.queue.empty():

                # 读取队列
                self.queue.get()

            # 网站循环发送（时间，队列，数据源类型）
            self.loop = Loop(self.doubleSpinBox_speed.value(), self.queue, self.comboBox_data.currentText())
            # 线程
            self.thread = Thread(target=self.loop.run, name='loop_run', args=())
            # 启动线程
            self.thread.start()
            # 休眠
            sleep(0.1)

            # 线程不可用
            if not self.thread.is_alive():

                # 警告框
                QMessageBox.warning(self, '余时锐警告', '请检查网络连接', QMessageBox.Yes)

                # 按钮变回发送
                self.pushButton_send.setText('发送')

        # 若是停止按钮，按钮名改为发送
        else:

            # 按钮改名为发送
            self.pushButton_send.setText('发送')

            # 写队列，等待时间1秒
            self.queue.put(1)

# pyinstaller -F -w -i yu.ico main.py
if __name__ == "__main__":
    # app
    app = QApplication(sys.argv)
    # 创建对象
    yu = Yu()
    # 显示窗口
    yu.show()
    # 应用程序循环
    sys.exit(app.exec_())
