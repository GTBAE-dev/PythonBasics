# Pillow 모듈: 이미지 처리(pip install pillow)
from PIL import ImageGrab 
# Keyboard 모듈: 입력 받은 키를 받아 처리 (pip install keyboard)
import keyboard
import time

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S") # strftime: 원하는 형식에 맞춰 날짜/시간 출력
    img = ImageGrab.grab() # grab: screenshot 함수
    img.save("image{}.png".format(curr_time)) # save: 저장 함수

keyboard.add_hotkey("F9", screenshot) # ("키", 함수): 키 입력 함수 실행하는 함수("ctrl+shift+s" 처럼 여러 키 입력 가능)
keyboard.wait("esc") # wait: 키 누르면 종료 함수