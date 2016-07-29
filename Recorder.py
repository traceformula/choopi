from time import sleep
from win32api import GetCursorPos, GetKeyState
from VirtualKeycodeLookups import description2keycode as d2k

def KeyIsUp(key):
    keystate = GetKeyState( key) 
    if (keystate == 0) or keystate == 1: return True
    else: return False
    
def KeyIsDown(key):
    return not KeyIsUp(key)
    
def run():
    left_mouse = d2k['Left mouse button']
    quit_key = d2k['Q key']
    while KeyIsUp(quit_key):
        sleep( 0.01)
        if KeyIsDown(left_mouse):
            x, y = GetCursorPos()
            print 'Clicked {} {}'.format(x, y)
            while(KeyIsDown(left_mouse)): 
                sleep(.01)

if __name__ == '__main__':
    run()