import os

filepath = "F:\\Python\\FilesusingAuto\\testfiles\\"
totalsize = 0
for filename in os.listdir(filepath):
    # print(filename)
    if not os.path.isfile(os.path.join(filepath, filename)):
        continue

    totalsize += os.path.getsize(os.path.join(filepath, filename))

print(f'Total filesize is: {totalsize} kB')
