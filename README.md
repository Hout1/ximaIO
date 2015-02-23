# ximaIO
Python module to do basic Input/Output operations on XIMA data (Télécom ParisTech SAR images)

## Introduction
This module provides IO function for xima images. Currently only **imw** (unsigned short imaged) and **ima** (unsigned char images) are supported.

For a detailed description of these format, see [Jean-Marie Nicolas' webpage](http://perso.telecom-paristech.fr/~nicolas/XIMA/index.html)

## Functions
### imw
To read an imw, use: `img = ximaIO.imwread(imgName)`

where imgName is the name of the image with or without the "*.imw" extension.

To write an imw, use: `ximaIO.imwwrite(img, imgName)`

where img is the image to be written and imgName the name of the file with or without the "*.imw" extension.

### ima
To read an ima, use: `img = ximaIO.imaread(imgName)`

where imgName is the name of the image with or without the "*.ima" extension.

To write an ima, use: `ximaIO.imawrite(img, imgName)`

where img is the image to be written and imgName the name of the file with or without the "*.ima" extension.

### General
You can also use the general functions providing a unique interface:

To read: `img = ximaIO.ximaread(imgName)`

In this case, imgName should come with an extension (ima or imw) to determine the format to use.

To write: `ximaIO.ximawrite(img, imgName)`

In this case, imgName should come with an extension (ima or imw) to determine the format to use.

Written by [Sylvain Lobry](http://www.sylvainlobry.com)