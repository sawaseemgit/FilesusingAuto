import os
import shutil
#WARNING: WHILE USING DELETE(UNLINK) COMMAND
#os.chdir('F:\Python\FilesusingAuto\\testfiles')#change to whtever working folder

for fname in os.listdir():
    if fname.endswith('.txt'):
        print(fname)# dry-run with print code before using del
        ###os.unlink(fname)
        ## shutil.rmtree(fname)