@flicklib.move()
def move(x, y, z):
    global xyztxt, x_range, y_range, z_range
    xyztxt = '{:5.3f} {:5.3f} {:5.3f}'.format(x,y,z)
    x_range = x  #find a divisor
    if x_range < 30:
        x_range = 30
    if x_range > 90:
        x_range = 90
    y_range = y
    if y_range < 30:
        y_range = 30
    if y_range > 90:
        y_range = 90
    z_range = z
    if z_range < 30:
        z_range = 30
    if z_range > 90:
        z_range = 90
    print(xyztxt)
@flicklib.flick()
def flick(start,finish):
    global flicktxt
    flicktxt = start + '-' + finish
    
    print(flicktxt)
@flicklib.airwheel()
def spinny(delta):
    global some_value
    global airwheeltxtq
    some_value += delta
    if some_value < 500:
        some_value = 500
    if some_value > 10000:
        some_value = 10000
    airwheeltxt = (some_value)
    print(airwheeltxt)

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

    
