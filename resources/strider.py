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

#Define all the names of Program data here
prg_prefix = ["30.11f", "35.11h","31.12f", "36.12h"]

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
prg_append =  ["st-14.8h", 0x80000]
append_swapendian = 2

#	ROM_LOAD16_BYTE( "30.11f",        0x00000, 0x20000, CRC(da997474) SHA1(3e4ac98f9a6967d61899281b31c7de779723397b) )
#	ROM_LOAD16_BYTE( "35.11h",        0x00001, 0x20000, CRC(5463aaa3) SHA1(e2d07ec2d818e9a2e2d7a77ff0309ae4011c0083) )
#	ROM_LOAD16_BYTE( "31.12f",        0x40000, 0x20000, CRC(d20786db) SHA1(c9c75488e6bb37cfd0d56073faf87ff5713bc9a0) )
#	ROM_LOAD16_BYTE( "36.12h",        0x40001, 0x20000, CRC(21aa2863) SHA1(446dc9280630318deb423531210a4eedfb4adfa6) )
#	ROM_LOAD16_WORD_SWAP( "st-14.8h", 0x80000, 0x80000, CRC(9b3cfc08) SHA1(a7d7f270a097437affa845d80bed82a1fa874878) )  // in "32" socket



