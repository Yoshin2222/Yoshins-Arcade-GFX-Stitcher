#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "midwunit"

#Generate tables for storing data using a dict
prg_prefix = {}
#Midway game GFX are weird in that they explicitly rely on being defined in PRG data in order
#to be displayed. For this reason, we'll interleave the CPU and GFX data
#ROMs share names but alternate between g and j
tbl = ["g","j"]
pref = "l3.1_mortal_kombat_ii_game_rom_u"
pref2 = ".u"
place = 0 #Lee[ track of where we are in the list
#INTERLEAVE PRG DATA
for x in range (0,2,1):
    val = 12
    let = tbl[x]
    stringinp = str("{}{}{}{}{}{}".format(pref,let,val,pref2,let,val))
    prg_prefix.update({x : stringinp})
place = place + 2
print("PLACE = ", place)

#INTERLEAVE GFX DATA
indexes = [14,19,16,20,17,22]
pref = "l1_mortal_kombat_ii_game_rom_u"
pref2 = ".u"
for i in range (0, len(indexes)<<1, 2):
    for x in range (0,2,1):
        val = indexes[i>>1]
        let = tbl[x]
        plc = place + x
        stringinp = str("{}{}{}{}{}{}".format(pref,let,val,pref2,let,val))
        prg_prefix.update({plc : stringinp})
    place = place + 2
    print("PLACE = ", place)

#Here we make an array to store every "group" of ROMs to interleave between
prg_groupsize = [2,4,4,4]
#How many Bytes to interleave between groups
prg_grabsize = [1,1,1,1]
#How big each group is
prg_romsize = [0x80000,0x100000,0x100000,0x100000]