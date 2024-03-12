Thank you for downloading Yoshins Arcade GFX Stitcher!
This Python script is designed to interleave Arcade GFX
(Namely for the CPS2/Neo-Geo) in to a readable format for
tools like Tile Molestor (charming name, i know) as well as
de-interleave your changes. Whether you want Arcade accurate
rips, wanna edit sprites or straight up add new ones to a gane
ya like, this stitchers got ya covered!

-----RUNNING THE SCRIPT----------
To get started, install the latest version of Python. This script
was made using Python 3.10.6 so any version equivalent or higher
should do the trick. Remember to associate .py files with your
Python installation, this is crucial to getting the script to
work. Once done however, it should be as simple as double clicking
the script to use it

-----IT'S RUNNING! NOW WHAT?-------
After installing Python and associating .py files, running the script
should open a new window asking for a ROM Name. What's actually happening
is it's comparing what you input to an associated ,py file in /resources.
If an associated file doesn't exist, the script returns and error and ya can'the
do anything. If the game is supported, simply enter the ROM name, example: dstlk
for Darkstalkers 1. If your enter 1, the script will check if the unzipped ROM is in your
/roms folder. If it exists, the script will interleave the ROMs and output the data
in /interleaved gfx, where you can open it in TM as 4bpp planar, row interleaved.
De-interleaving checks if thst interleaved file exists, and if it does, splitting
it back up in to it's composite ROMs. This is the power of the stitcher as it lets
ya view and edit the raw tiles and shoot them back as 1-1 as possible.

------WAIT, THE GAME I WANT ISN'T THERE, WHAT DO??------
Adding a new game is surprisingly simple. Go to /resources. You can either copy paste
a game from your system of choice and rename it or just make a new .py. The stitcher
requires a little data to work, and it's reccommended you copy paste one of the templates
for simplicities sake. Open that new file

---------------------FOR NEO-GEO---------------------
Write:
System = "Neo-Geo"

This lets the stitcher know this file/game is for the Neo-Geo specifically. This is important
as it determines how the game is interleaved.
Next bit of data is more intimidating to look at than it actually is

gname1 = "Number before each C file, example, 053"
gfx_prefix = [gname1]

The gname1 is a variable. We can set this to something and call it later. This is
first, copy paste in to the gfx_prefix table as many gname1s as ya need to accomodata
the ROMs of ya game. If your game has 4 C roms, your gfx_prefix should look like this

gfx_prefix = [gname1, gname1, gname1, gname1]

Due to the layout of this, you can give individual ROMs their own prefix. For example,
the game Kizuna Encounter has its C1/2 files use the prefix "059", it's C3/4 files use
"216", and the rest use "059". It's table therefore looks like this

gname1 = "059"
gname2 = "216"
gfx_prefix = [gname1,gname1,gname2,gname2,gname1,gname1,gname1,gname1]

Remember, we call a variable later, so using the name of the variable would
be the same as if we used the value of the variable itself. Here's a visualisation

gfx_prefix = [gname1,gname1,gname2,gname2,gname1,gname1,gname1,gname1]
gfx_prefix = ["059", "059", "216", "216",  "059", "059", "059", "059"]

You can of course just use the raw names, but i find using variables make adding
new games easier as you just have to edit the one variable and how many gfx_prefixs
there are, do what ya like.

Lastly, we have gfx_romsize. This determines how much data we have to read from each
group. Remember, the Neo-Geo groups C files in 2s, so in the case of Kizuna Encounter,
we only have to define 4 sizes since there are 8 ROMs. This is how it's laid out

#Total size of an individual rom#Total size of an individual rom
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
#The ROMs are read in pairs, so ya just need 1 for each pair of files
gfx_romsize = [rsize2,rsize3,rsize2,rsize2]

I promise this looks much scarier than it is. It's much and such the same logic
as earlier with gfx_prefix. In this case, the first group is rsize2, or 2MB.
The next is rsize3, which is 4MB, and so on till we cover every group.

Once all that data is given, you're done! The game has been added! It seems like
a lot but it'll become practically second nature after a while

---------------------FOR CPS2---------------------
The CPS2 uses mostly the same logic, with a couple little differences

System = "CPS2"

No shock we need to say the system is CPS2 for the script to work
The gfx_prefix section si the same as the Neo-Geo
gfx_romsize is also mostly the same, the only difference is that you have to
define 1 size per 4 ROMs as the CPS2 loads in groups of 4. Example: SSF2T uses
12 ROMs for gfx, each labeled something."number"m. Here's how it looks

#Total size of an individual rom
rsize1 = 2 << 19 #1048576 bytes, or 1MB
rsize2 = 2 << 20 #2097152 bytes, or 2MB
rsize3 = 2 << 21 #4194304 bytes, or 4MB
rsize4 = 2 << 22 #8388608 bytes, or 8MB
#The CPS2 Interleaves 4 files at a time, so 1 per group
gfx_romsize = [rsize2,rsize1,rsize1]
#Dictates the order in which files are read and written to
file_writes = [13,15,17,19,14,16,18,20,21,23,25,27]

The file_writes section is to accomodate the strange ordering of the ROMs.
Functionally, the interleaver reads the first group, which is sfx.13m, sfx.15m,
sfx.17m and sfx.19m in that order, and this group is 2MB big. Note the size refers
to an INDIVIDUAL ROM.
After adding that, ya should be good to go!

