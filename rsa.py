#Brynna Mering and Lucy Lu 
#CS 202 ps23
import math
import random
#This function calculates b^e mod n through recursion
def modExponentiate(b,e,n):
   if e == 0:
       return 1
   if e%2==0:
       x =  modExponentiate(b,e/2,n)
       return ((x**2) % n)
   if e%2!=0:
       x = modExponentiate(b,(e-1),n)
       return ((b * x) % n)

#This function performs the extended Euclidian 
#algorithm on two numbers to return x, y and the gcd
def extendedEuclid(n,m):
   if m%n==0:
       return 1,0, n
   else:
       x,y,r = extendedEuclid(m%n,n)
       return y-(m/n)*x,x,r

#This function finds the multiplicative inverse of a in modolus n
def multiplicativeInverse(a,n):
   x,y,d=extendedEuclid(a,n)
   if d==1:
       return x%n
   else:
       return False

#This function converts a string into a list in ints which are
#no larger than k
def toIntlist(s,k):
   intlist=[]
   chunk=[]
   for i in range(0, len(s)):
       number = ord(s[i])
       if len(chunk)<k:
           chunk.append(number)
       if len(chunk)==k or i==(len(s)-1):
           result = 0
           g = len(chunk)-1
           j=0
           while g >=0:
               result = result + chunk[g]*(127**j)
               j=j+1
               g=g-1
           intlist.append(result)
           chunk=[]
   return intlist

#This function convert a list of ints back into a string
def toString(L):
   resultString=''
   string=''
   for item in L:
       n = item
       while n > 0:
           d = n % 127
           char=chr(d)
           string=char+string
           n=(n-d)/127
       resultString = resultString+string
       string = ''
   return resultString

#This function generates a public and private key
def keygen(p,q):
   n = p*q
   k = (p-1)*(q-1)
   while True:
       e = random.randint(2,k-1)
       x,y,r = extendedEuclid(e,k)
       if r ==1:
           break
   d = multiplicativeInverse(e,k)
   public = (n,e)
   private = (n,d)
   return public, private

#This function ecrypts a message using a public key
def encrypt(m, publicKey):
   e = publicKey[1]
   n = publicKey[0]
   k = len(str(n-1))
   cipherCode=toIntlist(m,2)
   encryptList = []
   for item in cipherCode:
       c = modExponentiate(item,e,n) 
       encryptList.append(c)
   return encryptList
 
#This function decrypts a message using a private key
def decrypt(y,privateKey):
   d= privateKey[1]
   n = privateKey[0]
   decryptList = []
   for item in y:
       m = modExponentiate(item,d,n) 
       decryptList.append(m)

   decryptText = toString(decryptList)
   return decryptText

#This funtion tests our other functions
def main():
  p = 5277019477592911
  q = 7502904222052693
  m = "THE SECRET OF BEING BORING IS TO SAY EVERYTHING."
  print "The secret message is: ", m
  public, private = keygen(p,q)
  y = encrypt(m,public)
  decrypttext = decrypt(y,private)
  print "The decipher text is: ", decrypttext
    
main()

