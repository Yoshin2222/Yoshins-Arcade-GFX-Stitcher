#Used to navigate file directories
from distutils.command.build_scripts import first_line_re
import os
import importlib
import sys
import time
import math 

#DANGEROUTS TO MUCK WITH STUFF UNDER THIS LINE, BE WARNED
var_prefix = "GFX_C"
inter_data = bytes()
#Generate folders if they don't already exist
rompath = r'roms'
if not os.path.exists(rompath):
    os.makedirs(rompath)
gfxpath = r'interleaved_data'
if not os.path.exists(gfxpath):
    os.makedirs(gfxpath)
respath = r'resources'
if not os.path.exists(respath):
    os.makedirs(respath)

gfx_ok = 0
prg_ok = 0


print("---------- YOSHINS ARCADE DATA STITCHER ----------")
game_name = input("Enter ROM name here: ")
#Invalid Input: No Resource file
while not os.path.exists(os.path.join(respath, game_name+".py")):
    print("GAME NOT SUPPORTED! Look in resources")
    game_name = input("Try something else: ")    

#Valid input
print("ROM_Name = ", str(game_name).lower())

#Invalid Input: No ROM Folder
while not os.path.exists(os.path.join(rompath, game_name)):
    print("Oy, there's no ROM folder!")
    os.makedirs(os.path.join(rompath, game_name))
    print("Lemme just fix that!")
#    game_name = input("Try something else: ")    

#Grab the needed resource file
sys.path.append(respath)
res_file = importlib.import_module(game_name.lower()) #Ensure lowercase for ease of input

#PRINT GFX STATUS
try:
    res_file.gfx_prefix
except:
    print("GFX: = NO")
else:
    gfx_ok = 1
    num_of_gfx_roms = len(res_file.gfx_prefix)
    inter_name = str(game_name).upper() + "_INTERLEAVED_GFX"
    print("GFX: = OK")

    gfx_file = ["{}{}" .format(var_prefix, i) for i in range(1, num_of_gfx_roms + 1)]
#Generate tables for storing data using a dict
    gfx_table = {}
    for i in range (0, num_of_gfx_roms, 1):
        gfx_table.update({i : []})
    #NEO-GEO
    if res_file.System == "Neo-Geo":

    #Fuck you Samsho 1
        try:
            res_file.prefix_override
        except: #Most games will return negative, only do prefix override stuff if the var exists
            filename = ["{}-c{}.c{}".format(res_file.gfx_prefix[i].lower(), i + 1,i + 1) for i in range(0, num_of_gfx_roms)]
    #In the case of games like Samsho 1, you need to be additionally explicit in order to handle the weird c51/c61 prefixes
        else:
            filename = ["{}-c{}.c{}".format(res_file.gfx_prefix[i].lower(), res_file.prefix_override[i], i + 1) for i in range(0, num_of_gfx_roms)]        

    #CPS2
    if res_file.System == "CPS2":
        filename = ["{}.{}m".format(res_file.gfx_prefix[i], res_file.file_writes[i],res_file.file_writes[i]) for i in range(0, num_of_gfx_roms)]
    #CPS1
    if res_file.System == "CPS1" :
        filename = ["{}".format(res_file.gfx_prefix[i]) for i in range(0, num_of_gfx_roms)]
    print("GRAPHICS DATA")
#    print(filename)

    #Validate ROMS
    print("----Graphics ROMS----")
    for i in range(0, len(res_file.gfx_prefix), 1):
        if os.path.exists(os.path.join(rompath, game_name, filename[i])):
            print(filename[i], " - OK")
        else:
            print(filename[i], " - DOES NOT EXIST")
    if os.path.exists((os.path.join(gfxpath, inter_name))):
        print("Interleaved GFX - EXISTS")
    else:
        print("Interleaved GFX - DOES NOT EXIST")

#PRINT PRG STATUS
try:
    len(res_file.prg_import)
except:
    inter_prg_name = str(game_name).upper() + "_INTERLEAVED_PRG"
else:
    prg_ok = 1
    print("IMPORT PRG: = OK")
    #Validate ROMS
    print("----Import Program ROMS----")
    for i in range(0, len(res_file.prg_import), 2):
        if os.path.exists(os.path.join(rompath, game_name, res_file.prg_import[i])):
            print(res_file.prg_import[i], " - OK")
        else:
            print(res_file.prg_import[i], " - DOES NOT EXIST")
    ####Print status of 
    try:
        res_file.import_swapendian
    except:
        print("Import Endian - Default")
    else:
        print("Import Endian - Swapped")

try:
    res_file.prg_prefix
except:
    inter_prg_name = str(game_name).upper() + "_INTERLEAVED_PRG"
else:
    prg_ok = 1
    inter_prg_name = str(game_name).upper() + "_INTERLEAVED_PRG"
    print("INTERLEAVE PRG: = OK")
    #Validate ROMS
    print("----De-Interleaved Program ROMS----")
    for i in range(0, len(res_file.prg_prefix), 1):
        if os.path.exists(os.path.join(rompath, game_name, res_file.prg_prefix[i])):
            print(res_file.prg_prefix[i], " - OK")
        else:
            print(res_file.prg_prefix[i], " - DOES NOT EXIST")
        ####Print status of 
    try:
        res_file.swapendian
    except:
        print("Interleave Endian - Default")
    else:
        print("Interleave Endian - Swapped")

