from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = ord('z') + i

try:
    bf = open('file1.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerr(e.errno))

try:
    binfile = open('file1.bin', 'rb')
    readData = bytearray(binfile.read(5))
    binfile.close()

    for d in readData:
        print(hex(d), end='  ')

except IOError as ioe:
    print("IOError occured", strerr(ioe.errno))
