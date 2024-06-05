
import sys
import os
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}")
from kiloncore import controller, context
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel, QFileDialog
from ui.Ui_settingframe import Ui_SettingFrame
from qfluentwidgets import CheckBox
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from datetime import datetime
import json
import config

class SettingWidget(QFrame):
    def __init__(self, parent=None): 
        super().__init__(parent=parent)

        self.setObjectName('setting')
        self.frame = Ui_SettingFrame()
        self.frame.setupUi(self)

        self.frame.AdbPath.setText(config.conf['adb']['path'])
        self.frame.AdbConnectAddr.addItem(config.conf['adb']['addr'])

        self.frame.AdbSelect.clicked.connect(self.selectAdb)
        self.frame.AdbPath.returnPressed.connect(self.confChangeEvent)
        self.frame.AdbPath.editingFinished.connect(self.confChangeEvent)

        self.frame.AdbConnectAddr.returnPressed.connect(self.confChangeEvent)
        self.frame.AdbConnectAddr.editingFinished.connect(self.confChangeEvent)
       
    def confChangeEvent(self):
        config.conf['adb']['path'] = self.frame.AdbPath.text()
        config.conf['adb']['addr'] = self.frame.AdbConnectAddr.text()
        config.saveconf()

    def selectAdb(self):
        # 打开文件对话框，并设置对话框标题和默认打开的文件夹
        filters = "Adb Files (*adb*.exe);;All Files (*)"
        fname, _ = QFileDialog.getOpenFileName(self, '选择文件', f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}/resource/adb/", filters)

        # 如果用户选择了文件，打印出文件路径
        if fname:
            config.conf['adb']['path'] = fname
            self.frame.AdbPath.setText(config.conf['adb']['path'])
            config.saveconf()
