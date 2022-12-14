#Used to navigate file directories
import os
import importlib
import sys

#DANGEROUTS TO MUCK WITH STUFF UNDER THIS LINE, BE WARNED
var_prefix = "GFX_C"
inter_data = bytes()
#Generate folders if they don't already exist
rompath = r'roms'
if not os.path.exists(rompath):
    os.makedirs(rompath)
gfxpath = r'interleaved_gfx'
if not os.path.exists(gfxpath):
    os.makedirs(gfxpath)
respath = r'resources'
if not os.path.exists(respath):
    os.makedirs(respath)

print("---------- YOSHINS ARCADE GFX STITCHER ----------")
game_name = input("Enter ROM name here: ")
#Invalid Input
while not os.path.exists(os.path.join(respath, game_name+".py")):
    print("GAME NOT SUPPORTED! Look in resources")
    game_name = input("Try something else: ")    
#Valid input
print("ROM_Name = ", game_name)
script_action = input("Great, now what? 1:Interleave 2: De-Interleave: ")
#Invalid Input
while script_action != "1" and script_action != "2":
    print("Why'd ya do that? Now ya just look silly")
    script_action = input("Try something else: ")  

#Valid Input 1
if script_action == "1":
    print("Interleaving, please wait...")
#Valid Input 2
if script_action == "2":
    print("De-Interleaving, please wait...")

#Make a folder for the game ROM is there isn't one already
gamepath = os.path.join(rompath, game_name)
if not os.path.exists(gamepath):
    os.makedirs(gamepath)
#Grab the needed resource file
sys.path.append(respath)
res_file = importlib.import_module(game_name.lower()) #Ensure lowercase for ease of input
#Grab the number of ROMs to read and assign the name of the Interleaved GFX
num_of_gfx_roms = len(res_file.gfx_prefix)
inter_name = str(game_name).upper() + "_INTERLEAVED_GFX"

print(inter_name)
#Assign appropriate names/vars to be used later
if res_file.System == "Neo-Geo":
#    filename = ["{}-c{}.c{}".format(res_file.gfx_prefix[i].lower(), res_file.file_writes[i],res_file.file_writes[i]) for i in range(0, num_of_gfx_roms)]
    filename = ["{}-c{}.c{}".format(res_file.gfx_prefix[i].lower(), i + 1,i + 1) for i in range(0, num_of_gfx_roms)]
if res_file.System == "CPS2":
    filename = ["{}.{}m".format(res_file.gfx_prefix[i], res_file.file_writes[i],res_file.file_writes[i]) for i in range(0, num_of_gfx_roms)]
#-------------------------------NOT IMPLEMENTED YET!!!!!!!!!!!!-------------------------------
if res_file.System == "CPS1":
    filename = ["{}".format(res_file.gfx_prefix[i]) for i in range(0, num_of_gfx_roms)]

#Display some info, mostly aesthetic if i'm honest
print("System =", res_file.System)
print(filename)
gfx_file = ["{}{}" .format(var_prefix, i) for i in range(1, num_of_gfx_roms + 1)]
#Generate tables for storing data using a dict
gfx_table = {}
for i in range (0, num_of_gfx_roms, 1):
   gfx_table.update({i : []})

#Function used to write data to interleaved files
def grab_inter_data(i):
    for k in range (0, res_file.gfx_romsize[i>>1] >> 1, 1):
        gfx_table[0] += bytes(gfx_file[i].read(2))
        gfx_table[0] += bytes(gfx_file[i+1].read(2))

#Function used to write data to C files
def grab_Cx_data(x, inp):
    for i in range (0, res_file.gfx_romsize[x>>1] >> 1, 1):
#        print("interleave", i)
        gfx_table[x] += bytes(inp.read(2))
        gfx_table[x+1] += bytes(inp.read(2)) 

#//////////////////// START OF CASE NEO-GEO ////////////////////
def CASE_NEO_GEO():
#///// INTERLEAVE DATA ///////////////
    if script_action == "1":
   #Grab data from the interleaved GFX file
        for i in range (0, num_of_gfx_roms, 2):
#        if os.path.exists(os.path.join(gamepath, filename[i])):
            with open (os.path.join(gamepath, filename[i]), "rb") as gfx_file[i]:
                with open (os.path.join(gamepath, filename[i+1]), "rb") as gfx_file[i+1]: 
                    print("Interleaving", filename[i], filename[i+1])
                    grab_inter_data(i)

        #Write the final interleaved data
        with open (os.path.join(gfxpath, inter_name), "wb") as Interleaved_GFX:   
            Interleaved_GFX.write(bytes(gfx_table[0]))

