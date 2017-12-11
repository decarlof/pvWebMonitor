#!/APSshare/anaconda/x86_64/bin/python

import epics
import os, sys
import time
import matplotlib.image as mpimg

img = mpimg.imread("src.png")

a=0 
while(a == 0):
    mpimg.imsave("livedata1.png", img)
    mpimg.imsave("livedata2.png", img)

    time.sleep(30)
