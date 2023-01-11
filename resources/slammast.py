#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS1"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
#The CPS1 is annoyingly specific with the ROM prefixes, so ya need to
#define them each in order. Look in to MAMEs CPS1.C for info on the order
#that GFX are loaded
gfx_prefix = ["mb-1m.3a","mb-3m.5a","mb-2m.4a","mb-4m.6a","mb-5m.7a","mb-7m.9a","mb-6m.8a","mb-8m.10a","mb-10m.3c","mb-12m.5c","mb-11m.4c","mb-13m.6c",]

#The CPS1 has more variance in the size of GFX ROMs. For example, SF2 loads a WORD
#of data between a group of 4 apiece, whereas Ghosts 'n Ghouls loads a byte from a
#group of 8. Group size accounts for this by explicitly declaring how many GFX ROMs
#per group to load. In the case of SF2, [4, 4, 4] indicates that there are 3 groups, 
#each making use of 4 ROMs of data. The group_collec_size dictates how many bytes to
#take from each group. In this case, each group takes 2 Bytes
group_size = [4,4,4]
group_collec_size = [2,2,2]

#Total size of each ROM group
gfx_romsize = [0x80000,0x80000,0x80000]

#Import this data first before we interleave anything
prg_import = ["mbe_23e.8f",0x80000]
import_swapendian = 2 #Swap the endian. 2 Indicates a length of 16-bits, so every 2 bytes

#Define all the names of Program data here
prg_prefix = ["mbe_24b.9e","mbe_28b.9f","mbe_25b.10e","mbe_29b.10f",]

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
#	ROM_LOAD16_WORD_SWAP( "mbe_21a.6f", 0x100000, 0x80000, CRC(d5007b05) SHA1(c55e55908aeda40ca2318c76ccbc05d333676875) )
#	ROM_LOAD16_WORD_SWAP( "mbe_20a.5f", 0x180000, 0x80000, CRC(aeb557b0) SHA1(530551942961d776f0a85852e02bb243840ca671) )
prg_append =  ["mbe_21a.6f", 0x80000,"mbe_20a.5f", 0x80000]
append_swapendian = 2 #Swap the endian. 2 Indicates a length of 16-bits, so every 2 bytes