#///// DE-INTERLEAVE DATA ////////////
    if script_action == "2":
    #Grab data from the interleaved GFX file
        with open (os.path.join(gfxpath, inter_name), "rb") as Interleaved_GFX:   
            for i in range (0, num_of_gfx_roms, 2):
                print("De-Interleaving", filename[i], filename[i+1])
                grab_Cx_data(i,Interleaved_GFX)

    #Write the final Cx data
        for k in range (0, num_of_gfx_roms, 1):
            with open (os.path.join(gamepath, filename[k]), "wb") as gfx_file[k]:
                gfx_file[k].write(bytes(gfx_table[k]))

#//////////////////// END OF CASE NEO-GEO ////////////////////


#1. Split each base ROM into its even and odd words.
#2. Interleave these on a word basis into eight files: The 13-15 evens, 
#the 13-15 odds, the 17-19 evens, the 17-19 odds, the 14-16 evens, 
#the 14-16 odds, the 18-20 evens, and the 18-20 odds.
#3. Interleave each half's evens together and each half's odds together, 
#both on a 64-byte basis. You should now have four files: the 13-15-17-19 
#evens, the 13-15-17-19 odds, the 14-16-18-20 evens, and the 14-16-18-20 odds.
#4. Interleave each half's odds and evens with each other on a 1,048,576-byte 
#basis: You should now have two files, the 13-15-17-19 and the 14-16-18-20.
#5. Append the latter to the former.

#Holds the EVEN and ODD Bytes in as many tables as there are GFX Roms
def grab_ROM_Data(i):
    for k in range (0, res_file.gfx_romsize[i>>2] >> 2,1):
#Within each of those chunks, words from two of the associated base 
#ROMs are interleaved for each 8x8 subtile (64 bytes). The ROMs read 
#from alternate between each subtile. Meaning the first subtile is 
#comprised of interleaved words form the first two of the four associate 
#ROMs, the next tile is comprised of interleaved words from the second 
#two of the four associate ROMs. So, for example, the very first subtile
#would be comprised of alternating words from ROMs 13 and 15, the second 
#would comprised of alternating words from ROMs 17 and 19, the third would 
#switch back to alternating words from ROMs 13 and 15... etc.

        #Table 0 stores the EVEN Bytes for 13/15m
        tempfile[i] += gfx_file[i].read(2) #13m #14m
        tempfile[i] += gfx_file[i+1].read(2) #15m #16m
        #Table 1 stores the ODD Bytes for 13/15m
        tempfile[i+1] += gfx_file[i].read(2) #17m #18m
        tempfile[i+1] += gfx_file[i+1].read(2) #19m #20m
        #Table 2 stores the EVEN Bytes for 17/19m
        tempfile[i+2] += gfx_file[i+2].read(2) #13m #14m
        tempfile[i+2] += gfx_file[i+3].read(2) #15m #16m
        #Table 3 stores the ODD Bytes for 17/19m
        tempfile[i+3] += gfx_file[i+2].read(2) #17m #18m
        tempfile[i+3] += gfx_file[i+3].read(2) #19m #20m
#        print("interleave", k)
#    for j in range (0, res_file.gfx_romsize[i>>2], 64):
#    ["-------------- table 0 --------------"]
    print(filename[i],filename[i+1],"EVEN")
#    ["-------------- table 1 --------------"]
    print(filename[i],filename[i+1],"ODD")
#    ["-------------- table 2 --------------"]
    print(filename[i+2],filename[i+3],"EVEN")
#    ["-------------- table 3 --------------"]
    print(filename[i+2],filename[i+3],"ODD")


    j = 0
    while j < (res_file.gfx_romsize[i>>2]) << 1:
#Interleave every 64 Bytes between groups
        #The first table stores the EVEN WORDs of the 
        #group
        #Grab 64 bytes from the 13/15 EVEN WORDs table
        tempfile2[i >> 1] += tempfile[i][j:j+64]
        #Grab 64 bytes from the 17/19 EVEN WORDs table
        tempfile2[i >> 1] += tempfile[i+2][j:j+64]
        #The second table stores the ODD WORDs of the 
        #group
        #Grab 64 bytes from the 13/15 ODD WORDs table
        tempfile2[(i >> 1) + 1] += tempfile[i+1][j:j+64]
        #Grab 64 bytes from the 17/19 ODD WORDs table
        tempfile2[(i >> 1) + 1] += tempfile[i+3][j:j+64]
        j += 64
#    ["-------------- table2 - 0 --------------"]
    print(filename[i],filename[i+1],filename[i+2],filename[i+3],"EVEN")
