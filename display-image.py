#!/usr/bin/env python
from samplebase import SampleBase
from PIL import Image, ImageDraw
import time;

# RPi RGB LED Matrix, hzeller, https://github.com/hzeller/rpi-rgb-led-matrix/
# setimage() ,  liquidthex, https://github.com/liquidthex/ThexBerryClock/blob/master/ThexBerryClock.py#L225


def setimage(im,mx):
	(w,h) = im.size
	pix = im.load()
	for x in range(w):
		for y in range(h):
			(r, g, b) = pix[x, y]
			mx.SetPixel(x, y, r, g, b)

class StaticImage(SampleBase):
	def __init__(self, *args, **kwargs):
		super(StaticImage, self).__init__(*args, **kwargs)
		
		
	def Run(self):
		canvas = self.matrix;
		
		im = Image.open("led.png") # Load static image
		setimage(im, canvas)
		time.sleep(5)   # Display image for 5 seconds
		
		
		im = Image.open("led.jpg") # Load static image
		setimage(im, canvas)
		time.sleep(5)   # Display image for 5 seconds
		
		#Display and repeat a series of images, 0.png, 1.png, 2.png, 3.png etc
		#Change root directory to that of /rpi-rgb-led-matrix/python/samples/
		
		while True:
			for i in range(0,2):
				pacman = ("/home/pi/led/python/samples/ImageSeries/" + str(i) + ".png")
				im = Image.open(pacman)
				setimage(im, canvas)
				time.sleep(0.08)

# Main function
if __name__ == "__main__":
	parser = StaticImage()
	if (not parser.process()):
		parser.print_help()
