from djitellopy import tello
from time import sleep

tello = tello.Tello()
tello.connect()
print(tello.get_battery())

"take off"
tello.takeoff()
"get up to required height"
tello.move_up(165)
sleep(.5)
"cool flip"
tello.flip_back()
sleep(.5)
"go to the back of the room"
tello.move_forward(750)
sleep(.5)
"turn"
tello.rotate_clockwise(90)
sleep(.5)
"go to required quadrant"
tello.move_forward(400)
sleep(.5)
"turn"
tello.rotate_clockwise(90)
sleep(.5)
"go back to front of room"
tello.move_forward(800)
sleep(.5)
"turn again"
tello.rotate_clockwise(90)
sleep(.5)
"go back to landing pad"
tello.move_forward(500)
sleep(.5)
"cool flips"
tello.flip_back()
tello.flip_forward()
"land"
tello.land()