#    ["-------------- table2 - 1--------------"]
    print(filename[i],filename[i+1],filename[i+2],filename[i+3],"ODD")
    j = 0
    while len(tempfile3[i>>2]) < (res_file.gfx_romsize[i>>2]) << 2:
        #Table 0 stores the EVEN Bytes for 13/15m, 17/19m
        #Table 1 stores the ODD Bytes for 13/15m, 17/19m
        #Table 2 stores the EVEN Bytes for 17/19m
        #Table 3 stores the ODD Bytes for 17/19m
        tempfile3[i>>2] += tempfile2[(i>>1)][j:j+(2 << 19)]
        tempfile3[i>>2] += tempfile2[(i>>1) + 1][j:j+(2 << 19)]
        j += 2 << 19 #Add offset to grab the right data

#Append the groups final data to the output
    gfx_table[0] += tempfile3[i>>2]

def cps2_de_interleave1(inp, loopindex):
    #Properly retrieve each "Group" of Even and Odd Bytes
#    ["-------------- table2 - 0 --------------"]
    print(filename[i],filename[i+1],filename[i+2],filename[i+3],"EVEN")
#    ["-------------- table2 - 1--------------"]
    print(filename[i],filename[i+1],filename[i+2],filename[i+3],"ODD")
    j = 0
    while j < (res_file.gfx_romsize[loopindex>>2]) << 2:
        tempfile2[(loopindex >> 1)] += tempfile3[(loopindex>>2)][j:j+(2 << 19)]
        tempfile2[(loopindex >> 1)+1] += tempfile3[(loopindex>>2)][j+(2 << 19):j+(2 << 20)]
        j += 2 << 20


        #Extract each 64 Byte chunk
    j = 0
#    ["-------------- table 0 --------------"]
    print(filename[loopindex],filename[loopindex+1],"EVEN")
#    ["-------------- table 1 --------------"]
    print(filename[loopindex],filename[loopindex+1],"ODD")
#    ["-------------- table 2 --------------"]
    print(filename[loopindex+2],filename[loopindex+3],"EVEN")
#    ["-------------- table 3 --------------"]
    print(filename[loopindex+2],filename[loopindex+3],"ODD")    
    while j < (res_file.gfx_romsize[loopindex>>2]) << 1:
#De-Interleave every 64 Bytes between groups
        #The first table in the group contains the
        #EVEN WORDs of 13/15m
        tempfile[loopindex] += tempfile2[loopindex >> 1][j:j+64]
        #The second table in the group contains the
        #EVEN WORDs of 17/19m
        tempfile[loopindex+2] += tempfile2[loopindex >> 1][j+64:j+128]
        #The third table in the group contains the
        #ODD WORDs of 13/15m
        tempfile[loopindex+1] += tempfile2[(loopindex >> 1)  + 1][j:j+64]
        #The fourth table in the group contains the
        #ODD WORDs of 17/19m
        tempfile[loopindex+3] += tempfile2[(loopindex >> 1) + 1][j+64:j+128]
        j += 128

    j = 0
    while j < res_file.gfx_romsize[loopindex>>2]:
        #At the beginning of interleaving, we stitched
        #the ROMs together 2 bytes  at a time, first
        #Grab 2 bytes from EVEN 13/15m for 13m
        gfx_table[loopindex] += tempfile[loopindex][j:j+2]
        #Grab 2 bytes from EVEN 13/15m for 15m
        gfx_table[loopindex+1] += tempfile[loopindex][j+2:j+4]
        #Grab 2 bytes from ODD 13/15m for 13m
        gfx_table[loopindex] += tempfile[loopindex+1][j:j+2]
        #Grab 2 bytes from 0DD 13/15m for 15m
        gfx_table[loopindex+1] += tempfile[loopindex+1][j+2:j+4]

        #Repeat this process for the other 2 GFX
        #ROMs in the group
        #Grab 2 bytes from EVEN 17/19m for 17m
        gfx_table[loopindex+2] += tempfile[loopindex+2][j:j+2]
        #Grab 2 bytes from EVEN 17/19m for 19m
        gfx_table[loopindex+3] += tempfile[loopindex+2][j+2:j+4]
        #Grab 2 bytes from ODD 17/19m for 17m
        gfx_table[loopindex+2] += tempfile[loopindex+3][j:j+2]
        #Grab 2 bytes from 0DD 17/19m for 19m
        gfx_table[loopindex+3] += tempfile[loopindex+3][j+2:j+4]
        j += 4

