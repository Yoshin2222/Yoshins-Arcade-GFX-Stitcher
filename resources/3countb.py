#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "Neo-Geo"
#Set up the names of the GFX Roms/interleaved filename
#GFX Files have a number to prefix the file, example 094.c1.c1
#In the case of Kizuna encounter, the C3/4 files have a different prefix, so this
#table accounts for that. Uses variables to make copy pasting new games faster
gname1 = "043"
gfx_prefix = [gname1,gname1,gname1,gname1]

#Total size of an individual rom
#The ROMs are read in pairs, so ya just need 1 for each pair of files
gfx_romsize = [0x100000,0x100000]

prg_import =  ["043-p1.p1", 0x100000]
import_swapendian = 2 #Swap the endian. 2 Indicates a length of 16-bits, so every 2 bytes

