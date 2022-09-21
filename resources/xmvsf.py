#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS2"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
gname1 = "xvs"
gfx_prefix = [gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1]
#Total size of an individual rom
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
#The CPS2 Interleaves 4 files at a time, so 1 per group
gfx_romsize = [rsize3,rsize3]
#Dictates the order in which files are read and written to
file_writes = [13,15,17,19,14,16,18,20]