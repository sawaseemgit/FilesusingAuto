srcfile= input("enter name of source file")
try:
    src= open(srcfile, "rt")
except IOError as ioe:
    print("Error opening file:", strerr(ioe.errno))
    exit(ioe.errno)

buff=bytearray(1000)

try:
    readfile= src.readinto(buff)
    wdata= lower(readfile)
    alp=[]
    for c in range(len(readfile)):
        if c in alp:
            
