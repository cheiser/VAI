from PIL import ImageGrab as imggrab
import win32api
import win32con
import os
import time

# NOTE TO SELF: Renaming a python file (.py) to .pyw will make it execute without opening up console...

# TEST FILE!

SCREENSHOTDIR = "\\\\screenshots"
SCREENSHOTPREFIX = "\\\\screenshot-"

def screenGrab(box):
    img = imggrab.grab(box)
    img.save(os.getcwd() + SCREENSHOTDIR + SCREENSHOTPREFIX + str(int(time.time())) + ".png", "PNG")

# win32api.mouse_event(dwFlags, dx, dy, dwData)
#
# dwFlags:
# win32con.MOUSEEVENTF_LEFTDOWN
# win32con.MOUSEEVENTF_LEFTUP
# win32con.MOUSEEVENTF_MIDDLEDOWN
# win32con.MOUSEEVENTF_MIDDLEUP
# win32con.MOUSEEVENTF_RIGHTDOWN
# win32con.MOUSEEVENTF_RIGHTUP
# win32con.MOUSEEVENTF_WHEEL
# win32con.MOUSEEVENTF_ABSOLUTE
#
# dx/dy == absolute screen positions of the mouse
#
# dwData is used if and only if dwFlags == MOUSEEVENTF_WHEEL...
# it specifies the amount of scroll to be used
def moveMouseToTheMiddleAndScrollALittle():
    print("moving mouse")
    win32api.SetCursorPos((450, 200))

    print("scrolling...")
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -120) # Each wheel click == 120...

def main():
    # Check if the directory for screensshots exists and if it doesn't we create it
    if(not(os.path.exists(os.getcwd() + SCREENSHOTDIR))):
        os.mkdir(os.getcwd() + SCREENSHOTDIR)

    # time.sleep(90) # wait 1.5 minutes before taking screenshot
    # screenGrab(())
    # screenGrab((startX, startY, endX, endY))
    # screenGrab((10, 10, 50, 50))
    moveMouseToTheMiddleAndScrollALittle()

if __name__ == '__main__':
    main()