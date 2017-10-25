#coding:utf-8
from Crypto import *
from Crypto.Cipher import AES

f = open("7.txt")
ciphertext = f.read().decode("base64") #length = 2880 = 128*22
key = "YELLOW SUBMARINE"
decryptor = AES.new(key, AES.MODE_ECB)
plaintext = decryptor.decrypt(ciphertext)
output = open("s1_7_result.txt",'w')
output.write(plaintext)
