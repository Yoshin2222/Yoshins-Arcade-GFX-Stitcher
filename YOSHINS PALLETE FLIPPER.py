import os
import time
flip = "_Flipped"
act = ".act"
title = "YOSHINS PALMOD/TM PAL FLIPPER"
print(title)
pal_len = 0x30

print("ENTER THE NAME OF THE PALLETE YOU'D LIKE TO FLIP")
name = input("NAME = ")
actname = name + ".act"
while not os.path.exists(actname):
    print("INVALID FILENAME! INPUT SOMETHING ELSE")
    name = input("NAME = ")
    actname = name + ".act"

print("Now flipping file...")
time.sleep(1)
flipname = name+flip+act
#Begin flipping
with open(actname, "rb") as input:
    size = os.path.getsize(actname)
    print("Size = ", hex(size))
    temp = []
    temp2 = []
    off = 3
    temp = input.read(size) #Make a copy of the file we can mess with]
    for i in range(0, size, pal_len):
    #Put last color in palette first
        trans_start = i + pal_len - off
        temp2 += temp[i+off:off+trans_start]
    #Grab the rest of the palette
        temp2 += temp[i:i+off]
#Write the flipped data to a new file
with open(flipname, "wb") as out:
    out.write(bytes(temp2))


