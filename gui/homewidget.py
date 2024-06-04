
import sys
import os
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}")
from kiloncore import controller, context
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel
from ui.Ui_homeframe import Ui_HomeFrame
from qfluentwidgets import CheckBox
from PyQt5.QtCore import QObject, QThread

class HomeWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('home')
        self.frame = Ui_HomeFrame()
        self.frame.setupUi(self)
        #self.LinkStart = LinkStart(self)
        #self.frame.LinkStartButton.clicked.connect(self.LinkStart.start())

        self.frame.stackedWidget.setCurrentIndex(0)
        self.frame.LevelSelect.addItems(["当前","铸币美学","尘埃运动","丰收时令"])
        self.frame.AchieveAwardDetailButton.clicked.connect(self.ChangeToAchieveAwardDetailPage)
        self.frame.WastelandDetailButton.clicked.connect(self.ChangeToWastelandDetailPage)
        self.frame.AnalysisDetailButton.clicked.connect(self.ChangeToAnalysisDetailPage)
        self.frame.SleepWalkDetailButton.clicked.connect(self.ChangeToSleepWalkDetailPage)
        self.frame.CellActiveDetailButton.clicked.connect(self.ChangeToCellActiveDetailPage)

        self.frame.CheckAllButton.clicked.connect(self.CheckAllCheckBox)
        self.frame.ClearAllButton.clicked.connect(self.ClearAllCheckBox)
    
    def CheckAllCheckBox(self):
        self.frame.AnalysisCheckBox.setChecked(True)
        self.frame.SleepwalkCheckBox.setChecked(True)
        self.frame.AchieveAwardCheckBox.setChecked(True)
        self.frame.CellActiveCheckBox.setChecked(True)
        self.frame.WastelandCheckBox.setChecked(True)

    def ClearAllCheckBox(self):
        self.frame.AnalysisCheckBox.setChecked(False)
        self.frame.SleepwalkCheckBox.setChecked(False)
        self.frame.AchieveAwardCheckBox.setChecked(False)
        self.frame.CellActiveCheckBox.setChecked(False)
        self.frame.WastelandCheckBox.setChecked(False)

    def ChangeToAchieveAwardDetailPage(self):
        self.frame.stackedWidget.setCurrentIndex(1)
    def ChangeToSleepWalkDetailPage(self):
        self.frame.stackedWidget.setCurrentIndex(2)
    def ChangeToWastelandDetailPage(self):
        self.frame.stackedWidget.setCurrentIndex(3)
    def ChangeToAnalysisDetailPage(self):
        self.frame.stackedWidget.setCurrentIndex(4)
    def ChangeToCellActiveDetailPage(self):
        self.frame.stackedWidget.setCurrentIndex(5)


   
# class LinkStart(QThread):
#     def __init__(self):
#         super(LinkStart, self).__init__()

#     def run(self):
#         ## 初始化上下文
#         super.frame.LinkStartButton.setEnabled(False)
#         ctx = context.Context()
#         if super.frame.CellActiveCheckBox.isChecked():
#             controller.autoRecurrence(ctx)
#         if super.frame.AnalysisCheckBox.isChecked():
#             controller.volitionAlanalysis(ctx)
#         ctx.Close()