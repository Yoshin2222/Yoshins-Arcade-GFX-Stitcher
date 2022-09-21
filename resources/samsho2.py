#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "Neo-Geo"
#Set up the names of the GFX Roms/interleaved filename
#GFX Files have a number to prefix the file, example 094.c1.c1
#In the case of Kizuna encounter, the C3/4 files have a different prefix, so this
#table accounts for that. Uses variables to make copy pasting new games faster
gname1 = "063"
gfx_prefix = [gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1]
#Total size of an individual rom#Total size of an individual rom
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
#The ROMs are read in pairs, so ya just need 1 for each pair of files
gfx_romsize = [rsize2,rsize2,rsize2,rsize2]