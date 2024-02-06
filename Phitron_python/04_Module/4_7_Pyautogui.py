import pyautogui
import time

# # pyautogui.alert("This is An Alert Box")
time.sleep(3)
for i in range(1, 5):
    time.sleep(3)
    pyautogui.write("I Love Python", interval=0.25)
    pyautogui.press('enter')


# img =pyautogui.screenshot()
# img.save("scr.png")


# time.sleep(3)

# -> Mouse Function
# print(pyautogui.size()) # => Print Screen Resoluation
# print(pyautogui.position()) # =>  Print Mosuse Curent position

# => move The Mouse Over Time
# pyautogui.moveTo(100, 100, 3)

# => Move The Mouse relative to its current position
# pyautogui.moveRel(100,100,3)

# => click
# pyautogui.click(500, 500, 3, 3, button="left")
# pyautogui.rightClick(500, 500, 3, 3, button="left")
# pyautogui.leftClick(500, 500, 3, 3, button="left")
# pyautogui.doubleClick(500, 500, 3, 3, button="left")
# pyautogui.tripleClick(500, 500, 3, 3, button="left")


# => Scroll
# time.sleep(2)
# -> Scroll Up
# pyautogui.scroll(-500)

# -> Scroll Down
# pyautogui.scroll(500)


# => Mouse Up & Down
# pyautogui.mouseUp(100, 100, button="left")
# pyautogui.mouseDown(100, 100, button="left")

# =< Example

# pyautogui.mouseDown(300, 400, button="left")
# pyautogui.moveTo(800, 400, 3)
# pyautogui.mouseUp()
# pyautogui.moveTo(1000, 400, 3)

""" ===================================================== """
""" ==================== Project 1 ====================== """
""" ===================================================== """

""" time.sleep(2)
distance = 300

while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 10
    pyautogui.dragRel(0, distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, -distance,  1, button="left")
time.sleep(4) """
