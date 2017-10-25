#coding:utf-8
def xor_strings(xs,ys):
    return "".join(chr(ord(x) ^ ord(y)) for x,y in zip(xs,ys))

plaintext = "Burning 'em, if you ain't quick and nimble" + "\n" + "I go crazy when I hear a cymbal"
key = 'ICE'*(len(plaintext)/3)+'ICE'[:len(plaintext)%3]
result = xor_strings(plaintext,key).encode("hex")
print result
