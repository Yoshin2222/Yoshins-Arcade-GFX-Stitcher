#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS2"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
gname1 = "avp"
gfx_prefix = [gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1]
#The CPS2 Interleaves 4 files at a time, so 1 per group
gfx_romsize = [0x200000,0x100000]
#Dictates the order in which files are read and written to
file_writes = [13,15,17,19, 14,16,18,20]