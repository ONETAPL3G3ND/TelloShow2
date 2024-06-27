import time

from djitellopy import Tello


tello = Tello()
tello.connect()
try:
    tello.takeoff()
except:
    ...
while True:
    tello.move_back(100)
    tello.flip("l")
tello.land()