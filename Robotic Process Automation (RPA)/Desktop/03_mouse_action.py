import pyautogui

#### Find the button
# For the click action, I want to click the File tab
# First, I do not know the exactly location of File tab
# Move the mouse to File tab during the sleep time
# After three second, it will prints out the location of File tab
# (The value will be different for each computer)
pyautogui.sleep(3)              # Sleep 3 second
print(pyautogui.position())     # Get the mouse position
####


pyautogui.mouseDown()           # Hold down the mouse button
pyautogui.mouseUp()             # Mouse button released
pyautogui.click()               # mouseDonwn() + mouseUp()


pyautogui.click(57, 20)         # Mouse click at (57, 20)


pyautogui.doubleClick()           # Mouse double click
pyautogui.click(clicks=2)         # Mouse click twice



#### Try to using on Paint progrma for drawing
pyautogui.moveTo(1398,496)        # For this, you have to get the postion first
pyautogui.mouseDown()
pyautogui.move(100,200)
pyautogui.mouseUp()
##########


pyautogui.rightClick()            # Click the right button of mouse
pyautogui.middleClick()           # Click the middle button of mouse


#### Try to using the other progrma for drag
pyautogui.moveTo(1172, 161)               # Get the prgram position
pyautogui.drag(-1000, 0, duration=0.25)   # Drag base on current postion
                                          # (1277+100, 275+0)
pyautogui.dragTo(100, 100, duration=0.25) # Drag to absolute position
##########



pyautogui.scroll(300)       # scroll up 300
pyautogui.scroll(-300)      # scroll down 300