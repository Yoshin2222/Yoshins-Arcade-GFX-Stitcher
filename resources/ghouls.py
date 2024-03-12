#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS1"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
#The CPS1 is annoyingly specific with the ROM prefixes, so ya need to
#define them each in order. Look in to MAMEs CPS1.C for info on the order
#that GFX are loaded
gfx_prefix = ["dm-05.3a", "dm-07.3f", "dm-06.3c", "dm-08.3g", "09.4a", "18.7a", "13.4e", "22.7e", "11.4c", "20.7c", "15.4g", "24.7g", "10.4b", "19.7b", "14.4f", "23.7f", "12.4d", "21.7d", "16.4h", "25.7h"]

#The CPS1 has more variance in the size of GFX ROMs. For example, SF2 loads a WORD
#of data between a group of 4 apiece, whereas Ghosts 'n Ghouls loads a byte from a
#group of 8. Group size accounts for this by explicitly declaring how many GFX ROMs
#per group to load. In the case of SF2, [4, 4, 4] indicates that there are 3 groups, 
#each making use of 4 ROMs of data. The group_collec_size dictates how many bytes to
#take from each group. In this case, each group takes 2 Bytes
group_size = [4,8,8]
#Each file has bytes read from it when referenced. This list keeps track of how much apiece
rom_byte_size = [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#CPS1 Games are weird in that some GFX files can be bigger than the rest of the group, and
#sort of spill over in to the next one at the same offset. This list lets us properly
#reference these files in these "spillage" cases
#for i in range(0,len(gfx_prefix),1):
#    group_indexes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

#Loop for when the game is being nice to you today!
group_indexes = {}
for i in range (0, len(gfx_prefix), 1):
    group_indexes.update({i : i+1})

#Total size of each ROM group
rsize65 = 2 << 15 #65536 bytes, or 64KB
rsize0 = 2 << 18 #524288 bytes, or 512KB
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
assemble_sizes = [0x40000,rsize65,rsize65]


#Define all the names of Program data here
prg_prefix = ["dme_29.10h", "dme_30.10j", "dme_27.9h", "dme_28.9j"]

#Here we make an array to store every "group" of ROMs to interleave between
prg_groupsize = [2,2]
#How many Bytes to interleave between groups
prg_grabsize = [1,1]
#How big each group is
prg_romsize = [0x20000,0x20000]
#swapendian = 2 #Size of Endian, or how many Bytes to flip apiece
#EXAMPLE: 2 is common, so a value of 0x4039 would be swapped to 0x3940
#NOTE: Some games interleave the machine code but leave raw data alone. Comment out the Swapendian should you need to edit one or the other

#Slap the rest of the data on there for ease of use
prg_append =  ["dm-17.7j", 0x80000]
#append_swapendian = 2
