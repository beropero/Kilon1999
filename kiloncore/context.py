from pyminitouchModify import MNTDevice
import json
import os
import subprocess
from kiloncore.consts import getnowtimeformat

class Context:
    conf   = None  # 配置实例
    device = None  # minitouch设备实例
    is_running = True # 是否运行中
    cellActive = None # 细胞活性数量

    def __init__(self):
        # 读取配置文件
        with open('conf.json', 'r', encoding='utf-8') as f:
            conf = json.loads(f.read())
        self.conf = conf
        # 将ADB路径添加到环境变量PATH中
        os.environ["PATH"] += os.pathsep + os.path.dirname(self.conf["adb"]["path"])
        # adb 连接
        self.adbConnect()
        # 初始化minitouch
        _DEVICE_ID = self.conf["adb"]["addr"]
        self.device = MNTDevice(_DEVICE_ID)
        # 获取分辨率
        self.adbResolution()

    # adb 连接
    def adbConnect(self):
        adb = self.conf["adb"]
        result = subprocess.run(f"adb connect {adb['addr']}", stdout=subprocess.PIPE, stderr=subprocess.PIPE,creationflags=subprocess.CREATE_NO_WINDOW)

        if result.returncode != 0:
            print(f"{getnowtimeformat()} 连接失败")
        else:
            print(f"{getnowtimeformat()} 连接成功")

    # adb 获取分辨率
    def adbResolution(self):
        result = subprocess.run(f"adb shell wm size", stdout=subprocess.PIPE, stderr=subprocess.PIPE,creationflags=subprocess.CREATE_NO_WINDOW)

        if result.returncode == 0:
            output = result.stdout.decode("utf-8").strip()
            # 输出格式 "Physical size: WIDTHxHEIGHT"
            width_height = output.split(": ")[1]
            # 分割宽度和高度
            height, width = map(int, width_height.split("x"))
            # 长宽与模板比率
            self.wr = width/1280
            self.hr = height/720
            print(f"{getnowtimeformat()} 分辨率:{width}x{height}")
        else:
            error = result.stderr.decode("utf-8").strip()
            print(f"Error: {error}")
            exit(0)

    # 修改 adb 配置
    def adbChange(self, keyword, value):
        self.conf['adb'][keyword] = value
        with open('conf.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.conf, indent=4))

    def Close(self):
        adb = self.conf["adb"]
        subprocess.run(f"adb disconnect {adb['addr']}", stdout=subprocess.PIPE, stderr=subprocess.PIPE,creationflags=subprocess.CREATE_NO_WINDOW)
        self.device.stop()
