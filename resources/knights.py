#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS1"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
#The CPS1 is annoyingly specific with the ROM prefixes, so ya need to
#define them each in order. Look in to MAMEs CPS1.C for info on the order
#that GFX are loaded
gfx_prefix = ["kr-5m.3a", "kr-7m.5a", "kr-1m.4a", "kr-3m.6a", "kr-6m.7a", "kr-8m.9a", "kr-2m.8a", "kr-4m.10a"]

#The CPS1 has more variance in the size of GFX ROMs. For example, SF2 loads a WORD
#of data between a group of 4 apiece, whereas Ghosts 'n Ghouls loads a byte from a
#group of 8. Group size accounts for this by explicitly declaring how many GFX ROMs
#per group to load. In the case of SF2, [4, 4, 4] indicates that there are 3 groups, 
#each making use of 4 ROMs of data. The group_collec_size dictates how many bytes to
#take from each group. In this case, each group takes 2 Bytes
group_size = [4,4]
#Each file has bytes read from it when referenced. This list keeps track of how much apiece
rom_byte_size = [2,2,2,2,2,2,2,2]
#CPS1 Games are weird in that some GFX files can be bigger than the rest of the group, and
#sort of spill over in to the next one at the same offset. This list lets us properly
#reference these files in these "spillage" cases
#for i in range(0,len(gfx_prefix),1):
#    group_indexes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

#Loop for when the game is being nice to you today!
group_indexes = {}
for i in range (0, len(gfx_prefix), 1):
    group_indexes.update({i : i+1})

#Slap the rest of the data on there for ease of use
prg_import =  ["kr_23e.8f", 0x80000, "kr_22.7f", 0x80000]
import_swapendian = 2