try:
    len(res_file.prg_append)
except:
    inter_prg_name = str(game_name).upper() + "_INTERLEAVED_PRG"
else:
    prg_ok = 1
    print("APPEND PRG: = OK")
    #Validate ROMS
    print("----Append Program ROMS----")
    for i in range(0, len(res_file.prg_append), 2):
        if os.path.exists(os.path.join(rompath, game_name, res_file.prg_append[i])):
            print(res_file.prg_append[i], " - OK")
        else:
            print(res_file.prg_append[i], " - DOES NOT EXIST")
    ####Print status of 
    try:
        res_file.append_swapendian
    except:
        print("Append Endian - Default")
    else:
        print("Append Endian - Swapped")

if os.path.exists(os.path.join(gfxpath, inter_prg_name)):
    print(inter_prg_name, " - EXISTS")
else:
    print(inter_prg_name, " - DOES NOT EXIST")


#Make a folder for the game ROM is there isn't one already
gamepath = os.path.join(rompath, game_name)
if not os.path.exists(gamepath):
    os.makedirs(gamepath)

script_action = input("Great, now what? 1:Interleave 2: De-Interleave: ")

#Invalid Input
while script_action != "1" and script_action != "2":
    print("Why'd ya do that? Now ya just look silly")
    script_action = input("Try something else: ")  
if gfx_ok == 1:
    print(inter_name)
#Assign appropriate names/vars to be used later

#Valid Input 1
if script_action == "1":
    print("Interleaving, please wait...")
#Valid Input 2
if script_action == "2":
    print("De-Interleaving, please wait...")

#Allocate Filenames if PRG is prepped for interleaving
if prg_ok == 1:
    try:
        res_file.prg_prefix
    except:
        print("No interleave data")
    else:
        prg_filename = ["{}".format(res_file.prg_prefix[i]) for i in range(0, len(res_file.prg_prefix))]
        print("DE-INTERLEAVED PROGRAM DATA")
        print(prg_filename)



#Allocate Filenames if GFX is prepped for interleaving
#if gfx_ok == 1:


#Display some info, mostly aesthetic if i'm honest
print("System =", res_file.System)
#print(filename)

def Interleave_PRG():
#Go through every file based on it's group
    prg_table = []
    out_table = []
 #Append remainder of data if need be
    try:
        res_file.prg_import
    except:
        print("No initial data to import")
    else:
        print("Now importing data...")
        #Define the beginning of previous data to append the new data
        import_data = {}
        import_flipped_data = {}
        for x in range(0, len(res_file.prg_import), 2):
            import_data.update({x>>1 : []})
            print("Import X - ", x)
            print("Import Name - ", res_file.prg_import[x])
            print("Import Size - ", res_file.prg_import[x+1])
            with open((os.path.join(gamepath, res_file.prg_import[x])), "rb") as PRG1:
                import_data[x>>1] = PRG1.read(res_file.prg_import[x+1])
#####CHECK IF THE ENDIAN OF THE DATA SHOULD BE SWAPPED#####        
                try:
                    res_file.import_swapendian
                except:
                    print("writing appended data...")
                    out_table += import_data[x>>1]
                else: #Swap the Endian of the data before it's written
                    import_flipped_data.update({x>>1 : []})
                    for v in range(res_file.import_swapendian, (res_file.prg_import[x+1]) + res_file.import_swapendian, res_file.import_swapendian):
                        for b in range(-1, -res_file.import_swapendian-1, -1):
                            import_flipped_data[x>>1] += import_data[x>>1][v + b:  v + b + 1]
                    print("writing flipped appended data...")
                    out_table += import_flipped_data[x>>1]
 
    try:
        res_file.prg_prefix #Check if interleacving should be goin on
    except:
        print("-----")
    else:
        b = 0
        k = 0
        print("---Interleaving PRG---")
        for i in range(0,len(prg_filename), res_file.prg_groupsize[k]):
            if res_file.prg_groupsize[b] == 2:
                print("Group ", b+1)
                print("Interleaving - ", prg_filename[k], prg_filename[k+1])
    #            print(prg_filename[k+1])
                with open((os.path.join(gamepath, prg_filename[k])), "rb") as PRG1:
                    with open((os.path.join(gamepath, prg_filename[k+1])), "rb") as PRG2:
                            for j in range(0, res_file.prg_romsize[b], res_file.prg_grabsize[b]):
                                prg_table += PRG1.read(res_file.prg_grabsize[b])
                                prg_table += PRG2.read(res_file.prg_grabsize[b])
            if res_file.prg_groupsize[b] == 4:
                print("Group ", b+1)
                print("Interleaving - ", prg_filename[k], prg_filename[k+1], prg_filename[k+2], prg_filename[k+3])
                with open((os.path.join(gamepath, prg_filename[k])), "rb") as PRG1:
                    with open((os.path.join(gamepath, prg_filename[k+1])), "rb") as PRG2:
                        with open((os.path.join(gamepath, prg_filename[k+2])), "rb") as PRG3:
                            with open((os.path.join(gamepath, prg_filename[k+3])), "rb") as PRG4:
                                for j in range(0, res_file.prg_romsize[b], res_file.prg_grabsize[b]):
                                    prg_table += PRG1.read(res_file.prg_grabsize[b])
                                    prg_table += PRG2.read(res_file.prg_grabsize[b])
                                    prg_table += PRG3.read(res_file.prg_grabsize[b])
                                    prg_table += PRG4.read(res_file.prg_grabsize[b])
            k += res_file.prg_groupsize[b]
            b += 1
    #####CHECK IF THE ENDIAN OF THE DATA SHOULD BE SWAPPED#####        
        try:
            res_file.swapendian
        except:
            with open((os.path.join(gfxpath, inter_prg_name)), "wb") as Output:
                Output.write(bytes(prg_table))
                out_table += prg_table
        else: #Swap the Endian of the data before it's written
            print("Now swapping the Endian...")
            flipped_table = []
            for i in range(res_file.swapendian, sum(res_file.prg_romsize) * len(prg_filename) + res_file.swapendian, res_file.swapendian):
                for k in range(-1, -res_file.swapendian-1, -1):
                    flipped_table += prg_table[i + k:  i + k + 1]
    #Write the altered data
            out_table += flipped_table
