# coding:utf-8
f = open('6.txt')
g = f.read().decode("base64")
num = len(g)/29
keysize = 29
alphabet = "1234567890"+"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"+" "+"\n"+",.:;…?!-''"
key = []
for groupnumber in range(num):
    group = list(g)[groupnumber::keysize]
    print '----',groupnumber,'----'
    for c in range(32,127): #32之前都是控制字符

        result = "".join(chr(c ^ ord(x)) for x in group)
        allwords = list(result)
        for a in allwords:
            if a not in alphabet:
                break
        else:
            key.append(chr(c))
            print "BINGO!This is group %d:" % groupnumber
            print chr(c)
        #print chr(c),"-->",result
print key
f.close()
'''
刚开始每组都看一下，看看大概能不能目测找到key
groupnumber = 2
group = list(g)[groupnumber::keysize]
print '----',groupnumber,'----'
for c in range(32,127): #32之前都是控制字符

    result = "".join(chr(c ^ ord(x)) for x in group)
    allwords = list(result)
    for a in allwords:
        if a not in alphabet:
            break
    else:
        print "BINGO!"
    print chr(c),"-->",result
'''
