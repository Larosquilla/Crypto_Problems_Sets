#coding:utf-8
# 计算汉明距离
def hamming_distance(s1,s2):
    count = 0
    b1 = bin(ord(s1))[2:]
    b2 = bin(ord(s2))[2:]

    if len(b1) < 16:
        b1 = b1.zfill(16)
    if len(b2) < 16:
        b2 = b2.zfill(16)
    for i in range(0,len(b1)):
        if b1[i] != b2[i]:
            count += 1
    return count

#测试可能的密钥长度
def normalized(instr):
    result = 0.0
    for keysize in range(2,40):

        for i in range(keysize):
            # 依次比较以key为长度分的明文块的对应字符
            result += hamming_distance(instr[i],instr[keysize+i])
            result += hamming_distance(instr[keysize+i],instr[2*keysize+i])
            result += hamming_distance(instr[2*keysize+i],instr[3*keysize+i])
            result += hamming_distance(instr[3*keysize+i],instr[4*keysize+i])

        print(keysize),"-->",
        print(result/(keysize*4))
        result = 0.0


f = open('6.txt','r')
g = f.read().decode("base64")
normalized(g)
f.close()
