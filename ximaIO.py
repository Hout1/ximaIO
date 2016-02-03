import numpy as np
import os.path
import struct

#General IO functions
def ximaread(imgName):
	""" Reads a file in a xima format (currently only ima, imw and imf are supported). """
	if imgName.endswith('.ima'):
		return imaread(imgName)
	elif imgName.endswith('.imw'):
		return imwread(imgName)
	elif imgName.endswith('.imf'):
		return imfread(imgName)
	else:
		raise Exception("Format not currently supported.")

def ximawrite(img, imgName):
	""" Writes a file in a xima format (currently only ima, imw and imf are supported). """
	if imgName.endswith('.ima'):
		return imawrite(img, imgName)
	elif imgName.endswith('.imw'):
		return imwwrite(img, imgName)
	elif imgName.endswith('.imf'):
		return imfwrite(img, imgName)
	else:
		raise Exception("Format not currently supported.")


#IO operations for ima format.
def imaread(imgName):
	""" Reads a *ima file. ImgName can be with or without extension. """
	if imgName.endswith('.ima'):
		imgName = os.path.splitext(imgName)[0]

	return _imaread(imgName)

def imawrite(img, imgName):
	""" Writes img to imgName. imgName can come with or without extension. """
	if imgName.endswith('.ima'):
		imgName = os.path.splitext(imgName)[0]

	return _imawrite(img, imgName)


#IO operations for imw format.
def imwread(imgName):
	""" Reads a *.imw file. ImgName can be with or without extension. """
	if imgName.endswith('.imw'):
		imgName = os.path.splitext(imgName)[0]

	return _imwread(imgName)

def imwwrite(img, imgName):
	""" Write a *.imw file. ImgName can be with or without extension. """
	if imgName.endswith('.imw'):
		imgName = os.path.splitext(imgName)[0]

	return _imwwrite(img, imgName)


#IO operations for imf format.
def imfread(imgName):
	""" Reads a *.imf file. ImgName can be with or without extension. """
	if imgName.endswith('.imf'):
		imgName = os.path.splitext(imgName)[0]

	return _imfread(imgName)

def imfwrite(img, imgName):
	""" Write a *.imf file. ImgName can be with or without extension. """
	if imgName.endswith('.imf'):
		imgName = os.path.splitext(imgName)[0]

	return _imfwrite(img, imgName)


#Internal functions.
def _imaread(imgName):
	""" Reads a *.ima file. imgName should come with no extension. """
	w, h = _readDim(imgName + '.dim')
	return _readImage(imgName + '.ima', w, h, 'B', 1)

def _imawrite(img, imgName):
	""" Writes img to an imgName.ima file. imgName should come with no extension. """
	_writeDim(img, imgName + '.dim')
	_writeImage(img, imgName + '.ima', 'B')

def _imwread(imgName):
	""" Reads a *.imw file. imgName should come with no extension. """
	w, h = _readDim(imgName + '.dim')
	return _readImage(imgName + '.imw', w, h, '>H', 2)

def _imwwrite(img, imgName):
	""" Writes img to an imgName.imw file. imgName should come with no extension. """
	_writeDim(img, imgName + '.dim')
	_writeImage(img, imgName + '.imw', '>H')

def _imfread(imgName):
	""" Reads a *.imf file. imgName should come with no extension. """
	w, h = _readDim(imgName + '.dim')
	return _readImage(imgName + '.imf', w, h, 'f', 4)

def _imfwrite(img, imgName):
	""" Writes img to an imgName.imf file. imgName should come with no extension. """
	_writeDim(img, imgName + '.dim')
	_writeImage(img, imgName + '.imf', 'f')


def _readDim(dimFile):
	""" Reads a *.dim file and return width and height. """
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

