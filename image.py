import os
import numpy as np
import csv
from PIL import Image 

image_file = Image.open("probablyashitphoto.png")
image_file = image_file.resize((32*4, 24*4))
image_file = image_file.convert('1') 
image_file.save('result.png')

file = 'probablyashitphoto.png'
location = ""
path = os.path.join(location, file)
os.remove(path)

im = Image.open("result.png")
row,col = im.size
data = [[0 for i in range(row)] for i in range(col)]
pixels= im.load()
for i in range(row):
  for j in range(col):
    if pixels[i, j] == 255: data[j][i] = 1
    else: data[j][i] = 0


new = ""
for i in range(col):
  for j in range(row):
    new += str(data[i][j])

  print(new)
  new = ""

filename = "file.csv"
f = open(filename, "w+")
f.close()

with open(filename, 'w') as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writerows(data)


print(data)



