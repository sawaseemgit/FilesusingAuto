# afile = open('transtest.txt', 'a')
# afile.write(f'\nThis is the newly appended text')
# afile.close()
import shelve
shelvefile=shelve.open('testfile.txt')
# shelvefile['cats']=['sofi','reddy','cutie']


print(list(shelvefile.values()))
shelvefile.close()
