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
As of 1.1, the stitcher now supports CPS1 Games! The structure of resources files is
much and such the same as CPS2, the only real difference is the absence of file_writes,
and that gfx_prefix requires every ROM name be explicit
For example, Final Fight (ffight) has it's gfx_prefix setup like this

gfx_prefix = ["ff-5m.7a", "ff-7m.9a", "ff-1m.3a", "ff-3m.5a"]

Like the CPS2, ROMs are read in groups of 4, so each gfx_romsize accounts for 1 of the
groups

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
