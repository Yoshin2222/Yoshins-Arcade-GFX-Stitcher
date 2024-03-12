#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS1"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
#The CPS1 is annoyingly specific with the ROM prefixes, so ya need to
#define them each in order. Look in to MAMEs CPS1.C for info on the order
#that GFX are loaded
gfx_prefix = ["lw_2.2b","lw_1.2a","lw-08.9b","lw_18.5e","lw_17.5c","lw_30.8h","lw_29.8f","lw_4.3b","lw_3.3a","lw_20.7e","lw_19.7c","lw_32.9h","lw_31.9f","lw-02.6b","lw_14.10b","lw_13.10a","lw-06.9d","lw_26.10e","lw_25.10c","lw_16.11b","lw_15.11a","lw_28.11e","lw_27.11c",]
#The CPS1 has more variance in the size of GFX ROMs. For example, SF2 loads a WORD
#of data between a group of 4 apiece, whereas Ghosts 'n Ghouls loads a byte from a
#group of 8. Group size accounts for this by explicitly declaring how many GFX ROMs
#per group to load. In the case of SF2, [4, 4, 4] indicates that there are 3 groups, 
#each making use of 4 ROMs of data. The group_collec_size dictates how many bytes to
#take from each group. In this case, each group takes 2 Bytes
group_size = [7,7,6,6]
#Each file has bytes read from it when referenced. This list keeps track of how much apiece
rom_byte_size = [1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1]
#CPS1 Games are weird in that some GFX files can be bigger than the rest of the group, and
#sort of spill over in to the next one at the same offset. This list lets us properly
#reference these files in these "spillage" cases
group_indexes = [1,2,3,4,5,6,7,8,9,3,10,11,12,13,14,15,16,17,18,19,14,20,21,17,22,23]
#group_indexes = [1, 2, 3, 4, 5, 6, 7
#                 8, 9, 3, 10,11,12,13
#                 14,15,16,17,18,19
#                 14,20,21,17,22,23]

#Total size of each ROM group
rsize65 = 2 << 15 #65536 bytes, or 64KB
rsize0 = 2 << 18 #524288 bytes, or 512KB
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
#gfx_romsize = [rsize0,rsize65,rsize65]

#Define all the names of Program data here
prg_prefix = ["lw40.12f", "lw41.12h", "lw42.13f", "lw43.13h"]

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
prg_append =  ["lw-07.10g", 0x80000]
append_swapendian = 2 #Swap the endian. 2 Indicates a length of 16-bits, so every 2 bytes
