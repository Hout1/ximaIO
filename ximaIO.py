import numpy as np
import os.path
import struct

def imaread(imgName):
	"""Reads a *ima file. ImgName can be with or without extension"""
	if imgName.endswith('.ima'):
		imgName = os.path.splitext(imgName)[0]

	return _imaread(imgName)

def imawrite(img, imgName):
	"""Writes img to imgName. imgName can come with or without extension"""
	if imgName.endswith('.ima'):
		imgName = os.path.splitext(imgName)[0]

	return _imawrite(img, imgName)

def _imaread(imgName):
	"""Reads a *.ima file. imgName should come with no extension"""
	w, h = _readDim(imgName + '.dim')
	return _readImage(imgName + '.ima', w, h, 'B', 1)

def _imawrite(img, imgName):
	"""Writes img to an imgName.ima file. imgName should come with no extension"""
	_writeDim(img, imgName + '.dim')
	_writeImage(img, imgName + '.ima', 'B')

def _readDim(dimFile):
	""" Reads a *.dim file and return width and height """
	with open(dimFile) as f:
		tmp = f.readline().split()
		w = int(tmp[0])
		h = int(tmp[1])

	return w, h

def _writeDim(img, dimFile):
	""" Writes a *.dim file for image img. """
	w = img.shape[1]
	h = img.shape[0]
	with open(dimFile, 'w') as f:
		f.write(str(w) + ' ' + str(h))

def _readImage(imgName, w, h, type, nbBytes):
	""" Reads an image coded in any bynary format. """
	img = np.empty([h, w])
	with open(imgName) as f:
		for i in range(0, h):
			for j in range(0, w):
				img[i, j] = struct.unpack(type, f.read(nbBytes))[0]

	return img

def _writeImage(img, imgName, type):
	""" Writes an image in any binary format. """
	with open(imgName, 'w') as f:
		for i in range(0, img.shape[0]):
			for j in range(0, img.shape[1]):
				data = struct.pack(type, img[i, j])
				f.write(data)

