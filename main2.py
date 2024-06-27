import time
from djitellopy import Tello


tello = Tello()
print(tello.query_battery())
tello.connect()
try:
    tello.takeoff()
except:
    ...
while True:
    tello.move_forward(300)
    tello.rotate_clockwise(90)
    tello.flip("f")
time.sleep(3)
tello.land()