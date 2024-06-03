import random
import sys

def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    print(f"size = {sys.getsizeof(filename)}")
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        

    file = open("CC-" + filename, "wb")
    file.write(data)
    file.close()

def Decrypt(filename,key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    key=int(input("enter key "))
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()

#key=random.randrange(1,255)
#print(f"key :{key}")
key = int(input("Enter a key from 1 - 255 "))
filename =(input("Enter filename "))
Encrypt(filename, key)
        
    