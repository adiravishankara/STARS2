#!/usr/bin/python3

import signal
#from libs import Flick
#from Flick import flick
from Flick import flicklib
from time import sleep
from curses import wrapper
from os import system
from OSC import OSCClient, OSCMessage
import flick_code

client = OSCClient()
client.connect(("192.168.0.15",4559))



def main(stdscr):
    global xyztxt
    global x_range
    global y_range
    global z_range
    global flicktxt
    global airwheeltxt
    global touchtxt
    global taptxt
    global doubletaptxt

    xyztxt = ''
    x_range = ''
    y_range = ''
    z_range = ''
    flicktxt = ''
    flickcount = 0
    airwheeltxt = ''
    airwheelcount = 0
    cmd = ""

    while True:
	if len(flicktxt) > 0:
		if flicktxt == "east-west":
			print(flicktxt)
			#client.send(OSCMessage("a1",[1]))
		elif flicktxt == "west-east":
			print(flicktxt)
			#client.send(OSCMessage("a2",[1]))
		elif flicktxt == "north-south":
			print(flicktxt)
			#client.send(OSCMessage("a3",[1]))
		elif flicktxt == "south-north":
			print(flicktxt)
			#client.send(OSCMessage("a4",[1]))
	if len(airwheeltxt) > 0:
		print(airwheeltxt)
		#client.send(OSCMessage("a5",[airwheeltxt]))
	if len(x_range) > 0:
		print(x_range)
		#client.send(OSCMessage("ax",[x_range]))
		x_range = ''
	if len(y_range) > 0:
		print(y_range)
		#client.send(OSCMessage("ay",[y_range]))
		y_range = ''
	if len(z_range) > 0:
		print(z_range)
		#client.send(OSCMessage("az",[z_range]))
		z_range = ''
	sleep(0.02)
