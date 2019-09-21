import time
import os

import Image
import pyautogui
import numpy
import scipy.misc

image_paths = ["A.png"]
images = {}

if not os.path.exists('images-low-res/'):
    os.makedirs('images-low-res/')

def apply_edge_patch(i):
	res = numpy.copy(i)
	for y in range(i.shape[1]):
		for x in range(i.shape[0]):
			try:
				if (i[y][x][3] > 150 and i[y+1][x][3] > 150 and i[y-1][x][3] > 150 and i[y][x+1][3] > 150 and i[y][x-1][3] > 150):
					res[y][x][3] = 0
			except IndexError:
				pass
	return res

for path in image_paths:
	image_file = Image.open('images/' + path)
	image_hr = numpy.array(image_file)
	print(image_hr.shape)
	image_lr = scipy.misc.imresize(image_hr, (30, 30), mode='RGBA')

	image_lr = apply_edge_patch(image_lr)

	images[path[:path.rfind('.')]] = image_lr
	Image.fromarray(image_lr, 'RGBA').save('images-low-res/' + path)

"""	for y in range(image_lr.shape[1]):
		for x in range(image_lr.shape[0]):
			intensity = (float(image_lr[x][y][0]) + float(image_lr[x][y][1]) + float(image_lr[x][y][2])) / 3 / 255
			c = 255-float(float(intensity) < 0.5)*255
			image_lr[x][y] = [c, c, c]

	images[path[:path.rfind('.')]] = image_lr
	Image.fromarray(image_lr, 'RGB').save('images-low-res/mod_' + path)"""

#print(pyautogui.position())

pos = (140, 200)
pyautogui.moveTo(*pos)

i = images['A']

pyautogui.keyDown('shift')

for y in range(i.shape[1]):
	for x in range(i.shape[0]):
		if (i[y][x][3] > 150):
			pyautogui.moveTo(pos[0] + x*8, pos[1] + y*8)

			pyautogui.mouseDown()
			for v in [list(reversed(range(1, 9)))[0]]:
				pyautogui.moveRel(+v, 0)
				pyautogui.moveRel(0, +v)
				pyautogui.moveRel(-v, 0)
				pyautogui.moveRel(0, -v)
				pyautogui.moveRel(1, 1)
			pyautogui.mouseUp()
			

pyautogui.keyUp('shift')