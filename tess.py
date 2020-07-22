def I():
    s='abcde'
    for c in s[::2]:
        yield c

for x in I():
            print(x,end='')
        
