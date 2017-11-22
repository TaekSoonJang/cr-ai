import pyautogui
import numpy as np
import time

WIDTH = 768
HEIGHT = 1280

UPPER_LEFT = (0, 45)

CARD = [
  (250, 1200),
  (380, 1200),
  (510, 1200),
  (640, 1200),
]

EPSILON = .2
INTERVAL = .7 # second

while True:
  time.sleep(INTERVAL)
  e = np.random.sample() # [0, 1)
  if e < EPSILON:
    card_idx = np.random.randint(0, len(CARD))
    pyautogui.click(CARD[card_idx])
    """
    Playing Area
      (88, 181)
      (678, 181)
      (94, 985)
      (671, 985)
    """
    play_x = np.random.randint(88, 679)
    # play_y = np.random.randint(181, 986)
    play_y = np.random.randint(615, 986)  # Playing only my side
    pyautogui.click((play_x, play_y))
  else:
    # do nothing
    continue