#            with open((os.path.join(gfxpath, inter_prg_name)), "wb") as Output:
    #            print(sum(res_file.prg_romsize))
#                print(len(flipped_table))
#                Output.write(bytes(flipped_table))

#Append remainder of data if need be
    try:
        res_file.prg_append
    except:
        print("Finished reading PRG ROMs")
    else:
        print("Now appending data...")
        #Define the beginning of previous data to append the new data
#        try:
#            res_file.swapendian
#        except:
#            append_start = sum(res_file.prg_romsize) * len(prg_filename)
#        append_start = sum(res_file.prg_romsize) * len(prg_filename)
        append_data = {}
        append_flipped_data = {}
#        if not os.path.exists(((os.path.join(gfxpath, inter_prg_name)))):
#            with open((os.path.join(gfxpath, inter_prg_name)), "wb") as Output:
#                Output.write()
        for x in range(0, len(res_file.prg_append), 2):
            append_data.update({x>>1 : []})
            print("Append X - ", x)
            print("Append Name - ", res_file.prg_append[x])
            print("Append Size - ", res_file.prg_append[x+1])
            with open((os.path.join(gamepath, res_file.prg_append[x])), "rb") as PRG1:
                append_data[x>>1] = PRG1.read(res_file.prg_append[x+1])
#####CHECK IF THE ENDIAN OF THE DATA SHOULD BE SWAPPED#####        
                try:
                    res_file.append_swapendian
                except:
                    print("writing appended data...")
                    out_table += append_data[x>>1]
                else: #Swap the Endian of the data before it's written
                    append_flipped_data.update({x>>1 : []})
                    for v in range(res_file.append_swapendian, (res_file.prg_append[x+1]) + res_file.append_swapendian, res_file.append_swapendian):
                        for b in range(-1, -res_file.append_swapendian-1, -1):
                            append_flipped_data[x>>1] += append_data[x>>1][v + b:  v + b + 1]
                    print("writing flipped appended data...")
                    out_table += append_flipped_data[x>>1]

###WRITE THE FINAL INTERLEAVED DATA
    with open((os.path.join(gfxpath, inter_prg_name)), "wb") as Output:
        Output.write(bytes(out_table))


def De_Interleave_PRG():
####IMPORT DATA FOR LATER
    h = 0
    try:
        res_file.prg_import
    except:
        pass
    else:
        import_prg_table = {}
        with open((os.path.join(gfxpath, inter_prg_name)), "rb") as Input:
#Offset when the data begins reading if there's interleaved data beforehand
            for h in range(0, len(res_file.prg_import), 2):
                import_prg_table.update({h>>1 : []})
                import_prg_table[h>>1] += Input.read(res_file.prg_import[h+1])
####CHECK TO SEE IF WE SHOULD CHANGE THE ENDIAN OF THE DATA
        try:
            res_file.import_swapendian
        except:
            for h in range(0, len(res_file.prg_append), 2):
                with open((os.path.join(gamepath, res_file.prg_import[h])), "wb") as Appendfile:
                    Appendfile.write(bytes(append_prg_table[h>>1]))
        else: #Swap the Endian of the data before it's written
            import_flipped_table = {}
            for r in range(0, len(res_file.prg_import), 2):
                import_flipped_table.update({r>>1 : []})
                for q in range(res_file.import_swapendian, res_file.prg_import[r+1] + res_file.import_swapendian, res_file.import_swapendian):
                    for k in range(-1, -res_file.import_swapendian-1, -1):
                        import_flipped_table[r>>1] += import_prg_table[r>>1][q + k:  q + k + 1]
#Write the flipped data back
            for h in range(0, len(res_file.prg_import), 2):
                with open((os.path.join(gamepath, res_file.prg_import[h])), "wb") as Appendfile:
                    Appendfile.write(bytes(import_flipped_table[h>>1]))

