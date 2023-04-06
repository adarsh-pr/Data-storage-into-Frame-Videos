from PIL import Image,ImageDraw
import os
import subprocess

lis = os.listdir("DataImg")
dat = []
for i in lis:
    img = Image.open("DataImg/"+i)
    w,h = img.size
    if w == 1280 and h == 720:
        d = img.getdata()
        j=1
        while j < len(d):
            if d[j] == (0,0,0):
                dat.append(0)
            elif d[j] == (255,255,255):
                dat.append(1)
            elif d[j] == (255,0,0):
                print("Completed")
                j=len(d)+1
            else:
                print("fvgghgrjmrubngufn")
            j+=5
fin = ''
for i in dat:
    fin = fin + str(i)
print(fin)
with open("output.txt","w",encoding="utf-8") as f:
    f.write(fin)