---------------------FOR CPS1---------------------
As of 1.4, the stitcher now supports CPS1 Games! The structure of resources files is
a bit strange, but it should make some sense once you understand a couple key concepts
Unlike the CPS2, ROMs can be read between groups, in essence, "spilling" over in to the next group in the needed
area. Thankfully this only really happens in fringe cases like Forgotten Worlds, but it's still good to know about

To understand how the Stitcher interleaves a "group", let's break down one from Forgotten Worlds

	ROM_LOAD64_BYTE( "lw_2.2b",   0x000000, 0x20000, CRC(4bd75fee) SHA1(c27bfba951a0dc4f493937ceca335c50a1afeddf) ) // == lw-01.9d
	ROM_LOAD64_BYTE( "lw_1.2a",   0x000001, 0x20000, CRC(65f41485) SHA1(fb05dffc87ee2f2b1b6646d54b13671f8eee0429) ) // == lw-01.9d
	ROM_LOAD64_WORD( "lw-08.9b",  0x000002, 0x80000, CRC(25a8e43c) SHA1(d57cee1fc508db2677e84882fb814e4d9ad20543) ) // == lw-08.9f
	ROM_LOAD64_BYTE( "lw_18.5e",  0x000004, 0x20000, CRC(b4b6241b) SHA1(92b6b530e18ce27ba8739ebba0d8096b1551026c) )
	ROM_LOAD64_BYTE( "lw_17.5c",  0x000005, 0x20000, CRC(c5eea115) SHA1(22fe692eaf9dd00a56a76f46c19fb76bb5e5f0d6) )
	ROM_LOAD64_BYTE( "lw_30.8h",  0x000006, 0x20000, CRC(b385954e) SHA1(d33adb5842e7b85d304836bd92a7a96be4ff3694) ) // == lw-12.9g
	ROM_LOAD64_BYTE( "lw_29.8f",  0x000007, 0x20000, CRC(7bda1ac6) SHA1(5b8bd05f52798f98ae16efa2ff61c06e28a4e3a0) ) // == lw-12.9g

First, we add the names to gfx_prefix. This lets the Stitcher reference the file of that name, so for instance, putting 1 in group_indexes
is the same as saying "look at lw_2.2b". 
Next, rom_byte_size. Simply, each ROM has a certain amount of data read from it when referenced, so simply line up the amount with the
referenced ROMs, a WORD simply meaning 2 bytes.
group_size is self explanatory, just how big this group is, how many ROMs are referenced in it
group_indexes is the tricky one. This is here to handle the "spillage" mentioned earlier, more on that in a bit

Following along, the vars would look something like this

gfx_prefix = ["lw_2.2b","lw_1.2a","lw-08.9b","lw_18.5e","lw_17.5c","lw_30.8h","lw_29.8f"]
group_size = [7]
group_indexes = [1,2,3,4,5,6,7]
rom_byte_size = [1,1,2,1,1,1,1]

Just remember, rom_byte_size is basically there to define how many bytes to read from a ROM when it's referenced, group_indexes is used
in tandem with group_size to reference each ROM as needed
Understanding this, the real vars for this game look like this

gfx_prefix = ["lw_2.2b","lw_1.2a","lw-08.9b","lw_18.5e","lw_17.5c","lw_30.8h","lw_29.8f","lw_4.3b","lw_3.3a","lw_20.7e","lw_19.7c","lw_32.9h","lw_31.9f","lw-02.6b","lw_14.10b","lw_13.10a","lw-06.9d","lw_26.10e","lw_25.10c","lw_16.11b","lw_15.11a","lw_28.11e","lw_27.11c",]
rom_byte_size = [1,1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1]

group_size = [7,7,6,6]
group_indexes = [1,2,3,4,5,6,7,8,9,3,10,11,12,13,14,15,16,17,18,19,14,20,21,17,22,23]
#group_indexes = [1, 2, 3, 4, 5, 6, 7
#                 8, 9, 3, 10,11,12,13
#                 14,15,16,17,18,19
#                 14,20,21,17,22,23]

I'll probably tidy this format up EVENTUALLY, like maybe figuring out a way to automatically generate group_indexes so ya don't
have to do that manually, but for now it gets the job done

---------------------FOR PROGRAM DATA---------------------
As of 1.2, the Stitcher can now tinker with Program data, making it generally useful for hacking
a games code/values! There are 2 methods of interaction, interleaving and appending. For this
example, we'll look at Ghouls 'n Ghosts and how the Stitcher loads its program data for editing

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
	
Should the variable prg_prefix exist, the Stitcher will assume you wish to interleave files in that
array. We name all the ROMs we want to interleave in said array. Depending on the game, the group sizes
can be different, but in this case, there are 2 values of 2. This tells the Stitcher to read the first 2
ROMs as the first group, and the next 2 ROMs as the one after that. Grabsize refers to how many bytes to
interleave between the groups, and the Romsize defines how much data to interleave, being the size of either
of the ROMs in the group. With this structure, we've defined 2 groups. For the first group, take 1 byte of data
from each and interleave it 0x20000 times. For example

ROM1
	00 01 00 19
ROM2
	FF A2 06 0A
Resulting data
	00 FF 01 A2 00 06 19 0A
	
We can also uncomment the Swapendian variable to flip the Bytes as their interleaved, as some games store the data
as the opposite endian. This does the same process, but the resulting data would be this 

	FF 00 A2 01 06 00 0A 19

As for Appending, this process is much more straightforward, as the Stitcher merely slaps the data on to the end of
Program data. We define the name of the ROM, and then how big it is. We can also uncomment the append_swapendian
variable here to in order to flip the bytes like the previous example, You can define this array alone in order to use
the as a means to edit an individual ROMs flipped data (see garoup in resources)
