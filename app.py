import pyautogui
import time
import win32gui
import cv2
import numpy as np

time_1s = 4
status = 'waiting'

print("waiting for call....")

while True:
  active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
  
  time_1s += 1
  if time_1s == 5:
    time_1s = 0 
    if active_window_title != "Grasshopper App":
      pyautogui.hotkey('ctrl', 'alt', 'q')
  
  if active_window_title == "Grasshopper App":
    if status == 'waiting':
      left, top, right, bottom = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
      screenshot = pyautogui.screenshot(region=(left, top, right-left, bottom-top))
      screenshot_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
      template_image = cv2.imread('assets/incoming_call.png')
      res = cv2.matchTemplate(screenshot_image, template_image, cv2.TM_CCOEFF_NORMED)
      threshold = 0.8
      min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
      if max_val >= threshold:
        print(max_loc, "incoming call....")
        absolute_pt = (max_loc[0] + left + 35, max_loc[1] + top + 35)
        status = 'responding'
        print("responding now.......")
        time.sleep(3)

    if status == 'responding':
      pyautogui.moveTo(absolute_pt)
      pyautogui.click()
      print("waiting for keypad button....")
      status = 'keypad'

    if status == 'keypad':
      left, top, right, bottom = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
      screenshot = pyautogui.screenshot(region=(left, top, right-left, bottom-top))
      screenshot_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
      template_image = cv2.imread('assets/keypad.png')
      res = cv2.matchTemplate(screenshot_image, template_image, cv2.TM_CCOEFF_NORMED)
      threshold = 0.8
      min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
      if max_val >= threshold:
        print(max_loc, "found keypad button....")
        absolute_pt = (max_loc[0] + left + 25, max_loc[1] + top + 25)
        status = 'click numbers'

    if status == 'click numbers':
      pyautogui.moveTo(absolute_pt)
      pyautogui.click()
      print("clicked keypad....")
      status = 'keys'

    if status == 'keys':
      left, top, right, bottom = win32gui.GetWindowRect(win32gui.GetForegroundWindow())
      screenshot = pyautogui.screenshot(region=(left, top, right-left, bottom-top))
      screenshot_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
      template_images = ['assets/k1.png', 'assets/k2.png', 'assets/k#.png']
      keys_locations = []
      
      for template_image_path in template_images:
        template_image = cv2.imread(template_image_path)
        res = cv2.matchTemplate(screenshot_image, template_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >= threshold:
          absolute_pt = (max_loc[0] + left + 17, max_loc[1] + top + 17)
          keys_locations.append(absolute_pt)
          print(f"Found key at {absolute_pt}")
      if len(keys_locations) == 3:
        status = 'keys_found'
    
    if status == 'keys_found':
      time.sleep(1)
      pyautogui.moveTo(keys_locations[0])
      pyautogui.click()
      print("clicked 1....")

      time.sleep(3)
      pyautogui.moveTo(keys_locations[2])
      pyautogui.click()
      print("clicked #....")

      time.sleep(1)
      pyautogui.moveTo(keys_locations[2])
      pyautogui.click()
      print("clicked #....")

      time.sleep(1)
      pyautogui.moveTo(keys_locations[1])
      pyautogui.click()
      print("clicked 2....")

      time.sleep(1)
      pyautogui.moveTo(keys_locations[0])
      pyautogui.click()
      print("clicked 1....")

      time.sleep(3)
      pyautogui.moveTo(keys_locations[2])
      pyautogui.click()
      print("clicked #....")

      time.sleep(1)
      pyautogui.moveTo(keys_locations[0])
      pyautogui.click()
      print("clicked 1....")

      status = 'waiting'
      print("waiting for next call....")

  time.sleep(1)
