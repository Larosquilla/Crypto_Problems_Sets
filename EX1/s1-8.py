#coding:utf-8
f = open("8.txt")
g = f.readlines()
def splitString(s,width):
    return [s[x:x+width] for x in range(0,len(s),width)]

for num,line in enumerate(g):
    blocks = splitString(line,16)
    flag = 0
    already_had = set()
    for block in blocks:
        if block in already_had:
            flag = 1
        else:
            already_had.add(block)

    if flag >= 1:
        print num+1,line
