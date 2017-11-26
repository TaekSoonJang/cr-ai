import pyautogui
import numpy as np
import time

WIDTH = 600
HEIGHT = 1024

UPPER_LEFT = (0, 45)

CARD = [
  (190, 960),
  (300, 960),
  (410, 960),
  (520, 960),
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
      (70, 160)
      (530, 160)
      (70, 800)
      (530, 800)
    """
    play_x = np.random.randint(70, 530)
    # play_y = np.random.randint(181, 986)
    play_y = np.random.randint(510, 800)  # Playing only my side
    pyautogui.click((play_x, play_y))
  else:
    # do nothing
    continue