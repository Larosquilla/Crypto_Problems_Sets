#coding:Utf-8
import hashlib
def get_pwd(str, num):
        if(num == 1):
            for x in str:
                yield x
        else:
            for x in str:
                for y in get_pwd(str, num-1):
                    yield x+y
f = open("/Users/user/Desktop/Problem sets/EX3/generate.txt",'a')

biglist = [['q','Q'],['w','W'],['i','I'],['n','N'],['5','%'],['8','('],['=','0'],['+','*'],]
for i in range(1,8)

strKey="qwinQWIN580%()+-="
for x in get_pwd(strKey,8):
    f.write(x)
f.close()
'''
    hash_new = hashlib.sha1()
    hash_new.update(x)
    hash_value = hash_new.hexdigest()
    if hash_value == '67ae1a64661ac8b4494666f58c4822408dd0a3e4':
        print "FOUND!",data
        break
else:
    print "NOT FOUND!"
'''
