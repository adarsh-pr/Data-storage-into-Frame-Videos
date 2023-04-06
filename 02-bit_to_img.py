from PIL import Image,ImageDraw
import os

try:
    os.system("mkdir DataImg")
except:
    pass

f=open("binaryfile.txt","r",encoding="utf-8")
exp=f.read()
exp=exp+"E"
flag = True

def upimg ():
    global exp
    global flag
    drawobj.rectangle((0,0,1280,720), fill="cyan")

    a,b,c,d=0,0,5,5
    for i in range(len(exp)):

        if exp[i]=='1':
            shape = (a,b,c,d)
            drawobj.rectangle(shape, fill="white")
        elif exp[i]=='0':
            shape = (a,b,c,d)
            drawobj.rectangle(shape, fill="black")
        elif exp[i] == "E":
            shape = (a,b,c,d)
            drawobj.rectangle(shape, fill="red")
            flag = False
        else:
            pass

        if c == 1280:
            if d+5 > 720:
                exp=exp[i:]
                break
            else:
                b=d
                d=d+5
                a,c=0,5
        else:
            a=c
            c=c+5


count = 1
while flag == True:

    w, h = 1280 , 720
    img = Image.new("RGB", (w, h))
    drawobj = ImageDraw.Draw(img)
    upimg()
    img.show()
    img.save(f"DataImg/Image{count}.png")
    count+=1



