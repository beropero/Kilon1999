# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\workplace\PythonProject\Kilon1999\gui\ui\homeframe.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeFrame(object):
    def setupUi(self, HomeFrame):
        HomeFrame.setObjectName("HomeFrame")
        HomeFrame.resize(1291, 923)
        self.horizontalLayout = QtWidgets.QHBoxLayout(HomeFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SelectWidget = QtWidgets.QWidget(HomeFrame)
        self.SelectWidget.setMinimumSize(QtCore.QSize(300, 500))
        self.SelectWidget.setMaximumSize(QtCore.QSize(300, 500))
        self.SelectWidget.setObjectName("SelectWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.SelectWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.AchieveAwardDetailButton = TransparentToolButton(self.SelectWidget)
        self.AchieveAwardDetailButton.setObjectName("AchieveAwardDetailButton")
        self.gridLayout.addWidget(self.AchieveAwardDetailButton, 7, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.ClearAllButton = PushButton(self.SelectWidget)
        self.ClearAllButton.setMinimumSize(QtCore.QSize(100, 40))
        self.ClearAllButton.setObjectName("ClearAllButton")
        self.gridLayout.addWidget(self.ClearAllButton, 9, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.WastelandDetailButton = TransparentToolButton(self.SelectWidget)
        self.WastelandDetailButton.setObjectName("WastelandDetailButton")
        self.gridLayout.addWidget(self.WastelandDetailButton, 3, 2, 1, 1)
        self.CheckAllButton = PushButton(self.SelectWidget)
        self.CheckAllButton.setMinimumSize(QtCore.QSize(100, 40))
        self.CheckAllButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.CheckAllButton.setObjectName("CheckAllButton")
        self.gridLayout.addWidget(self.CheckAllButton, 9, 1, 1, 1)
        self.SleepWalkDetailButton = TransparentToolButton(self.SelectWidget)
        self.SleepWalkDetailButton.setObjectName("SleepWalkDetailButton")
        self.gridLayout.addWidget(self.SleepWalkDetailButton, 6, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 12, 1, 1, 1)
        self.AchieveAwardCheckBox = CheckBox(self.SelectWidget)
        self.AchieveAwardCheckBox.setObjectName("AchieveAwardCheckBox")
        self.gridLayout.addWidget(self.AchieveAwardCheckBox, 7, 1, 1, 1)
        self.LinkStartButton = PushButton(self.SelectWidget)
        self.LinkStartButton.setMinimumSize(QtCore.QSize(120, 60))
        self.LinkStartButton.setObjectName("LinkStartButton")
        self.gridLayout.addWidget(self.LinkStartButton, 11, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 10, 1, 1, 1)
        self.CellActiveCheckBox = CheckBox(self.SelectWidget)
        self.CellActiveCheckBox.setObjectName("CellActiveCheckBox")
        self.gridLayout.addWidget(self.CellActiveCheckBox, 1, 1, 1, 1)
        self.WastelandCheckBox = CheckBox(self.SelectWidget)
        self.WastelandCheckBox.setObjectName("WastelandCheckBox")
        self.gridLayout.addWidget(self.WastelandCheckBox, 3, 1, 1, 1)
        self.CellActiveDetailButton = TransparentToolButton(self.SelectWidget)
        self.CellActiveDetailButton.setObjectName("CellActiveDetailButton")
        self.gridLayout.addWidget(self.CellActiveDetailButton, 1, 2, 1, 1)
        self.SleepwalkCheckBox = CheckBox(self.SelectWidget)
        self.SleepwalkCheckBox.setObjectName("SleepwalkCheckBox")
        self.gridLayout.addWidget(self.SleepwalkCheckBox, 6, 1, 1, 1)
        self.AnalysisCheckBox = CheckBox(self.SelectWidget)
        self.AnalysisCheckBox.setObjectName("AnalysisCheckBox")
        self.gridLayout.addWidget(self.AnalysisCheckBox, 2, 1, 1, 1)
        self.AnalysisDetailButton = TransparentToolButton(self.SelectWidget)
        self.AnalysisDetailButton.setObjectName("AnalysisDetailButton")
        self.gridLayout.addWidget(self.AnalysisDetailButton, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.SelectWidget)
        self.DetailWidget = QtWidgets.QWidget(HomeFrame)
        self.DetailWidget.setMinimumSize(QtCore.QSize(200, 500))
        self.DetailWidget.setMaximumSize(QtCore.QSize(200, 500))
        self.DetailWidget.setObjectName("DetailWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DetailWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.DetailWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.initPage = QtWidgets.QWidget()
        self.initPage.setObjectName("initPage")
        self.stackedWidget.addWidget(self.initPage)
        self.AchieveAwardDetailPage = QtWidgets.QWidget()
        self.AchieveAwardDetailPage.setObjectName("AchieveAwardDetailPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.AchieveAwardDetailPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MailAwardCheckBox = CheckBox(self.AchieveAwardDetailPage)
        self.MailAwardCheckBox.setObjectName("MailAwardCheckBox")
        self.gridLayout_3.addWidget(self.MailAwardCheckBox, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        self.HHAwardCheckBox = CheckBox(self.AchieveAwardDetailPage)
        self.HHAwardCheckBox.setObjectName("HHAwardCheckBox")
        self.gridLayout_3.addWidget(self.HHAwardCheckBox, 5, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 6, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 0, 1, 1)
        self.PerDayorWeekCheckBox = CheckBox(self.AchieveAwardDetailPage)
        self.PerDayorWeekCheckBox.setObjectName("PerDayorWeekCheckBox")
        self.gridLayout_3.addWidget(self.PerDayorWeekCheckBox, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 4, 0, 1, 1)
        self.stackedWidget.addWidget(self.AchieveAwardDetailPage)
        self.SleepwalkDetailPage = QtWidgets.QWidget()
        self.SleepwalkDetailPage.setObjectName("SleepwalkDetailPage")
        self.stackedWidget.addWidget(self.SleepwalkDetailPage)
        self.WastelandDetailPage = QtWidgets.QWidget()
        self.WastelandDetailPage.setObjectName("WastelandDetailPage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.WastelandDetailPage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stackedWidget.addWidget(self.WastelandDetailPage)
        self.AnalysisDetailPage = QtWidgets.QWidget()
        self.AnalysisDetailPage.setObjectName("AnalysisDetailPage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.AnalysisDetailPage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.AnalysisDetailPage)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 1, 0, 1, 1)
        self.AnalysisTime = SpinBox(self.AnalysisDetailPage)
        self.AnalysisTime.setObjectName("AnalysisTime")
        self.gridLayout_6.addWidget(self.AnalysisTime, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 343, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem10, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.AnalysisDetailPage)
        self.CellActiveDetailPage = QtWidgets.QWidget()
        self.CellActiveDetailPage.setObjectName("CellActiveDetailPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.CellActiveDetailPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.CellActiveDetailPage)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 5, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem11, 6, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 0, 0, 1, 1)
        self.LevelSelect = ComboBox(self.CellActiveDetailPage)
        self.LevelSelect.setObjectName("LevelSelect")
        self.gridLayout_4.addWidget(self.LevelSelect, 1, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 2, 0, 1, 1)
        self.CellActiveTime = SpinBox(self.CellActiveDetailPage)
        self.CellActiveTime.setObjectName("CellActiveTime")
        self.gridLayout_4.addWidget(self.CellActiveTime, 3, 1, 1, 1)
        self.NextLevel = ComboBox(self.CellActiveDetailPage)
        self.NextLevel.setObjectName("NextLevel")
        self.gridLayout_4.addWidget(self.NextLevel, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.CellActiveDetailPage)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.CellActiveDetailPage)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem14, 4, 0, 1, 1)
        self.stackedWidget.addWidget(self.CellActiveDetailPage)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.DetailWidget)
        self.LogWidget = QtWidgets.QWidget(HomeFrame)
        self.LogWidget.setMinimumSize(QtCore.QSize(300, 500))
        self.LogWidget.setMaximumSize(QtCore.QSize(300, 10000))
        self.LogWidget.setObjectName("LogWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.LogWidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem15, 0, 1, 1, 1)
        self.LogOutput = TextEdit(self.LogWidget)
        self.LogOutput.setMinimumSize(QtCore.QSize(150, 0))
        self.LogOutput.setMaximumSize(QtCore.QSize(600, 16777215))
        self.LogOutput.setReadOnly(True)
        self.LogOutput.setObjectName("LogOutput")
        self.gridLayout_7.addWidget(self.LogOutput, 1, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem16, 1, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem17, 1, 2, 1, 1)
        self.horizontalLayout.addWidget(self.LogWidget)

        self.retranslateUi(HomeFrame)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(HomeFrame)

    def retranslateUi(self, HomeFrame):
        _translate = QtCore.QCoreApplication.translate
        HomeFrame.setWindowTitle(_translate("HomeFrame", "Frame"))
        self.AchieveAwardDetailButton.setText(_translate("HomeFrame", "⚙"))
        self.ClearAllButton.setText(_translate("HomeFrame", "清空"))
        self.WastelandDetailButton.setText(_translate("HomeFrame", "⚙"))
        self.CheckAllButton.setText(_translate("HomeFrame", "全选"))
        self.SleepWalkDetailButton.setText(_translate("HomeFrame", "⚙"))
        self.AchieveAwardCheckBox.setText(_translate("HomeFrame", "领取奖励"))
        self.LinkStartButton.setText(_translate("HomeFrame", "Link Start!"))
        self.CellActiveCheckBox.setText(_translate("HomeFrame", "刷活性"))
        self.WastelandCheckBox.setText(_translate("HomeFrame", "荒原收取"))
        self.CellActiveDetailButton.setText(_translate("HomeFrame", "⚙"))
        self.SleepwalkCheckBox.setText(_translate("HomeFrame", "人工梦游"))
        self.AnalysisCheckBox.setText(_translate("HomeFrame", "意志解析"))
        self.AnalysisDetailButton.setText(_translate("HomeFrame", "⚙"))
        self.MailAwardCheckBox.setText(_translate("HomeFrame", "领取所有邮件奖励"))
        self.HHAwardCheckBox.setText(_translate("HomeFrame", "领取吼吼点唱机"))
        self.PerDayorWeekCheckBox.setText(_translate("HomeFrame", "领取每日/每周任务"))
        self.label_3.setText(_translate("HomeFrame", "刷取次数"))
        self.label_4.setText(_translate("HomeFrame", "剩余活性"))
        self.label_2.setText(_translate("HomeFrame", "刷取次数"))
        self.label.setText(_translate("HomeFrame", "关卡选择"))
from qfluentwidgets import CheckBox, ComboBox, PushButton, SpinBox, TextEdit, TransparentToolButton
