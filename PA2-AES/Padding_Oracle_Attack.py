#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open("/Users/user/Desktop/Problem sets/PA2-AES/challenge.txt")
g = f.read().decode("hex")
print str(g)
f.close()
iv = g[:16]
ct = g[16:32]
result = ""
for i in range(1,5):
    pt = g[16*i:16*(i+1)]
    ct =  "".join(chr(ord(x) ^ ord(y)) for x,y in zip(iv,pt))
    result+= ct
    iv = ct


print result.encode("hex")
