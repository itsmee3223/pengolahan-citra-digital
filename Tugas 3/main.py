import numpy as np
import matplotlib.pyplot as plt


def grayscaleProcess(img):
    h, w = img.shape[:2]
    grayImg = np.zeros((h, w, 1), dtype=np.uint8)
    for x in range(w):
      for y in range(h):
        r = img[y, x, 0]
        g = img[y, x, 1]
        b = img[y, x, 2]
        val = (r *.299) + (g *.587) + (b *.114)
        if val > 255:
          val = 255
        if val < 0:
          val = 0
        grayImg[y, x, 0] = val
    return grayImg

def histProcess(img):
    h, w = img.shape[:2]
    res = np.zeros((256), dtype=np.uint8)
    for x in range(w):
        for y in range(h):
            r = img[y,x,0]
            res[r] += 1
    return res

def histEqProcess(img):
  h, w = img.shape[:2]
  cdf_img = np.zeros((h,w,1), dtype='uint8')
  cdf_value = np.cumsum(hist)
  ng_n = 255 / (h * w)

  for y in range(h):
    for x in range(w):
      color = img[y,x,0]
      cdf_img[y,x,0] = int(ng_n * cdf_value[color])
  return cdf_img

img = plt.imread('waifu.jpg')
grayImg = grayscaleProcess(img)
hist = histProcess(grayImg)
histEq = histEqProcess(grayImg)

plt.plot(hist)
plt.xlabel('Pixel Value')
plt.ylabel('Pixel Count')
plt.show()

fig = plt.figure(figsize=(10, 7))
rows = 1
columns = 2

fig.add_subplot(rows, columns, 1)
plt.imshow(grayImg, cmap='gray')
plt.title("Grayscale Image")

fig.add_subplot(rows, columns, 2)
plt.imshow(histEq, cmap='gray')
plt.title("Histogram Eq Image")

plt.show()