#Go through every file based on it's group
    prg_table = {}
####GRAB INTERLEAVED DATA FOR LATER
    h = 0
    try:
        res_file.prg_prefix
    except:
        pass
    else:
        with open((os.path.join(gfxpath, inter_prg_name)), "rb") as Input:
            try:
                res_file.prg_import
            except:
                while h < len(res_file.prg_groupsize):
                    prg_table.update({h : []})
                    prg_table[h] += Input.read((res_file.prg_romsize[h]) * (res_file.prg_groupsize[h]))
                    h += 1
            else:
                for q in range(0, len(res_file.prg_import),2):
                    Input.read(res_file.prg_import[q+1])

                while h < len(res_file.prg_groupsize):
                    prg_table.update({h : []})
                    prg_table[h] += Input.read((res_file.prg_romsize[h]) * (res_file.prg_groupsize[h]))
                    h += 1


        out_table = {}

        for i in range (0, len(res_file.prg_prefix), 1):
            out_table.update({i : []})
        b = 0
        k = 0
        print("---De-Interleaving PRG---")
        for i in range(0,len(prg_filename), res_file.prg_groupsize[k]):
            with open((os.path.join(gfxpath, inter_prg_name)), "rb") as Input:
                if res_file.prg_groupsize[b] == 2:
                    print("Group ", b+1)
                    print("De-Interleaving - ", prg_filename[k], prg_filename[k+1])
                    for j in range(0, res_file.prg_romsize[b] << 1, res_file.prg_grabsize[b] << 1):
                        out_table[k] += prg_table[b][j : j + res_file.prg_grabsize[b]]
                        out_table[k+1] += prg_table[b][j + res_file.prg_grabsize[b] : j + (res_file.prg_grabsize[b] * 2)]

                if res_file.prg_groupsize[b] == 4:
                    print("Group ", b+1)
                    print("De-Interleaving - ", prg_filename[k], prg_filename[k+1], prg_filename[k+2], prg_filename[k+3])
                    for j in range(0, res_file.prg_romsize[b] << 2, res_file.prg_grabsize[b] << 2):
                        out_table[k] += prg_table[b][j : j + res_file.prg_grabsize[b]]
                        out_table[k+1] += prg_table[b][j + res_file.prg_grabsize[b] : j + (res_file.prg_grabsize[b] * 2)]
                        out_table[k+2] += prg_table[b][j + (res_file.prg_grabsize[b] * 2) : j + (res_file.prg_grabsize[b] * 3)]
                        out_table[k+3] += prg_table[b][j + (res_file.prg_grabsize[b] * 3) : j + (res_file.prg_grabsize[b] * 4)]

                k += res_file.prg_groupsize[b]
                b += 1
        try:
            res_file.swapendian
        except:
    #Write the PRG Data back
            for l in range(0,len(prg_filename), 1):
                with open((os.path.join(gamepath, prg_filename[l])), "wb") as output:
                    output.write(bytes(out_table[l]))
        #            print(l)
        #            output.write(bytes(0))
        else: #Swap the Endian of the data before it's written
            print("Now swapping the Endian...")
    #Generate tables to push the data back in to, flipped back to it's original state
            flipped_table = {}
            for i in range(0, len(prg_filename), 1):
                flipped_table.update({i : []})
            for m in range(0, len(prg_filename), 1):
                for i in range(res_file.swapendian, sum(res_file.prg_romsize) + res_file.swapendian, res_file.swapendian):
                    for k in range(-1, -res_file.swapendian-1, -1):
                        flipped_table[m] += out_table[m][i + k:  i + k + 1]
    #Write the PRG Data back
            for l in range(0,len(prg_filename), 1):
                with open((os.path.join(gamepath, prg_filename[l])), "wb") as output:
                    output.write(bytes(flipped_table[l]))
                    print(len(flipped_table[l]))


####GRAB APPENDED DATA FOR LATER
    h = 0
    try:
        res_file.prg_append
    except:
        pass
    else:
        append_prg_table = {}
        with open((os.path.join(gfxpath, inter_prg_name)), "rb") as Input:
            ###Just to be safe, read data until the start of appended data
            try:
                res_file.prg_prefix
            except:
                for h in range(0, len(res_file.prg_append), 2):
                    append_prg_table.update({h>>1 : []})
                    append_prg_table[h>>1] += Input.read(res_file.prg_append[h+1])
            else:
#Offset when the data begins reading if there's interleaved data beforehand
                for s in range(0, len(res_file.prg_groupsize), 1):
                    Input.read((res_file.prg_romsize[s]) * (res_file.prg_groupsize[s]))
            try:
                res_file.prg_import
            except:
                for h in range(0, len(res_file.prg_append), 2):
                    append_prg_table.update({h>>1 : []})
                    append_prg_table[h>>1] += Input.read(res_file.prg_append[h+1])
            else:
#Offset when the data begins reading if there's interleaved data beforehand
                for q in range(0, len(res_file.prg_import),2):
                    Input.read(res_file.prg_import[q+1])

                for h in range(0, len(res_file.prg_append), 2):
                    append_prg_table.update({h>>1 : []})
                    append_prg_table[h>>1] += Input.read(res_file.prg_append[h+1])
