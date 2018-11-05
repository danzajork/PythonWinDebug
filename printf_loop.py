from ctypes import *
import time

msvcrt = cdll.msvcrt
counter = 0

while 1:
    msvcrt.printf("loop iteration %d\n" % counter)
    time.sleep(2)
    counter +=1
