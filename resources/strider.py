#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS1"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
#The CPS1 is annoyingly specific with the ROM prefixes, so ya need to
#define them each in order. Look in to MAMEs CPS1.C for info on the order
#that GFX are loaded
gfx_prefix = ["st-2.8a", "st-11.10a", "st-5.4a", "st-9.6a", "st-1.7a", "st-10.9a", "st-4.3a", "st-8.5a",]

#The CPS1 has more variance in the size of GFX ROMs. For example, SF2 loads a WORD
#of data between a group of 4 apiece, whereas Ghosts 'n Ghouls loads a byte from a
#group of 8. Group size accounts for this by explicitly declaring how many GFX ROMs
#per group to load. In the case of SF2, [4, 4, 4] indicates that there are 3 groups, 
#each making use of 4 ROMs of data. The group_collec_size dictates how many bytes to
#take from each group. In this case, each group takes 2 Bytes
group_size = [4,4]
group_collec_size = [2,2]

#Total size of each ROM group
rsize65 = 2 << 15 #65536 bytes, or 64KB
rsize0 = 2 << 18 #524288 bytes, or 512KB
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
gfx_romsize = [rsize0,rsize0]
