import pyautogui

# Moving the mouse at specific location
pyautogui.moveTo(200, 100)              # (Horizen: X, Vertical: Y)
pyautogui.moveTo(100,200, duration=1)   # Move the mouse during 1 second


pyautogui.moveTo(100,100, duration=0.25)
pyautogui.moveTo(200,100, duration=0.25)
pyautogui.moveTo(100,300, duration=0.25)


# Move the mouse base on current position
pyautogui.moveTo(100, 100)
print(pyautogui.position())
pyautogui.move(100,200, duration=0.25)      # move (100+100, 100+200)
print(pyautogui.position())
pyautogui.move(200,100, duration=0.25)      # move (100+100+200, 100+200+100)
print(pyautogui.position())


p = pyautogui.position()
print(p[0], p[1])   # Print the x and y position
print(p.x, p.y)     # Print the x and y position