import logging
from time import sleep
from picamera import PiCamera
from fractions import Fraction
from drivers.daynight_driver.histogram import compute_histogram, weighted_means
import cv2

DAY_MODE = "day"
NIGHT_MODE = "night"
NIGHT = 40
DAY = 230
CHECK = 5

cam = None
mode = DAY_MODE

def night_mode(cam):
    """
    Switches the camera to night mode.

    :param cam: the PiCamera to tweak
    """
    logging.info("Switching to night-time mode")
    cam.framerate = Fraction(1, 6)
    cam.shutter_speed = 3000000
    cam.exposure_mode = 'off'
    cam.ISO = 800
    cam.exposure_compensation = 25
    cam.awb_mode = 'off'
    cam.awb_gains = (2.0, 2.0)
    logging.info("Waiting for auto white balance")
    sleep(10)


def day_mode(cam):
    """
    Switches the camera to day mode.

    :@param cam: the PiCamera to tweak
    """
    logging.info("Switching to day-time mode")
    cam.shutter_speed = 0
    cam.exposure_mode = 'auto'
    cam.ISO = 200
    cam.exposure_compensation = 25
    cam.awb_mode = 'auto'
    logging.info("Waiting for auto white balance")
    sleep(10)

def init(): 
    global cam, mode
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    cam = PiCamera()
    cam.led = False
    mode = DAY_MODE

def loop():
    global mode
    newMode = ""

    pic = cam.capture('ram', format='jpeg', use_video_port=True)
    pic = cv2.imread(pic)
    hist = compute_histogram(pic)
    means = weighted_means(hist)

    if means["read"] >= DAY and\
        means["green"] >= DAY and\
        means["blue"] >= DAY:
        day_mode(cam)
        newMode = DAY_MODE
    
    if means["red"] <= NIGHT and\
        means["green"] <= NIGHT and\
        means["blue"] <= NIGHT:
        night_mode(cam)
        newMode = NIGHT_MODE
    
    mode = newMode
    return newMode


if __name__ == "__main__":
    init()

    while True:
        loop()
