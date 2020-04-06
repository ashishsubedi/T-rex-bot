from PIL import Image, ImageGrab
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

X1 = 300
Y1 = 350
X2 = 350
Y2 = 400

x_range = X2-X1
y_range = Y2-Y1

timer = 0
TIMERVALUE = 0.04
increased = False

while(True):
    img = ImageGrab.grab(bbox=(X1,Y1,X2,Y2)).convert("L")
    color = 0
    # Image._show(img)
    color = img.getdata()
    color = sum(color)
    color /= (y_range)*x_range
    print(color,timer)
    if(color <= 240):
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        timer+= 1
        time.sleep(TIMERVALUE) 

    if(not increased and timer >= 100):
        X1=300
        X2 = 405
        x_range = X2-X1
        y_range = Y2-Y1
        increased = True
        TIMERVALUE = 0.03
    elif( increased and timer >= 300):
        X1=310
        X2 = 405
        x_range = X2-X1
        y_range = Y2-Y1
        increased = True
        TIMERVALUE = 0.02