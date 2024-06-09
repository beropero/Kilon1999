import sys
import os
sys.path.append(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}")
from kiloncore import controller, context
from PyQt5.QtWidgets import QFrame
from PyQt5 import QtWidgets
from gui.ui.Ui_homeframe import Ui_HomeFrame
from PyQt5.QtCore import  QThread, pyqtSignal
from datetime import datetime

from gui import config

class HomeWidget(QFrame):
    LinkStartThread = None
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.frame = Ui_HomeFrame()
        self.frame.setupUi(self)

        self.frame.LinkStartButton.clicked.connect(self.LinkStart)

        self.frame.stackedWidget.setCurrentIndex(0)
        self.frame.LevelSelect.addItems(["当前","铸币美学","尘埃运动","丰收时令"])
        self.frame.NextLevel.addItems(["不选择","铸币美学","尘埃运动","丰收时令"])

        self.setConfState()

        self.frame.AchieveAwardDetailButton.clicked.connect(self.ChangeToAchieveAwardDetailPage)
        self.frame.WastelandDetailButton.clicked.connect(self.ChangeToWastelandDetailPage)
        self.frame.AnalysisDetailButton.clicked.connect(self.ChangeToAnalysisDetailPage)
        self.frame.SleepWalkDetailButton.clicked.connect(self.ChangeToSleepWalkDetailPage)
        self.frame.CellActiveDetailButton.clicked.connect(self.ChangeToCellActiveDetailPage)

        self.frame.CheckAllButton.clicked.connect(self.CheckAllCheckBox)
        self.frame.ClearAllButton.clicked.connect(self.ClearAllCheckBox)

        self.frame.CellActiveCheckBox.clicked.connect(self.confChangeEvent)
        self.frame.AnalysisCheckBox.clicked.connect(self.confChangeEvent)
        self.frame.WastelandCheckBox.clicked.connect(self.confChangeEvent)
        self.frame.SleepwalkCheckBox.clicked.connect(self.confChangeEvent)
        self.frame.AchieveAwardCheckBox.clicked.connect(self.confChangeEvent)

        self.frame.PerDayorWeekCheckBox.clicked.connect(self.confChangeEvent)
        self.frame.MailAwardCheckBox.clicked.connect(self.confChangeEvent)
        self.frame.HHAwardCheckBox.clicked.connect(self.confChangeEvent)

        self.frame.AnalysisTime.valueChanged.connect(self.confChangeEvent)

        self.frame.CellActiveTime.valueChanged.connect(self.confChangeEvent)
        self.frame.LevelSelect.currentIndexChanged.connect(self.confChangeEvent)
        self.frame.NextLevel.currentIndexChanged.connect(self.confChangeEvent)

        # 重定向输出
        sys.stdout = self
        # sys.stderr = self

    def setConfState(self):
        self.frame.CellActiveCheckBox.setChecked(config.conf['CellActive']['check'])
        self.frame.AnalysisCheckBox.setChecked(config.conf['VolitionalAnalysis']['check'])
        self.frame.WastelandCheckBox.setChecked(config.conf['Wasteland']['check'])
        self.frame.SleepwalkCheckBox.setChecked( config.conf['Sleepwalk']['check'])
        self.frame.AchieveAwardCheckBox.setChecked(config.conf['AchieveAward']['check'])

        self.frame.PerDayorWeekCheckBox.setChecked(config.conf['AchieveAward']['dayAndWeek'])
        self.frame.MailAwardCheckBox.setChecked(config.conf['AchieveAward']['mail'])
        self.frame.HHAwardCheckBox.setChecked(config.conf['AchieveAward']['hhJukebox'])

        self.frame.AnalysisTime.setValue(config.conf['VolitionalAnalysis']['time'])

        self.frame.CellActiveTime.setValue(config.conf['CellActive']['time'])
        self.frame.LevelSelect.setCurrentIndex(config.conf['CellActive']['levelselect'])
        self.frame.NextLevel.setCurrentIndex(config.conf['CellActive']['nextlevels'])

    def CheckAllCheckBox(self):
        self.frame.AnalysisCheckBox.setChecked(True)
        self.frame.SleepwalkCheckBox.setChecked(True)
        self.frame.AchieveAwardCheckBox.setChecked(True)
        self.frame.CellActiveCheckBox.setChecked(True)
        self.frame.WastelandCheckBox.setChecked(True)
        self.confChangeEvent()

    def ClearAllCheckBox(self):
        self.frame.AnalysisCheckBox.setChecked(False)
        self.frame.SleepwalkCheckBox.setChecked(False)
        self.frame.AchieveAwardCheckBox.setChecked(False)
        self.frame.CellActiveCheckBox.setChecked(False)
        self.frame.WastelandCheckBox.setChecked(False)
        self.confChangeEvent()

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
        if self.frame.LinkStartButton.text() == "Link Start!":
            self.rolloverLinkStartButton()
            data = {}
            data['CellActiveCheckBox'] = self.frame.CellActiveCheckBox.isChecked()
            data['AchieveAwardCheckBox'] = self.frame.AchieveAwardCheckBox.isChecked()
            data['AnalysisCheckBox'] = self.frame.AnalysisCheckBox.isChecked()
            data['SleepwalkCheckBox'] = self.frame.SleepwalkCheckBox.isChecked()
            data['WastelandCheckBox'] = self.frame.WastelandCheckBox.isChecked()
            self.LinkStartThread = LinkStartThread(data)
            self.LinkStartThread.finish.connect(self.rolloverLinkStartButton)
            self.LinkStartThread.start()
            self.frame.LinkStartButton.setText("Stop")
        elif self.frame.LinkStartButton.text() == "Stop":
            print(f"{getnowtimeformat()} 停止中...")
            self.stop()
           


    def confChangeEvent(self):
        config.conf['CellActive']['check'] = self.frame.CellActiveCheckBox.isChecked()
        config.conf['Wasteland']['check'] = self.frame.WastelandCheckBox.isChecked()
        config.conf['VolitionalAnalysis']['check'] = self.frame.AnalysisCheckBox.isChecked()
        config.conf['Sleepwalk']['check'] = self.frame.SleepwalkCheckBox.isChecked()
        config.conf['AchieveAward']['check'] = self.frame.AchieveAwardCheckBox.isChecked()
        
        config.conf['AchieveAward']['dayAndWeek'] = self.frame.PerDayorWeekCheckBox.isChecked()
        config.conf['AchieveAward']['mail'] = self.frame.MailAwardCheckBox.isChecked()
        config.conf['AchieveAward']['hhJukebox'] = self.frame.HHAwardCheckBox.isChecked()
        
        config.conf['VolitionalAnalysis']['time'] = self.frame.AnalysisTime.value()

        config.conf['CellActive']['levelselect'] = self.frame.LevelSelect.currentIndex()
        config.conf['CellActive']['nextlevels'] = self.frame.NextLevel.currentIndex()
        config.conf['CellActive']['time'] = self.frame.CellActiveTime.value()

        config.saveconf()

    ## 停止
    def stop(self):
        self.frame.LinkStartButton.setEnabled(not self.frame.LinkStartButton.isEnabled())
        self.LinkStartThread.is_running = False
        if self.LinkStartThread.ctx != None:
            self.LinkStartThread.ctx.is_running = False

    ## 翻转按钮状态
    def rolloverLinkStartButton(self):
        self.frame.LinkStartButton.setEnabled(True)
        self.frame.LinkStartButton.setText("Link Start!")
   
    def write(self, text):
        self.frame.LogOutput.insertPlainText(text)

    def flush(self):
        pass

class LinkStartThread(QThread):
    finish = pyqtSignal(bool)
    ctx = None
    is_running = True
    def __init__(self, data):
        super(LinkStartThread, self).__init__()
        self.CellActiveCheckBox = data['CellActiveCheckBox']
        self.AchieveAwardCheckBox = data['AchieveAwardCheckBox']
        self.AnalysisCheckBox = data['AnalysisCheckBox']
        self.SleepwalkCheckBox = data['SleepwalkCheckBox']
        self.WastelandCheckBox = data['WastelandCheckBox']
        
    def run(self):
        try :
            print(f"{getnowtimeformat()} 建立连接...")
            ## 初始化上下文
            self.ctx = context.Context()
            if not self.is_running:
                exit(0)
            # 开始执行
            try:
                controller.cmd(self.ctx)
            except Exception as ex:
                print(ex)
            finally:
                self.ctx.Close() 
        except:
            pass
        finally:
            print(f"{getnowtimeformat()} 任务结束 !")
            self.finish.emit(True)
    


def getnowtimeformat():
    return datetime.now().strftime("%H:%M:%S")