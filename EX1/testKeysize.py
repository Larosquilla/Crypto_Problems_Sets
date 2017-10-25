#coding:utf-8
import freqAnalysis

keysize = 29
f = open('6.txt','r')
g = f.read().decode("base64")
def testEnglishLetters(instr,keysize):
    inlist = list(instr)
    plist = inlist[:100*keysize:keysize]
    for c in range(127):
        total = 0
        lettercount = freqAnalysis.getLetterCount("".join(chr(c ^ ord(x)) for x in plist))
        for k in lettercount:
            total += lettercount[k]
        m = map(c,)
        print chr(c),"-->",total


testEnglishLetters(g,keysize)
