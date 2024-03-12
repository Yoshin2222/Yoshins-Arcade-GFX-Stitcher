#Intended system this res file is needed for. This is used when reading
#appropriate GFX ROMs
System = "CPS2"
#Set up the names of the GFX Roms/interleaved filename
#Uses a table in the case of games with varying prefixes/compatability
gname1 = "smb"
gfx_prefix = [gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1,gname1]

#	ROM_LOAD64_WORD( "smb.13m",   0x0000000, 0x200000, CRC(d9b2d1de) SHA1(e8658983070dadcd1300a680a42c8431579e2b4f) )
#	ROM_LOAD64_WORD( "smb.15m",   0x0000002, 0x200000, CRC(9a766d92) SHA1(afdf88afbec527268d63c11ea32f861b52e11489) )
#	ROM_LOAD64_WORD( "smb.17m",   0x0000004, 0x200000, CRC(51800f0f) SHA1(9526cd69a23340a81841271b51de03d9bf2b979f) )
#	ROM_LOAD64_WORD( "smb.19m",   0x0000006, 0x200000, CRC(35757e96) SHA1(c915f3b9e4fdec3defc7eecb2c1f7377e6072228) )

#	ROM_LOAD64_WORD( "smb.14m",   0x0800000, 0x200000, CRC(e5bfd0e7) SHA1(327e626df4c2152f921f15535c01dda6c4437527) )
#	ROM_LOAD64_WORD( "smb.16m",   0x0800002, 0x200000, CRC(c56c0866) SHA1(1e2218e852ae72a9a95861dd37129fe78d4b1329) )
#	ROM_LOAD64_WORD( "smb.18m",   0x0800004, 0x200000, CRC(4ded3910) SHA1(d883541ce4d83f4e7ab095f2ef273408d9911f9a) )
#	ROM_LOAD64_WORD( "smb.20m",   0x0800006, 0x200000, CRC(26ea1ec5) SHA1(22be249b1f73272feacf4026f09fc877f5d86353) )

#	ROM_LOAD64_WORD( "smb.21m",   0x1000000, 0x080000, CRC(0a08c5fc) SHA1(ff3fad4fbc98e3013291c7ba7ee5e057a2628b36) )
#	ROM_LOAD64_WORD( "smb.23m",   0x1000002, 0x080000, CRC(0911b6c4) SHA1(e7a7061b192658724d98cae8693f63dd5bc40c00) )
#	ROM_LOAD64_WORD( "smb.25m",   0x1000004, 0x080000, CRC(82d6c4ec) SHA1(ed8ed02a00f59a048b9891ec2a77720bb6a5e03d) )
#	ROM_LOAD64_WORD( "smb.27m",   0x1000006, 0x080000, CRC(9b48678b) SHA1(4fa300d356c538947983ae85bb5c5cfd1fb835e7) )

#Total size of an individual rom
#The CPS2 Interleaves 4 files at a time, so 1 per group
gfx_romsize = [0x200000,0x200000,0x080000]
#Dictates the order in which files are read and written to
file_writes = [13,15,17,19,14,16,18,20,21,23,25,27]