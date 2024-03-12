#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS1"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
#The CPS1 is annoyingly specific with the ROM prefixes, so ya need to
#define them each in order. Look in to MAMEs CPS1.C for info on the order
#that GFX are loaded
gfx_prefix = ["rcm_01.3a","rcm_02.4a","rcm_03.5a","rcm_04.6a","rcm_05.7a","rcm_06.8a","rcm_07.9a","rcm_08.10a","rcm_10.3c","rcm_11.4c","rcm_12.5c","rcm_13.6c","rcm_14.7c","rcm_15.8c","rcm_16.9c","rcm_17.10c"]

#The CPS1 has more variance in the size of GFX ROMs. For example, SF2 loads a WORD
#of data between a group of 4 apiece, whereas Ghosts 'n Ghouls loads a byte from a
#group of 8. Group size accounts for this by explicitly declaring how many GFX ROMs
#per group to load. In the case of SF2, [4, 4, 4] indicates that there are 3 groups, 
#each making use of 4 ROMs of data. The group_collec_size dictates how many bytes to
#take from each group. In this case, each group takes 2 Bytes
group_size = [4,4,4,4]

#Each file has bytes read from it when referenced. This list keeps track of how much apiece
rom_byte_size = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#CPS1 Games are weird in that some GFX files can be bigger than the rest of the group, and
#sort of spill over in to the next one at the same offset. This list lets us properly
#reference these files in these "spillage" cases
group_indexes = {}
for i in range (0, len(gfx_prefix), 1):
    group_indexes.update({i : i+1})

prg_import = ["rcmu_23b.8f",0x80000,"rcmu_22b.7f",0x80000,"rcmu_21a.6f"	,0x80000]
import_swapendian = 2 #Swap the endian. 2 Indicates a length of 16-bits, so every 2 bytes



