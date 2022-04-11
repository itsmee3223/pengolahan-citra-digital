import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('waifu.jpg')

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

negativImg = np.zeros((h, w, 1), dtype=np.uint8)
for x in range(w):
  for y in range(h):
    negativImg[y, x, 0] = 255 - img[y, x, 0]


logImg = np.zeros((h, w, 1), dtype=np.uint8)
for x in range(w):
  for y in range(h):
    logImg[y, x, 0] = 100 * np.log10(1 + img[y, x, 0])

pwrImg = np.zeros((h, w, 1), dtype=np.uint8)
for x in range(w):
  for y in range(h):
    val = 34 * (img[y, x, 0]**0.2)
    if val > 255:
      val = 255
    if val < 0:
      val = 0
    pwrImg[y, x, 0] = val

fig = plt.figure(figsize=(10, 7))
rows = 2
columns = 2

fig.add_subplot(rows, columns, 1)
plt.imshow(grayImg, cmap='gray')
plt.title("Grayscale Image")

fig.add_subplot(rows, columns, 2)
plt.imshow(negativImg, cmap='gray')
plt.title("Negative Image")

fig.add_subplot(rows, columns, 3)
plt.imshow(logImg, cmap='gray')
plt.title("Log Image")

fig.add_subplot(rows, columns, 4)
plt.imshow(pwrImg, cmap='gray')
plt.title("Power Image")

plt.show()