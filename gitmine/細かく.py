from re import L
from djitellopy import Tello
import sys
import socket


tello = Tello()

tello.connect()

battery=tello.get_battery()
print(battery)

tello.takeoff()

tello.go_xyz_speed( 50, -50, 50, 100)
tello.go_xyz_speed( -50, 50, -50, 100)
tello.go_xyz_speed( 50, -50, 50, 100)
tello.go_xyz_speed( -50, 50, -50, 100)
tello.go_xyz_speed( 50, 50, 50, 100)
tello.go_xyz_speed( -50, 50, -50, 100)


tello.land()



sys.exit()




