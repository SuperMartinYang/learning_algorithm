from time import *

while True:
    dt = localtime()
    print dt[3], " : ", dt[4]
    sleep(20)

raw_input()
