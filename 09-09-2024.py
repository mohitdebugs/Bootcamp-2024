import math
n=int(input("Enter Range"))
c=[0]*10
if n<10:
    print("1")
    exit
c[2]=1
c[3]=1
c[5]=1
c[7]=1
c[9]=1
print(c)
for i in range (10,n+1):
    prime=1
    for j in range (2,int(math.sqrt(i))):
        if(i%j==0):
            prime=0
            break
    if(prime):
        while(i>0):
            c[i%10]+=1
            i//=10
print(c)
print(c.index(max(c)))
#2,3,5,7,11,13,17


#exception

try:
    a=int(input("Enter : "))
    b=int(input("Enter : "))
    print(a/b)
except ZeroDivisionError:
    print("Error 0")
except ValueError:
    print("Value")


try:
    print("try")
    print(1/0)
except :
    print("hello")
finally:
    print("finally")
print('~'*10)

class Too(Exception):
    def __init__(self,arg):
        self.msg=arg 
