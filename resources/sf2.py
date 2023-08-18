#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS1"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
#The CPS1 is annoyingly specific with the ROM prefixes, so ya need to
#define them each in order. Look in to MAMEs CPS1.C for info on the order
#that GFX are loaded
gfx_prefix = ["sf2-5m.4a", "sf2-7m.6a", "sf2-1m.3a", "sf2-3m.5a", "sf2-6m.4c", "sf2-8m.6c", "sf2-2m.3c", "sf2-4m.5c", "sf2-13m.4d", "sf2-15m.6d", "sf2-9m.3d", "sf2-11m.5d"]

#The CPS1 has more variance in the size of GFX ROMs. For example, SF2 loads a WORD
#of data between a group of 4 apiece, whereas Ghosts 'n Ghouls loads a byte from a
#group of 8. Group size accounts for this by explicitly declaring how many GFX ROMs
#per group to load. In the case of SF2, [4, 4, 4] indicates that there are 3 groups, 
#each making use of 4 ROMs of data. The group_collec_size dictates how many bytes to
#take from each group. In this case, each group takes 2 Bytes
group_size = [4,4,4]
#Each file has bytes read from it when referenced. This list keeps track of how much apiece
rom_byte_size = [2,2,2,2,2,2,2,2,2,2,2,2]
#CPS1 Games are weird in that some GFX files can be bigger than the rest of the group, and
#sort of spill over in to the next one at the same offset. This list lets us properly
#reference these files in these "spillage" cases
group_indexes = [1,2,3,4,5,6,7,8,9,10,11,12]
#Keeps track of the smallest ROM per group
assemble_sizes = [0x80000, 0x80000, 0x80000]
#Gonna level with ya, extremely lazy solution to splitting up groups.
#For instance, in SF2, the first 2 ROMs have 2 bytes apiece placed in to the EVEN Table
#Then the next 2 have 2 bytes placed in the ODD table
#Forgotten world uses the first 3 ROMs for the first table, then the next 4, and so on
split_table = [0,0,1,1,0,0,1,1,0,0,1,1]

#Total size of each ROM group
rsize0 = 2 << 18 #524288 bytes, or 512KB
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
gfx_romsize = [rsize0,rsize0,rsize0]

#Define all the names of Program data here
prg_prefix = ["sf2e_30g.11e", "sf2e_37g.11f", "sf2e_31g.12e", "sf2e_38g.12f", "sf2e_28g.9e", "sf2e_35g.9f", "sf2_29b.10e", "sf2_36b.10f"]
#Here we make an array to store every "group" of ROMs to interleave between
prg_groupsize = [2,2,2,2]
#How many Bytes to interleave between groups
prg_grabsize = [1,1,1,1]
#How big each group is
prg_romsize = [0x20000,0x20000,0x20000,0x20000]
