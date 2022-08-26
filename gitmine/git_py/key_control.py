from re import L
from djitellopy import Tello
import sys
import socket


tello = Tello()

tello.connect()

battery=tello.get_battery()
print(battery)

def battery():
    battery=tello.get_battery()
    print(battery)


def xyz():
    # x=int(input("x"))
    # y=int(input("y"))
    # z=int(input("z"))
    # speed=int(input("speed"))
    #tello.go_xyz_speed( x, y, z, speed)
    tello.go_xyz_speed( 50, -50, 50, 100)

def forward():
    try:range=int(input("range"))
    except ValueError:
        print("数値")
        range=int(input("range"))
    tello.move_forward(range)

def left():
    try:range=int(input("range"))
    except ValueError:
        print("数値")
        range=int(input("range"))
    tello.move_left(range)

def right():
    try:range=int(input("range"))
    except ValueError:
        print("数値")
    tello.move_right(range)

def back():
    try:range=int(input("range"))
    except ValueError:
        print("数値")
        range=int(input("range"))
    tello.move_back(range)

def take():

    tello.takeoff()

def land():
    tello.land()

while 1:
    user=input("制御")

    if (user=="w"):
        forward()
    elif (user=="d"):
        right()
    elif (user=="s"):
        back()
    elif (user=="a"):
        left()
    elif (user=="x"):
        xyz()
    elif (user=="l"):
        land()
    elif (user=="t"):
        take()
    elif (user=="b"):
        battery()
    elif(user=="p"):
        socket.close()
        sys.exit()

    else:
        print("無効な操作")    