#                h += 1
####CHECK TO SEE IF WE SHOULD CHANGE THE ENDIAN OF THE DATA
        try:
            res_file.append_swapendian
        except:
            for h in range(0, len(res_file.prg_append), 2):
                with open((os.path.join(gamepath, res_file.prg_append[h])), "wb") as Appendfile:
                    Appendfile.write(bytes(append_prg_table[h>>1]))
        else: #Swap the Endian of the data before it's written
            append_flipped_table = {}
            for r in range(0, len(res_file.prg_append), 2):
                append_flipped_table.update({r>>1 : []})
                for q in range(res_file.append_swapendian, res_file.prg_append[r+1] + res_file.append_swapendian, res_file.append_swapendian):
                    for k in range(-1, -res_file.append_swapendian-1, -1):
                        append_flipped_table[r>>1] += append_prg_table[r>>1][q + k:  q + k + 1]
#Write the flipped data back
            for h in range(0, len(res_file.prg_append), 2):
                with open((os.path.join(gamepath, res_file.prg_append[h])), "wb") as Appendfile:
                    Appendfile.write(bytes(append_flipped_table[h>>1]))


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
    l = 64
    mode = 0
    if mode == 0:
        order = [0,0,1,1]
    else:
        order = [0,1,0,1]
    #ssf2t
        
    while j < (res_file.gfx_romsize[i>>2]) << 1:
#Interleave every 64 Bytes between groups
        #The first table stores the EVEN WORDs of the 
        #group
        #Grab 64 bytes from the 13/15 EVEN WORDs table
        tempfile2[(i >> 1) + order[0]] += tempfile[i][j:j+l]
        #Grab 64 bytes from the 17/19 EVEN WORDs table
        tempfile2[(i >> 1) + order[1]] += tempfile[i+2][j:j+l]
        #The second table stores the ODD WORDs of the 
        #group
        #Grab 64 bytes from the 13/15 ODD WORDs table
        tempfile2[(i >> 1) + order[2]] += tempfile[i+1][j:j+l]
        #Grab 64 bytes from the 17/19 ODD WORDs table
        tempfile2[(i >> 1) + order[3]] += tempfile[i+3][j:j+l]
        j += l
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

############ #32x32 TILE TEST ##################
#        My guess is essentially instead of the tiles being organised like
#        1234
#        5678
#        It's more like
#        1256
#        3478
    TEST = 1

    if TEST != 0:
        # The output should resemble MAMEs default display, where each 32x32 tile
        # is composed of 16x16 tiles in this ROM order
        #  - 12
        #  - 34
        # 16 32x32 tiles across.

        # Normally when assembled, data is simply read from left to right, top to bottom.
        # But in order to get 32x32 tiles to display correctly, we need to understand a few things
        # In TM, Tiles are displayed in 8x8 chunks, and since we're messing with the CPS2, GFX 
        # are stored as 4bits per pixel. 8 Pixels across, that's 4 Bytes per line. 8 lines down, 
        # 4*8 gives us 32, 0x20 bytes in total per tile. In 1D mode, data is simply read from left to right, 
        # what is displayed being built up 1 8x8 tile at a time. This is how you can change the canvas size 
        # and tiles to the upper left will stay still. In the ROM, this is reflected as a linear string of 
        # 0x20 bytes. This is important to note as it seems 32x32 tiles are stored in a slightly different format,
        # more reflective of 2D Mode. Instead of defaulting to 1 8x8 chunk, 2D Mode allows you to manually
        # assert how big chunks are. For our purposes, 16x16, or 2 chunks. It's at this point things get funky.
        # Now instead of Bytes being linear, they adhere to the dimensions of the chunks we've defined.
        # A string of 0xFF bytes 0x20 long would normally show a solid tile, but in this 2D mode, it instead
        # displays 2 tiles seemingly cut in half. You can visually see this in a Hex Editor such as HxD. It's
        # important to note that chunks only ever increase in size horizontally,  
        # 1
        # 2
        # 3
        # 4
        # And this after the process
        # 1 3
        # 2 4
        # For reference, this is how TM uses data in 2D Mode
        # The first 4 bytes are responsible for the first line of the tile. Since we're messing with the
        # CPS2, it's GFX are 4bpp, or 4 Bits Per-pixel. These Bits are split across the 4 Bytes, and are
        # essentially stitched together when the data is read. For instance, a value of 0x80808080
        # would equate to 10000000100000001000000010000000
        #10000000
        #10000000
        #10000000
        #10000000
        # By stitching the upper Bits together, we get 1111, the value 15, so we use that color for this
        # pixel.
        # The process is repeated for the rest of the bits to get the rest of the line. Once this is done,
        # we skip forward to 
        # By default, when viewing tiles in TM in 2D Mode-2 column rows, the first tile is 0x0 to 0x04
        # across, 0x0 to 0x40 down, totalling 16 bytes. The tile 

        width = 16
        tile_data = {}
        buffer = {}
        for b in range (0,4,1):
            tile_data.update({b : []})
        for b in range (0,4,1):
            buffer.update({b : []})
        test2 = 1
        #Read through the whole file, grabbing the needed Bytes in 4x8 strips
        if test2 == 0:
            for offset in range(0, len(tempfile3[i>>2]),0x40):
                for tile in range(0,4,1):
                    # Read 4 Y Strips of Bytes
                    for y in range(0,4,1):
                    # 4 Bytes across
                        # TILE = 0
                        # (0) + offset + x + (32
                        for x in range(0,4,1):
                            adr = (tile<<2) + offset + x + (y<<4)
                            tile_data[tile] += tempfile3[(i>>2)][adr:adr+1]
            #interleave the tiles 4 Bytes apiece to convert it to 1D data
            for offset in range(0, len(tempfile3[i>>2]),0x40):
                for dat in range(0,2,1):
                    for y in range(0,8,1):
                    # 4 Bytes across
                        # TILE = 0
                        # (0) + offset + x + (32
                        for x in range(0,2,1):
                            adr = (dat<<2) + offset + (x<<2) + (y<<4)
                            buffer[(dat<<1)+0] += tile_data[(i>>2)][adr:adr+4]            
                            buffer[(dat<<1)+1] += tile_data[(i>>2)][adr:adr+4]            

    #        for offset in range(0, len(tempfile3[i>>2]),0x40):
    #            for index in range(0,4,1):
    #                gfx_table[0] += tile_data[tile]#[offset:offset+1]
            add = 0x20
            add2 = add<<1
            for index in range(0,4,1):
                for offset in range(0, len(tempfile3[i>>2]),add2):
                    gfx_table[0] += tile_data[index][offset:offset+add]
    #                gfx_table[0] += tile_data[(index<<1)+1][offset:offset+add]
        else:
            add2 = 0x40
        #Take every 8x8 tile and reogrganize them
            for offset in range(0, len(tempfile3[i>>2]), add2<<1):
            #Create 2 tables, 1 for every EVEN and ODD pars of the 16x16 tiles
                start2 = offset + add2
                tile_data[0] += tempfile3[i>>2][offset:offset+add2]
                tile_data[1] += tempfile3[i>>2][start2:start2+add2]
            #Add the tables together
