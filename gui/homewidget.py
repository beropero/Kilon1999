
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel
from ui.Ui_homeframe import Ui_HomeFrame
from qfluentwidgets import CheckBox

class HomeWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('home')
        self.frame = Ui_HomeFrame()
        self.frame.setupUi(self)

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

