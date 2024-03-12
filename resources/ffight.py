#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS1"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
#The CPS1 is annoyingly specific with the ROM prefixes, so ya need to
#define them each in order. Look in to MAMEs CPS1.C for info on the order
#that GFX are loaded
gfx_prefix = ["ff-5m.7a", "ff-7m.9a", "ff-1m.3a", "ff-3m.5a"]

#The CPS1 has more variance in the size of GFX ROMs. For example, SF2 loads a WORD
#of data between a group of 4 apiece, whereas Ghosts 'n Ghouls loads a byte from a
#group of 8. Group size accounts for this by explicitly declaring how many GFX ROMs
#per group to load. In the case of SF2, [4, 4, 4] indicates that there are 3 groups, 
#each making use of 4 ROMs of data. The group_collec_size dictates how many bytes to
#take from each group. In this case, each group takes 2 Bytes
group_size = [4]
#Each file has bytes read from it when referenced. This list keeps track of how much apiece
rom_byte_size = [2,2,2,2]
#CPS1 Games are weird in that some GFX files can be bigger than the rest of the group, and
#sort of spill over in to the next one at the same offset. This list lets us properly
#reference these files in these "spillage" cases
#for i in range(0,len(gfx_prefix),1):
#    group_indexes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

group_indexes = {}
for i in range (0, len(gfx_prefix), 1):
    group_indexes.update({i : i+1})

#Define all the names of Program data here
prg_prefix = ["ff_36.11f", "ff_42.11h","ff_37.12f", "ffe_43.12h"]

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
prg_append =  ["ff-32m.8h", 0x80000]
#append_swapendian = 2

#	ROM_LOAD16_BYTE( "ff_36.11f",      0x00000, 0x20000, CRC(f9a5ce83) SHA1(0756ae576a1f6d5b8b22f8630dca40ef38567ea6) ) // in "30" socket
#	ROM_LOAD16_BYTE( "ff_42.11h",      0x00001, 0x20000, CRC(65f11215) SHA1(5045a467f3e228c02b4a355b52f58263ffa90113) ) // in "35" socket
#	ROM_LOAD16_BYTE( "ff_37.12f",      0x40000, 0x20000, CRC(e1033784) SHA1(38f44434c8befd623953ae23d6e5ff4e201d6627) ) // in "31" socket
#	ROM_LOAD16_BYTE( "ffe_43.12h",     0x40001, 0x20000, CRC(995e968a) SHA1(de16873d1639ac1738be0937270b108a9914f263) ) // in "36" socket
#	ROM_LOAD16_WORD_SWAP( "ff-32m.8h", 0x80000, 0x80000, CRC(c747696e) SHA1(d3362dadded31ccb7eaf71ef282d698d18edd722) )