#            add = 0x80
#            for b in range(0, len(tempfile3[i>>2]), add):
#                for c in range(0,2,1):
#                    gfx_table[0] += tile_data[c][b:b+add]
            #test thing
#            tempfile3[i>>2] = convert_GFX_2Dto1D(tempfile3[i>>2], 4, 16, 16, len(tempfile3[i>>2]))
#            gfx_table[0] += convert_GFX_2Dto1D(tempfile3[i>>2], 4, 8, 8, len(tempfile3[i>>2]))
            gfx_table[0] += tempfile3[i>>2]
            #Interleave tiles
#            add3 = 0x80
#            for offset in range(0, len(tempfile3[i>>2]), add3<<1):
#                start2 = offset + add3
#                gfx_table[0] += tempfile3[i>>2][offset:offset+add3]
#                gfx_table[0] += tempfile3[i>>2][start2:start2+add3]


           # gfx_table[0] += tempfile3[i>>2]
    else:
#Append the groups final data to the output
        gfx_table[0] += tempfile3[i>>2]


def convert_GFX_2Dto1D(table, bpp, blockwidth, blockheight, length):
    tempbuf = []
    #READ A BLOCK OF DATA AS IF IT WERE 2D TILES
    x_read = math.floor((blockwidth/bpp))<<1
    buf_x = x_read<<2
    y_read = blockheight*0x10

    #Get the Location in ROM to read/Define Chunk
    for y_ptr in range(0, length, y_read):
        for x_ptr in range(0, buf_x, x_read):
        #Read the Data at this chunk
            for y in range(0, y_read, math.floor(y_read/blockheight)):
                adr = x_ptr + y_ptr + y
                tempbuf += table[adr:adr+x_read]
    return tempbuf


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
### The process for the CPS1 is much and such the same as CPS2, only that due to the varied GFX sizes,
# we don't interleave every 2 << 19 chunk of data. Data is read from each Group, and any remaining data in essence
#"spills" over in to the next one
                        #CPS1 GFX INTERLEAVING STEPS
#    = Copy the files
#    = Go through every Group, making EVEN and ODD tables composed of 4 bytes per half of the group. For instance,
#   SF2 has ROM Groups of 4, each reading 2 bytes apiece. The first table would contain a WORD from each of the 
#   first 2 ROMs, then the next table would have the next 4 bytes.
#    = Interleave these EVEN and ODD tables together a tile apiece, 64 Bytes
#    = Finally, Append that interleaved group data to the output

def generate_split_table():
    split_tab = []
    index = 0
    for i in range(0, len(res_file.group_size), 1):
        temp = 0
        temp2 = 0
        for k in range (0, res_file.group_size[i], 1):
            add = res_file.rom_byte_size[res_file.group_indexes[index+k]-1]
            if temp2 >= 4:
                temp = 1
            else:
                 temp = 0
            split_tab.append(temp)
            temp2 += add
        index += res_file.group_size[i]
    print(split_tab)
    return split_tab

