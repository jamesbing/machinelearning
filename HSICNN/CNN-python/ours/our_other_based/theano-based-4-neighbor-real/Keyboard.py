import sys
import time
import threading

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno(), termios.TCSANOW)
            ch = sys.stdin.read(1)
            sys.stdout.write(ch)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()
MyThread = None

class KeyboardEvent(threading.Thread):
    key = ''
    over = False

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not self.over:
            self.key = getch()
            time.sleep(1)

    def stop(self):
        self.over = True;

def StartKeyboardListener():
    global MyThread
    MyThread = KeyboardEvent()
    MyThread.start()

def KeyDown():
    global MyThread
    key = MyThread.key
    MyThread.key = ''
    return key

def StopKeyboardListener():
    global MyThread
    MyThread.stop()
    MyThread = None

if __name__=='__main__':
    StartKeyboardListener()
    while True:
        if KeyDown() == 'q':
            break
    StopKeyboardListener()
    print('no')
