#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "jchan"

#Define all the names of Program data here
prg_prefix = ["jm01x3.u67", "jm00x3.u68","jm11x3.u69","jm10x3.u70"]

#Here we make an array to store every "group" of ROMs to interleave between
prg_groupsize = [2,2]
#How many Bytes to interleave between groups
prg_grabsize = [1,1]
#How big each group is
prg_romsize = [524288,524288]
swapendian = 2 #Size of Endian, or how many Bytes to flip apiece
#EXAMPLE: 2 is common, so a value of 0x4039 would be swapped to 0x3940
#NOTE: Some games interleave the machine code but leave raw data alone. Comment out the Swapendian should you need to edit one or the other
