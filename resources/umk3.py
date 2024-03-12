#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "midwunit"

#Generate tables for storing data using a dict
prg_prefix = {}
pref = "l1_mortal_kombat_3_u1"
pref2 = "_game_rom.u1"
for i in range (0, 12, 1):
    val = 33 - i
    stringinp = str("{}{}{}{}".format(pref,val,pref2,val))
    prg_prefix.update({i : stringinp})
pref = "umk-u1"
pref2 = ".bin"
for i in range (0, 4, 1):
    val = 21 - i
    stringinp = str("{}{}{}".format(pref,val,pref2))
    prg_prefix.update({12+i : stringinp})

#Here we make an array to store every "group" of ROMs to interleave between
prg_groupsize = [4,4,4,4]
#How many Bytes to interleave between groups
prg_grabsize = [1,1,1,1]
#How big each group is
prg_romsize = [0x100000,0x100000,0x100000,0x100000]
    
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u133_game_rom.u133",  0x0000000, 0x100000, CRC(79b94667) SHA1(31bba640c351fdccc6685cadb74dd79a3f910ce8) ) /* all GAME ROMs here are also known to be labeled as P1.0 */
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u132_game_rom.u132",  0x0000001, 0x100000, CRC(13e95228) SHA1(405b05f5a5a55667c2be17d4b399129bdacefd90) )
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u131_game_rom.u131",  0x0000002, 0x100000, CRC(41001e30) SHA1(2cec91116771951c0380cec5debf4cbb40c14c61) )
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u130_game_rom.u130",  0x0000003, 0x100000, CRC(49379dd7) SHA1(e6dfab4e23d9cc38ae56c1bbf10ccd160e8fad5e) )

#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u129_game_rom.u129",  0x0400000, 0x100000, CRC(a8b41803) SHA1(9697e35e8bb51d6d36b1d7ae47377b446e57682f) )
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u128_game_rom.u128",  0x0400001, 0x100000, CRC(b410d72f) SHA1(ac5c1c6f744186540f4ab100d9bd4ce6007e600b) )
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u127_game_rom.u127",  0x0400002, 0x100000, CRC(bd985be7) SHA1(f5183abea2e5eb2c2c8cefa72c9ed321679f5128) )
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u126_game_rom.u126",  0x0400003, 0x100000, CRC(e7c32cf4) SHA1(94ea7b2eed7dae66f5dd676c20d6b360140e3e0e) )

#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u125_game_rom.u125",  0x0800000, 0x100000, CRC(9a52227e) SHA1(0474a14fa8dbfea0b0889c1d1756b86391683558) )
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u124_game_rom.u124",  0x0800001, 0x100000, CRC(5c750ebc) SHA1(45d68af1a56994376e086d840502453c8d6be700) )
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u123_game_rom.u123",  0x0800002, 0x100000, CRC(f0ab88a8) SHA1(cdc9dc12e162255845c6627b1e35182b7e8502d0) )
#	ROM_LOAD32_BYTE( "l1_mortal_kombat_3_u122_game_rom.u122",  0x0800003, 0x100000, CRC(9b87cdac) SHA1(a5f8db559293978f23e6f105543d8b2e170a2e0d) )

#	ROM_LOAD32_BYTE( "umk-u121.bin",  0x0c00000, 0x100000, CRC(cc4b95db) SHA1(3d53180eec649e9616c4b87db55573f12d9bfee3) ) /* PCB pictures show EPROMs labeled as: */
#	ROM_LOAD32_BYTE( "umk-u120.bin",  0x0c00001, 0x100000, CRC(1c8144cd) SHA1(77cdc1eaf630ccb7233f5532f8b08191d00f0816) ) /* L2.0 MORTAL KOMBAT 3 Uxxx ULTIMATE   */
#	ROM_LOAD32_BYTE( "umk-u119.bin",  0x0c00002, 0x100000, CRC(5f10c543) SHA1(24dc83b7aa531ebd399258ffa7b2e028f1c4a28e) ) /* currently unverified if these are the same as for v1.0 & v1.1 UMK3 */
#	ROM_LOAD32_BYTE( "umk-u118.bin",  0x0c00003, 0x100000, CRC(de0c4488) SHA1(227cab34798c440b2a45223567113df5f17d913f) )
    
    