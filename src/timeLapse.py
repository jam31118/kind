from time import sleep
from picamera import PiCamera
import RPi.GPIO as GPIO
import sys
import requests
#import os
from datetime import datetime
from subprocess import call

OUTDIR = ""
IMGNUM = -1
if (len(sys.argv) == 5):
	OUTDIR = sys.argv[1]
	IMGNUM = int(sys.argv[2])
	TIMESTEP = float(sys.argv[3])
	exp_id = sys.argv[4]
else:
	print("Please enter output directory, IMGNUM, TIMESTEP, exp_id")
	print("Program turning off . . .")
	sys.exit(2)



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
print("LED is going on")
GPIO.output(17,GPIO.HIGH)

## Preparing file transfer
photoDirName = "photoServer/photos/"+exp_id
cmdMkdir = ["bash","src/mkPhotoDirOnServer.sh",photoDirName]
#cmdSendPhoto = ["bash","src/sendPhotoServer.sh",]

timeStep = TIMESTEP
numImg = IMGNUM
PREFIX = "http://dgist.dothome.co.kr/kindProject/updateExperiment_public.php?exp_id="+exp_id+"&done_img_num="

idx = 1

print("Preparing Camera . . .")
cam = PiCamera()
#cam.resolution = (2592,1944)
sleep(1)
cam.start_preview()
print("Starting time-lapse mode . . .")
sleep(2)
for filename in cam.capture_continuous(OUTDIR + "/" +'img{counter}.jpg'):
    print('Captured %s' % filename)
    updateURL = PREFIX + str(idx)
    with requests.Session() as s:
        r = s.get(updateURL)
        if (r.text == "OK"):
            print("Updated to ",idx)
        else:
            print("[FAIL] Update failed, terminating program")
            sys.exit(2)
    call(cmdMkdir)
    call(["bash","src/sendPhotoServer.sh",filename,photoDirName])
    if (idx >= numImg): break
    idx = idx + 1
    sleep(timeStep)

print("LED is going down")
GPIO.output(17,GPIO.LOW)
GPIO.cleanup()
