import keyboard
from PIL import ImageGrab
import time

def screenshot():
    # 현재 시간 저장
    cur_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("imgae{}.png".format(cur_time))

keyboard.add_hotkey("F1", screenshot) # 사용자가 0 키를 누르면 스크린샷 저장

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행