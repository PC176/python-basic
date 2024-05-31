# we can run multiple task simultaneously in different core
from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(500):
            print("Hello")
            sleep(0.2)


class Hi(Thread):
    def run(self):
        for i in range(500):
            print("Hi")
            sleep(0.2)


t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("Bye")
