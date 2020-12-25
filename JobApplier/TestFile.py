from selenium import webdriver
from pynput.mouse import Button, Controller
import time
# PATH = "C:\chromedriver"
# driver = webdriver.Chrome(PATH)
# driver.get("https://www.google.com/webhp?hl=en&ictx=2&sa=X&ved=0ahUKEwjXrqzSuOftAhVixFkKHR_kCEYQPQgI")
# driver.maximize_window()
# time.sleep(3)
# driver.set_window_position(0,0)
# print(driver.current_window_handle)
# time.sleep(3)
mouse = Controller()
# mouse.position = (1850, 11)
# mouse.click(Button.left, 1)
# mouse.release(Button.left)

# time.sleep(5)
# mouse.position=(1851,14)
# mouse.press(Button.left)
# time.sleep(2)
# mouse.move(-1011,90)
# time.sleep(5)
# mouse.release(Button.left)
# print(mouse.position)
# time.sleep(2)
# mouse.position=(870,120)
# mouse.press(Button.left)
# mouse.move(1011,-90)
# time.sleep(2)
for i in range(100):
    print(mouse.position)
    time.sleep(1)