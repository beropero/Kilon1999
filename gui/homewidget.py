
import sys
import os
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}")
from kiloncore import controller, context
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel
from ui.Ui_homeframe import Ui_HomeFrame
from qfluentwidgets import CheckBox
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from datetime import datetime

class HomeWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName('home')
        self.frame = Ui_HomeFrame()
        self.frame.setupUi(self)

        self.frame.LinkStartButton.clicked.connect(self.LinkStart)

        self.frame.stackedWidget.setCurrentIndex(0)
        self.frame.LevelSelect.addItems(["当前","铸币美学","尘埃运动","丰收时令"])
        self.frame.AchieveAwardDetailButton.clicked.connect(self.ChangeToAchieveAwardDetailPage)
        self.frame.WastelandDetailButton.clicked.connect(self.ChangeToWastelandDetailPage)
        self.frame.AnalysisDetailButton.clicked.connect(self.ChangeToAnalysisDetailPage)
        self.frame.SleepWalkDetailButton.clicked.connect(self.ChangeToSleepWalkDetailPage)
        self.frame.CellActiveDetailButton.clicked.connect(self.ChangeToCellActiveDetailPage)

        self.frame.CheckAllButton.clicked.connect(self.CheckAllCheckBox)
        self.frame.ClearAllButton.clicked.connect(self.ClearAllCheckBox)

        # 重定向输出
        sys.stdout = self
        sys.stderr = self

    
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
    
    def LinkStart(self):
        self.rolloverLinkStartButton()
        data = {}
        data['CellActiveCheckBox'] = self.frame.CellActiveCheckBox.isChecked()
        self.LinkStartThread = LinkStartThread(data)
        self.LinkStartThread.finish.connect(self.rolloverLinkStartButton)
        self.LinkStartThread.start()

    ## 翻转按钮状态
    def rolloverLinkStartButton(self):
        self.frame.LinkStartButton.setEnabled(not self.frame.LinkStartButton.isEnabled())
   
    def write(self, text):
        self.frame.LogOutput.insertPlainText(text)

    def flush(self):
        pass

class LinkStartThread(QThread):
    finish = pyqtSignal(bool)

    def __init__(self, data):
        super(LinkStartThread, self).__init__()
        self.CellActiveCheckBox = data['CellActiveCheckBox']
        
    def run(self):
        try :
            print(f"{getnowtimeformat()} 建立连接...")
            ## 初始化上下文
            ctx = context.Context()
            print(f"{getnowtimeformat()} 连接成功 !")
            if self.CellActiveCheckBox:
                print(f"{getnowtimeformat()} 刷活性...")
                controller.autoRecurrence(ctx)     
            ctx.Close() 
        except:
            print(f"{getnowtimeformat()} 连接失败 ！")
        finally:
            print(f"{getnowtimeformat()} 任务结束 ！")
            self.finish.emit(True)
            

def getnowtimeformat():
    return datetime.now().strftime("%H:%M:%S")