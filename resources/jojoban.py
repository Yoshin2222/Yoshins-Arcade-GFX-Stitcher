#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS3"
pref = "jojoba-simm"
#Generate tables for storing data using a dict
prg_prefix = {}
for i in range (0, 4, 1):
    stringinp = str("{}1.{}".format(pref,i))
    prg_prefix.update({i : stringinp})

#Here we make an array to store every "group" of ROMs to interleave between
prg_groupsize = [4]
#How many Bytes to interleave between groups
prg_grabsize = [1]
#How big each group is
prg_romsize = [2097152]
#swapendian = 2 #Size of Endian, or how many Bytes to flip apiece
#EXAMPLE: 2 is common, so a value of 0x4039 would be swapped to 0x3940
#NOTE: Some games interleave the machine code but leave raw data alone. Comment out the Swapendian should you need to edit one or the other
