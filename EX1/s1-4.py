jj#coding:UTF-8
import freqAnalysis

d = open("encoded.txt-4", "rb").readlines()



sum = []

for i,line in enumerate(d):
  hexline = line[:-1].decode("hex")
  print "\n", i,": hexline ->", hexline
  sumd = 0
  for c in range(127):
    matchScore = freqAnalysis.englishFreqMatchScore(''.join([ chr(c ^ ord(x)) for x in hexline]))
    sumd += matchScore
    print c," :" , chr(c), " -> ", matchScore
  print sumd
  sum.append(sumd)


print max(sum)
