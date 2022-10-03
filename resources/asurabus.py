#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "Fuukifg3"

#Define all the names of Program data here
prg_prefix = ["pgm3.u1", "pgm2.u2","pgm1.u3","pgm0.u4"]
#Here we make an array to store every "group" of ROMs to interleave between
prg_groupsize = [4]
#How many Bytes to interleave between groups
prg_grabsize = [1]
#How big each group is
prg_romsize = [524288]
