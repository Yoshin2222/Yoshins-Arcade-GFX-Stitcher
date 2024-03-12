#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS2"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
gname1 = "vam"
gfx_prefix = [gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1]
#Total size of an individual rom
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
#The CPS2 Interleaves 4 files at a time, so 1 per group
gfx_romsize = [rsize3,rsize1]
#Dictates the order in which files are read and written to
file_writes = [13,15,17,19,14,16,18,20]

#Define all the names of Program data here
#prg_prefix = ["vam.11m", "vam.12m"]

#Here we make an array to store every "group" of ROMs to interleave between
#prg_groupsize = [2]
#How many Bytes to interleave between groups
#prg_grabsize = [2]
#How big each group is
#prg_romsize = [0x200000]
#swapendian = 2 #Size of Endian, or how many Bytes to flip apiece
#EXAMPLE: 2 is common, so a value of 0x4039 would be swapped to 0x3940
#NOTE: Some games interleave the machine code but leave raw data alone. Comment out the Swapendian should you need to edit one or the other

#Slap the rest of the data on there for ease of use
prg_import =  ["vam.01", 0x20000, "vam.02", 0x20000]
#import_swapendian = 2 #Swap the endian. 2 Indicates a length of 16-bits, so every 2 bytes
#Slap the rest of the data on there for ease of use
prg_append =  ["vam.11m", 0x200000,"vam.12m", 0x200000]
append_swapendian = 2 #Swap the endian. 2 Indicates a length of 16-bits, so every 2 bytes