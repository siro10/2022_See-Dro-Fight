

import time, cv2
from djitellopy import Tello

tello = Tello()
tello.connect()
tello.streamon()

frame_read = tello.get_frame_read()
cv2.imshow('Live Video', frame_read.frame)
cv2.waitKey(1000)
