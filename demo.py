#!/usr/bin/env python

import signal
import flicklib
import time
import curses
from curses import wrapper
from OSC import OSCClient, OSCMessage

client = OSCClient()
client.connect(("192.168.1.200",4559))

client.send(OSCMessage("STARTUP"))
client.send(OSCMessage("THIS IS A VALUE"))

some_value = 5000

@flicklib.move()
def move(x, y, z):
    global xyztxt
    global x1
    global y1
    global z1
    xyztxt = '{:5.3f} {:5.3f} {:5.3f}'.format(x,y,z)
    x1 = x
    y1 = y
    z1 = z
@flicklib.flick()
def flick(start,finish):
    global flicktxt
    flicktxt = start + ' - ' + finish

@flicklib.airwheel()
def spinny(delta):
    global some_value
    global airwheeltxt
    global airwheel
    some_value += delta
    if some_value < 0:
        some_value = 0
    if some_value > 10000:
        some_value = 10000
    airwheel =  (some_value/100)
    airwheeltxt = str(airwheel)


# @flicklib.double_tap()
# def doubletap(position):
#     global doubletaptxt
#     doubletaptxt = position

# @flicklib.tap()
# def tap(position):
#     global taptxt
#     taptxt = position

# @flicklib.touch()
# def touch(position):
#     global touchtxt
#     touchtxt = position

#
# Main display using curses
#

def main(stdscr):
    global x1
    global y1
    global z1
    global xyztxt
    global flicktxt
    global airwheeltxt
    global airwheel
    global touchtxt
    global taptxt
    global doubletaptxt

    x1 = ''
    y1 = ''
    z1= ''
    xyztxt = ''
    flicktxt = ''
    flickcount = 0
    airwheeltxt = ''
    airwheel = some_value
    airwheelcount = 0
    touchtxt = ''
    touchcount = 0
    taptxt = ''
    tapcount = 0
    doubletaptxt = ''
    doubletapcount = 0

    # Clear screen and hide cursor
    stdscr.clear()
    curses.curs_set(0)

    # Add title and footer
    exittxt = 'Control-C to exit'
    title = '**** STARS FLICK BOARD ****'
    stdscr.addstr( 0, (curses.COLS - len(title)) / 2, title)
    stdscr.addstr(22, (curses.COLS - len(exittxt)) / 2, exittxt)
    stdscr.refresh()

    fw_info = flicklib.getfwinfo()

    datawin = curses.newwin( 8, curses.COLS - 6,  2, 3)
    fwwin   = curses.newwin(10, curses.COLS - 6, 11, 3)


    # Update data window continuously until Control-C
    while True:
        datawin.erase()
        datawin.border()
        datawin.addstr(1, 2, 'X Y Z     : ' + xyztxt)
        datawin.addstr(2, 2, 'Flick     : ' + flicktxt)
        datawin.addstr(3, 2, 'Airwheel  : ' + airwheeltxt)
        datawin.refresh()



        if len(flicktxt) > 0:
            client.send(OSCMessage("a/"+flicktxt,[1]))
        elif len(airwheeltxt) > 0:
            client.send(OSCMessage("a/airwheeltxt",[airwheel]))

        elif x1 > 0:
            client.send(OSCMessage("a/xyz",[x1,y1,z1]))


        xyztxt = ''

        # if len(flicktxt) > 0 and flickcount < 5:
        #     flickcount += 1
        # else:
        #     flicktxt = ''
        #     flickcount = 0

        # if len(airwheeltxt) > 0 and airwheelcount < 5:
        #     airwheelcount += 1
        # else:
        #     airwheeltxt = ''
        #     airwheelcount = 0

        # if len(touchtxt) > 0 and touchcount < 5:
        #     touchcount += 1
        # else:
        #     touchtxt = ''
        #     touchcount = 0

        # if len(taptxt) > 0 and tapcount < 5:
        #     tapcount += 1
        # else:
        #     taptxt = ''
        #     tapcount = 0

        # if len(doubletaptxt) > 0 and doubletapcount < 5:
        #     doubletapcount += 1
        # else:
        #     doubletaptxt = ''
        #     doubletapcount = 0

        time.sleep(0.2)

wrapper(main)

