#coding:utf-8
def xor_strings(xs,ys):
    return "".join(chr(ord(x) ^ ord(y)) for x,y in zip(xs,ys))
f = open("6.txt")
plaintext = f.read().decode("base64")
key="Terminator X: Bring the noise"*(len(plaintext)/29)+"Terminator X: Bring the noise"[:len(plaintext)%29]
result = xor_strings(plaintext,key)
print result
f.close()
