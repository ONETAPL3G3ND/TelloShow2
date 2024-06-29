import time

from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_back(300)

time.sleep(10)

tello.land()