import subprocess
from kiloncore import context



def screencap(ctx: context.Context):
    screencap  = f"adb shell screencap -p /sdcard/screenshot.png"
    pullscreen = f"adb pull /sdcard/screenshot.png screencap/"
    rmscreen   = f"adb shell rm /sdcard/screenshot.png"

    cmds = [screencap, pullscreen, rmscreen]

    for cmd in cmds:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,creationflags=subprocess.CREATE_NO_WINDOW)