def generate_assemble_sizes():
    temp = 0
    output = []
    comp_table = []
    #First, make a copy of every GFX ROM
    for group in range(0, len(res_file.group_size), 1):
        output.append(0)
        k = 0
    #Gather temp Assemble sizes before comparison
        for index in range(0, res_file.group_size[group], 1):
            group_index = res_file.group_indexes[index+k]-1
            FILE_LOC = os.path.join(gamepath, filename[group_index])
            bytesize = res_file.rom_byte_size[group_index]
            assemble_size = math.floor(os.path.getsize(FILE_LOC)/bytesize)
            comp_table.append(assemble_size)
        k +=  res_file.group_size[group]

    #Compare each Assemble size for each group, specifically choosing the smallest number
    temp = comp_table[0]
    k = 0
    for group in range(0, len(res_file.group_size), 1):
        for index2 in range(0, res_file.group_size[group], 1):
            if comp_table[index2+k] < temp:
                temp = comp_table[index2]
        output[group] = temp
        k +=  res_file.group_size[group]
        print("ASSEMBLE_SZZE - ", hex(output[group])) #," - ", hex(bytesize))
    return output

def grab_CPS1_ROM_Data():
    print("Interleaving GFX...")
    time.sleep(1)
    finalsize = 0
    #First, make a copy of every GFX ROM
    for i in range(0, len(res_file.gfx_prefix), 1):
        FILE_LOC = os.path.join(gamepath, filename[i])
        file_length = os.path.getsize(FILE_LOC)
        with open (FILE_LOC, "rb") as inp:
            bytesize = res_file.rom_byte_size[i]
            print(FILE_LOC, " - SIZE = ", hex(file_length), " - ", hex(bytesize))
            gfx_file[i] = inp.read(file_length)
            finalsize += file_length
    print("\tTOTAL SIZE OF GFX ROMS - ", hex(finalsize))

def CPS1_Interleave_GFX_data():
    a = 0 #Keeps track of which Group Indexes to mess with
    increment = 0
    split_table = generate_split_table()
    assemble_sizes = generate_assemble_sizes()
    #For how many groups there are, grab Bytes from each file
    #and appropriately split them in to EVEN and ODD parts
    for group in range(0, len(res_file.group_size),1):
        print(group, " - assemble size  - ", hex(assemble_sizes[group]))
        for k in range(0, assemble_sizes[group], 1):
#        print(group, " - assemble size  - ", hex(res_file.assemble_sizes[group]))
#        for k in range(0, res_file.assemble_sizes[group], 1):
            for b in range(0, res_file.group_size[group],1):
                file_index = res_file.group_indexes[a+b]-1
                increment = res_file.rom_byte_size[file_index]
#                split = res_file.split_table[a+b]
                split = split_table[a+b]
                val = temp_counter[file_index]
                tempfile[(group<<1)+split] += gfx_file[file_index][val:val+increment]
                temp_counter[file_index] += increment

    #Add to a when done reading this group data
        a += res_file.group_size[group]

    #Once the Groups are properly split in to EVEN and ODD tables, Interleave
    #them one Tile at a time
    for i in range(0, len(res_file.group_size),1):
        j = 0
        while j < len(tempfile[i])<<1:
            tempfile2[i] += tempfile[(i<<1)][j:j+64]
            tempfile2[i] += tempfile[(i<<1)+1][j:j+64]
            j += 64

    with open (os.path.join(gfxpath, inter_name), "wb") as Interleaved_GFX: 
        print("----------------TABLE3----------------")
        for i in range (0,len(tempfile3),1):
            print(len(tempfile3[i]), " - ", hex(len(tempfile3[i])))
        print("----------------TABLE2----------------")
        for i in range (0,len(tempfile2),1):
            print(len(tempfile2[i]), " - ", hex(len(tempfile2[i])))
            gfx_table[0] += tempfile2[i]
        print("----------------TABLE1----------------")
        for i in range (0,len(tempfile),1):
            print(len(tempfile[i]), " - ", hex(len(tempfile[i])))
        print("----------------EVEN----------------")
        for i in range (0,len(even_tables),1):
            print(len(even_tables[i]), " - ", hex(len(even_tables[i])))
        print("----------------ODD----------------")
        for i in range (0,len(odd_tables),1):
            print(len(odd_tables[i]), " - ", hex(len(odd_tables[i])))
        print("----------------OUTPUT----------------")
        for i in range (0,len(gfx_table),1):
            print(len(gfx_table[i]), " - ", hex(len(gfx_table[i])))
        Interleaved_GFX.write(bytes(gfx_table[0]))

