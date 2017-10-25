#coding:utf-8
import hashlib
import itertools as itr

words = 'owinOWIN580%()+=-'
r = itr.product(words,repeat=8)
for i in r:
    hash_new = hashlib.sha1()
    hash_new.update(num)
    hash_value = hash_new.hexdigest()

    if hash_value == '67ae1a64661ac8b4494666f58c4822408dd0a3e4':
        print "FOUND!",data
        break
else:
    print "Nothing!"
