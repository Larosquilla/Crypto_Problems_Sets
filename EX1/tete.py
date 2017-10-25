# coding:utf-8
f = open("encoded-4.txt","rb")
c = f.readlines()
for i,line in enumerate(c):
     hexline = line[:-1].decode("hex")
     key = ord(max(hexline,key=hexline.count)) ^ ord(' ')
     result = ''.join(chr(key ^ ord(a)) for a in hexline)
     print "第%d行" % (i+1),
     print result

f.close()
