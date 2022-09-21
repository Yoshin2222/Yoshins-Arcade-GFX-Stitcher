#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS1"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
#The CPS1 is annoyingly specific with the ROM prefixes, so ya need to
#define them each in order. Look in to MAMEs CPS1.C for info on the order
#that GFX are loaded
#gfx_prefix = [gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1]
gfx_prefix = ["sf2-5m.4a", "sf2-7m.6a", "sf2-1m.3a", "sf2-3m.5a", "sf2-6m.4c", "sf2-8m.6c", "sf2-2m.3c", "sf2-4m.5c", "sf2-13m.4d", "sf2-15m.6d", "sf2-9m.3d", "sf2-11m.5d"]
#gfx_prefix = ["sf2-5m.4a", "sf2-1m.3a", "sf2-7m.6a",  "sf2-3m.5a", "sf2-6m.4c", "sf2-8m.6c", "sf2-2m.3c", "sf2-4m.5c", "sf2-13m.4d", "sf2-15m.6d", "sf2-9m.3d", "sf2-11m.5d"]
#Total size of an individual rom
rsize0 = 2 << 18 #524288 bytes, or 512KB
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
#The CPS1 Interleaves 4 files at a time, so 1 per group
gfx_romsize = [rsize0,rsize0,rsize0]
#Dictates the order in which files are read and written to
#file_writes = [13,15,17,19,14,16,18,20,21,23,25,27]