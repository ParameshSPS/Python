from PIL import Image
import numpy as np

img = Image.open('image.jpg')
ary = np.array(img)

# Split the three channels
r,g,b = np.split(ary,3,axis=2)
r=r.reshape(-1)
g=r.reshape(-1)
b=r.reshape(-1)

# Standard RGB to grayscale 
bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
zip(r,g,b)))
bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
bitmap = np.dot((bitmap > 128).astype(float),255)
im = Image.fromarray(bitmap.astype(np.uint8))
im.save('image.bmp')


# from PIL import Image

# threshold = 30 

# # convert image to a list of pixels
# img = Image.open('image.jpg')
# pixels = list(img.getdata())

# # convert data list to contain only black or white
# newPixels = []
# for pixel in pixels:
#     # if looks like black, convert to black
#     if pixel[0] <= threshold:
#         newPixel = (0, 0, 0)
#     # if looks like white, convert to white
#     else:
#         newPixel = (255, 255, 255)
#     newPixels.append(newPixel)

# # create a image and put data into it

# newImg = Image.new(img.mode, img.size)
# newImg.putdata(newPixels)
# newImg.save('new-image.jpg')