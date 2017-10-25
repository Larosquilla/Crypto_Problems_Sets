#coding:utf-8
from Crypo.Cipher import AES
f = open("/Users/user/Desktop/Problem sets/PA2-AES/challenge.txt")
g = f.read().decode("hex")
f.close()
print len(g)
iv = g[:16]
result = ""
for i in range(1,3):
    encrypted_input = g[16*i:16*(i+1)]
    middle_value =
    decrypted_value =  "".join(chr(ord(x) ^ ord(y)) for x,y in zip(iv,middle_value))
    result+= ct
    iv = encrypted_input


print result.encode("hex")