#//////////////////// START OF CASE CPS2 ////////////////////
def CASE_CPS2():
#Based on the interleaver by Born2SPD
#///// INTERLEAVE DATA ///////////////
    if script_action == "1":
   #Grab data for the interleaved GFX file
        for i in range (0, num_of_gfx_roms, 4):
            with open (os.path.join(gamepath, filename[i]), "rb") as gfx_file[i]:
                with open (os.path.join(gamepath, filename[i+1]), "rb") as gfx_file[i+1]: 
                    with open (os.path.join(gamepath, filename[i+2]), "rb") as gfx_file[i+2]:
                        with open (os.path.join(gamepath, filename[i+3]), "rb") as gfx_file[i+3]: 
                            print("Interleaving", filename[i], filename[i+1],filename[i+2],filename[i+3])
                            grab_ROM_Data(i)

        with open (os.path.join(gfxpath, inter_name), "wb") as Interleaved_GFX: 
#            CPS2_Interleave_1048576()
            print("----------------TABLE3----------------")
            for i in range (0,len(tempfile3),1):
                print(len(tempfile3[i]))
            print("----------------TABLE2----------------")
            for i in range (0,len(tempfile2),1):
                print(len(tempfile2[i]))
            print("----------------TABLE1----------------")
            for i in range (0,len(tempfile),1):
                print(len(tempfile[i]))
            print("----------------OUTPUT----------------")
            for i in range (0,len(gfx_table),1):
                print(len(gfx_table[i]))
            Interleaved_GFX.write(bytes(gfx_table[0]))
#            Interleaved_GFX.write[tempfile3[0]]

    #///// DE-INTERLEAVE DATA ////////////
    if script_action == "2":
    #Grab data from the interleaved GFX file
        for i in range (0, num_of_gfx_roms, 4):
            with open (os.path.join(gfxpath, inter_name), "rb") as Interleaved_GFX:   
        #      for i in range (0, num_of_gfx_roms, 2):
        #         cps2_de_interleave1()
                print("De-Interleaving", filename[i], filename[i+1],filename[i+2],filename[i+3])
                #Grab the groups again
                if i >> 1 == 0:
                    for k in range(0, len(tempfile3), 1):
                        tempfile3[k] += Interleaved_GFX.read((res_file.gfx_romsize[k]) << 2)

                cps2_de_interleave1(Interleaved_GFX,i)


        print("----------------TABLE3----------------")
        for i in range (0,len(tempfile3),1):
            print(len(tempfile3[i]))
        print("----------------TABLE2----------------")
        for i in range (0,len(tempfile2),1):
            print(len(tempfile2[i]))
        print("----------------TABLE1----------------")
        for i in range (0,len(tempfile),1):
            print(len(tempfile[i]))
        print("----------------OUTPUT----------------")
        for i in range (0,len(gfx_table),1):
            print(len(gfx_table[i]))
        write_m_files()

def write_m_files():
    #Write the final .M data
    for i in range (0, num_of_gfx_roms, 4):
        with open (os.path.join(gamepath, filename[i]), "wb") as gfx_file[i]:
            with open (os.path.join(gamepath, filename[i+1]), "wb") as gfx_file[i+1]: 
                with open (os.path.join(gamepath, filename[i+2]), "wb") as gfx_file[i+2]:
                    with open (os.path.join(gamepath, filename[i+3]), "wb") as gfx_file[i+3]: 
                        gfx_file[i].write(bytes(gfx_table[i]))
                        gfx_file[i+1].write(bytes(gfx_table[i+1]))
                        gfx_file[i+2].write(bytes(gfx_table[i+2]))
                        gfx_file[i+3].write(bytes(gfx_table[i+3]))
#                            print("WIP")
                            #print("De-Interleaving", filename[i], filename[i+1],filename[i+2],filename[i+3])

#//////////////////// END OF CASE CPS2 ////////////////////

#//////////////////// DECIDE WHAT TO DO WITH DATA ////////////////////
if res_file.System == "Neo-Geo":
    CASE_NEO_GEO()

if res_file.System == "CPS2":
    #Generate required tables to store data
    tempfile = {}
    for i in range (0, num_of_gfx_roms, 1):
        tempfile.update({i : []})
    tempfile2 = {}
    for i in range (0, num_of_gfx_roms >> 1, 1):
        tempfile2.update({i : []})
    tempfile3 = {}
    for i in range (0, num_of_gfx_roms>>2, 1):
        tempfile3.update({i : []})
    CASE_CPS2()

if res_file.System == "CPS1":
    #Generate required tables to store data
    tempfile = {}
    for i in range (0, num_of_gfx_roms, 1):
        tempfile.update({i : []})
    tempfile2 = {}
    for i in range (0, num_of_gfx_roms >> 1, 1):
        tempfile2.update({i : []})
    tempfile3 = {}
    for i in range (0, num_of_gfx_roms>>2, 1):
        tempfile3.update({i : []})
    CASE_CPS2()    