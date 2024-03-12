#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "SF"

#Define all the names of Program data here
prg_prefix = ["sfd-19.2a", "sfd-22.2c", "sfd-20.3a", "sfd-23.3c", "sfd-21.4a", "sfd-24.4c"]
#Here we make an array to store every "group" of ROMs to interleave between
prg_groupsize = [2,2,2]
#How many Bytes to interleave between groups
prg_grabsize = [1,1,1]
#How big each group is
prg_romsize = [0x10000,0x10000,0x10000]