def cps1_de_interleave1():
    print("De-interleaving GFX...")
    #Grab the Interleaved Data
    int_gfx_name = os.path.join(gfxpath, inter_name)
    int_gfx_size = os.path.getsize(int_gfx_name)
    with open(int_gfx_name, "rb") as inp: 
        gfx_file[0] = inp.read(int_gfx_size)


    #Split the data back in to its individual ROM groups
    assemble_sizes = generate_assemble_sizes()
    offset = 0
    f_read = 0 #This is a caveman way of doing it but fuck it i'm tired lol
    for i in range(0, len(res_file.group_size),1):
        byte_read = assemble_sizes[i] << 3
        tempfile3[i] += gfx_file[0][offset:offset+byte_read]
        offset += byte_read
        f_read += 1

    #Split the ROM in to its EVEN and ODD groups again, tile by tile
    for i in range(0, len(res_file.group_size),1):
        j = 0
        while j < len(tempfile3[i]):
            tempfile2[(i<<1)]   += tempfile3[i][j:j+64]
            tempfile2[(i<<1)+1] += tempfile3[i][j+64:j+128]
            j += 128

    a = 0 #Keeps track of which Group Indexes to mess with
    increment = 0
    split_table = generate_split_table()
    #For how many groups there are, grab Bytes from each file
    #and appropriately split them in to EVEN and ODD parts
    for group in range(0, len(res_file.group_size),1):
        k = 0
#        print(group, " - assemble size  - ", hex(res_file.assemble_sizes[group]))
        print(group, " - assemble size  - ", hex(assemble_sizes[group]))
        while k < len(tempfile2[group<<1])<<1:
            for b in range(0, res_file.group_size[group],1):
                file_index = res_file.group_indexes[a+b]-1
                increment = res_file.rom_byte_size[file_index]
#                split = res_file.split_table[a+b]
                split = split_table[a+b]
                val = temp_counter[(group<<1)+split]

                tempfile[file_index] += tempfile2[(group<<1)+split][val:val+increment]
                temp_counter[(group<<1)+split] += increment
                k += 1

    #Add to a when done reading this group data
        a += res_file.group_size[group]

    print("----------------TABLE3----------------")
    for i in range (0,len(tempfile3),1):
        print(len(tempfile3[i]), " - ", hex(len(tempfile3[i])))
    print("----------------TABLE2----------------")
    for i in range (0,len(tempfile2),1):
        print(len(tempfile2[i]), " - ", hex(len(tempfile2[i])))
    print("----------------TABLE1----------------")
    for i in range (0,len(tempfile),1):
        print(len(tempfile[i]), " - ", hex(len(tempfile[i])))
    print("----------------EVEN----------------")
    for i in range (0,len(even_tables),1):
        print(len(even_tables[i]), " - ", hex(len(even_tables[i])))
    print("----------------ODD----------------")
    for i in range (0,len(odd_tables),1):
        print(len(odd_tables[i]), " - ", hex(len(odd_tables[i])))

    #Write the files back
    for i in range(0, num_of_gfx_roms, 1):
        FILE_LOC = os.path.join(gamepath, filename[i])
        with open(FILE_LOC,"wb") as out:
            out.write(bytes(tempfile[i]))
    time.sleep(1)

#//////////////////// START OF CASE CPS2 ////////////////////
def CASE_CPS1():

#///// INTERLEAVE DATA ///////////////
    if script_action == "1":
   #Grab data for the interleaved GFX file
        grab_CPS1_ROM_Data()
    #Next, assemble EVEN and ODD tables based on ROM layout
        CPS1_Interleave_GFX_data()

#///// DE-INTERLEAVE DATA ////////////
    if script_action == "2":
    #Grab data from the interleaved GFX file
        cps1_de_interleave1()


#        print("----------------TABLE3----------------")
#        for i in range (0,len(tempfile3),1):
#            print(len(tempfile3[i]))
#        print("----------------TABLE2----------------")
#        for i in range (0,len(tempfile2),1):
#            print(len(tempfile2[i]))
#        print("----------------TABLE1----------------")
#        for i in range (0,len(tempfile),1):
#            print(len(tempfile[i]))
#        print("----------------OUTPUT----------------")
#        for i in range (0,len(gfx_table),1):
#            print(len(gfx_table[i]))
#        write_m_files()

#//////////////////// END OF CASE CPS1 ////////////////////


#//////////////////// DECIDE WHAT TO DO WITH DATA ////////////////////
if gfx_ok == 1:
    if res_file.System == "Neo-Geo":
        CASE_NEO_GEO()

    if res_file.System == "CPS1" or res_file.System == "CPS2" :
    #Only Interleave GFX if there is GFX to interleave
        #Generate required tables to store data
            tempfile = {}
            even_tables = {}
            odd_tables = {}
            for i in range (0, num_of_gfx_roms, 1):
                tempfile.update({i : []})
                even_tables.update({i : []})
                odd_tables.update({i : []})
            tempfile2 = {}
            for i in range (0, num_of_gfx_roms >> 1, 1):
                tempfile2.update({i : []})
            tempfile3 = {}
            for i in range (0, num_of_gfx_roms>>2, 1):
                tempfile3.update({i : []})
            if res_file.System == "CPS2":
                CASE_CPS2()
            if res_file.System == "CPS1":
                temp_counter = {}
                for i in range (0, num_of_gfx_roms, 1):
                        temp_counter.update({i : 0})
                CASE_CPS1()

if prg_ok == 1:
    if script_action == "1":
        Interleave_PRG()
    if script_action == "2":
       De_Interleave_PRG()
