__author__ = 'rsukla'

import thread
import time

#simple thread function

def show(name, delay):
    i = 0
    while i < 5:

        time.sleep(delay)
        print '%s, %s' %(name, time.ctime(time.time()))
        i = i + 1

try:
    thread.start_new_thread(show, ('thread 1', 2))
    thread.start_new_thread(show, ('thread 2', 4))
except:
    print "Unable to display the value"

while 1:
    pass

