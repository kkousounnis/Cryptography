import sys, getopt, hashlib
from math import exp, expm1 

import random

SECRET = "s2rj6235-77d3-3405-3d23-462w34179227"

def mykey(key):
    return hashlib.sha256(key + SECRET).hexdigest()



# string to binary
def ConvertStringToBinary(s):
    return ''.join('{:08b}'.format(ord(c)) for c in s)

# binary to int
def ConvertBinarytoInt(s):
    return int(s, 2)

# int to binary
def IntegerToBInary(i):
    return bin(i)

# binary to string
def BinaryToString(b):
    n = int(b, 2)
    return ''.join(chr(int(b[i: i + 8], 2)) for i in xrange(0, len(b), 8))

def My_Function(x, i, k):
    k = ConvertStringToBinary(k)
    x = ConvertStringToBinary(str(x))

    k = ConvertBinarytoInt(k)
    x = ConvertBinarytoInt(x)

    res = pow((x * k), i)
    res = IntegerToBInary(res)

    return BinaryToString(res) 

# xor two strings
def xor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2)) 

def SubKeyGeneration(s1, s2, i):
    #print ("GENERATING KEY #" + str(i))
    #print ("S1: " + s1)
    #print ("S2: " + s2)
    SubKey = hashlib.sha256(s1 + s2).hexdigest()
    #print ("SubKey: " + SubKey)
    return SubKey

CreditCardNumber=4532294877918448 #Its an example of a credit card number that the article give us.
print ("CreditCardNumber:" + str(CreditCardNumber))

key= ''.join(chr(random.randint(0,0xFF))for i in range(16)) #create a random 16 byte key.

BinaryFormOfCreditCardNumber=bin(CreditCardNumber)[2:] #Calculate the binary form of the credit card number.

print (BinaryFormOfCreditCardNumber)
#print(len(BinaryFormOfCreditCardNumber)) 

ROUNDS = 4
BLOCKSIZE = 54
BLOCKSIZE_BITS = 54


cipherCreditCardNumber = ""
n = BLOCKSIZE  
BinaryFormOfCreditCardNumber = [BinaryFormOfCreditCardNumber[i: i + n] for i in range(0, len(BinaryFormOfCreditCardNumber), n)] 
#print(BinaryFormOfCreditCardNumber)

lengthOfLastBlock = len(BinaryFormOfCreditCardNumber[len(BinaryFormOfCreditCardNumber)-1])

if ( lengthOfLastBlock < BLOCKSIZE):
        for i in range(lengthOfLastBlock, BLOCKSIZE):
            BinaryFormOfCreditCardNumber[len(BinaryFormOfCreditCardNumber)-1] += " "

TemporaryKey = mykey(key)
MyFirstKey = TemporaryKey

for block in BinaryFormOfCreditCardNumber:
        #print ("Block: " + block)
        L = [""] * (ROUNDS + 1)
        R = [""] * (ROUNDS + 1)
        L[0] = block[0:BLOCKSIZE/2]
        R[0] = block[BLOCKSIZE/2:BLOCKSIZE]
	print ("L Initial: " + L[0])
	print ("R Initial: " + R[0])
	for i in range(1, ROUNDS+1):

        	L[i] = R[i - 1]
        	if (i == 1):
                	Key = MyFirstKey
		else:
                	Key = SubKeyGeneration(L[i], MyFirstKey, i)
		    
            	R[i] = xor(L[i - 1], My_Function(R[i - 1], i, Key))

        cipherCreditCardNumber += (L[ROUNDS] + R[ROUNDS])

print ("CipherCreditCardNumber:")
print(cipherCreditCardNumber)
print ("LengthOfCipherText:")
print(len(cipherCreditCardNumber))



