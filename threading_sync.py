__author__ = 'rsukla'

#Using threading module to demostrate how both the threads will run concurrently

import threading
import time


class mythread(threading.Thread):  #this is the concept of inheritance

    def __init__(self, name, delay, id): #overidding the _init_ function to include more items

        threading.Thread.__init__(self)  # we have to always call the base class __init_ function
        self.name = name
        self.delay = delay
        self.id = id

    def run(self):

        print "Starting thread", self.name
        threadlock.acquire()
        func(self.name, self.delay, 5)
        print "Exiting thread", self.name
        threadlock.release()

def func(name, delay, counter):

    while counter:

        print "Thread_Name is %s and time is %s" % (name, time.ctime(time.time()))
        time.sleep(delay)
        counter -= 1

threadlock = threading.Lock()
threads = []

r = mythread('Thread 1', 2, 1)
p = mythread('Thread 2', 4, 2)

r.start()
p.start()


threads.append(r)
threads.append(p)

print threads









