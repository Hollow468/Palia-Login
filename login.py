import pyautogui
import win32gui
from os import path
import base64
from subprocess import Popen

im = pyautogui.screenshot()
password = (im.width/4)*0.67, (im.height/2)*0.915
login = (im.width/4)*0.67, (im.height/2)*1.08
game_path="./palia.exe"
x,y=im.width/1.72,im.height*0.2


def __main__():
    if path.exists("config"):   
        file = open("config", "r")
        text = file.read()
    else:
        print("config文件不存在")
        text = input("请输入密码：")
        Interval=input("输入速度(单位秒):")
        encoded = base64.b64encode(text.encode("utf-8"))
        with open("config", "wb") as file:
            file.write(encoded)
            file.write(b"\n"+Interval.encode())

def login_in():
    Interval=open("config", "r").read().split("\n")
    S = open("config", "r").read()
    d64 = base64.b64decode(S.encode("utf-8")).decode("utf-8")
    pyautogui.click(password)
    pyautogui.typewrite(d64,interval=Interval[1])

def find():
  reg = False 
  while not reg: 
    reg = pyautogui.pixelMatchesColor(int(x),int(y),(255,255,255),tolerance=3) 
    if reg: 
      login_in()
      break 

FrameClass="UnrealWindow"
FrameTitle="Palia  "
def Palia_Path():
  hwnd = win32gui.FindWindow(FrameClass,FrameTitle)
  if hwnd !=  0: 
    find()
    print('游戏已运行')
  else:
    print('正在尝试启动游戏')
    try:
      Popen(game_path)
    except(FileNotFoundError):
       print('启动失败,请手动开启游戏')

__main__()
Palia_Path()


      




