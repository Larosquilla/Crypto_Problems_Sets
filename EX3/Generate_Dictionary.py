#coding:Utf-8
import itertools as itr

words = 'owinOWIN580%()+=-'
r = itr.product(words,repeat=8)
dic = open("/Users/user/Desktop/Problem sets/EX3/generate.txt",'a')
for i in r:
    dic.write("".join(i))
dic.close()
