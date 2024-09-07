#main
if __name__ =='__main__':
    print("HEllo")


#print format
name="Mohit"
salary="1000000"
print("Hello {0} your salary is {1}".format(name,salary))

a=10
b="ftr"
print("hello %d id %s"%(a,b))


#if else
n=555
if(n%2==0):
    print("even")
else:
    print("odd")

a,b,c,d,e=input("Enter 5 number").split()
max=a
if b>max:
    max=b
if c>max:
    max=c
if d>max:
    max=d
if e>max:
    max=e
print(max)
print(type(max))
max=int(max)
print(type(max))

#cost price 
cost=int(input("Enter Cost : "))
print("Are you student Y/N : ",end="")
stu=input()
if stu=='Y'or'y' :
    if cost>500 :
        dis=10
    else:
        dis=8
else:
    dis=2

price=cost-(cost*dis)/100
print(price)

#multi input
a,b,c,d,e=map(int,input("Enter five subject marks out of 100 : ").split())
gender=input("Enter gender M/F : ")
total=a+b+c+d+e
per=total/5
if gender=='F' and per>=82:
    ad=1
elif gender=='M' and per>=62:
    ad=1
else:
    ad=0
if(ad):
    print("admitted")
else:
    print("Next time :) ")

#reverse usig slicing
a=input("Enter : ")
b=int(a[::-1])
print(b)

num=int(input("Enter Number : "))
#reverse count sum product
temp=num
rev=0
count=0
sum=0
prod=1
while temp>0:
    rem=temp%10
    sum+=rem
    prod*=rem
    rev=rev*10+rem
    temp//=10
    count+=1
print(count)
print(rev)
print(sum)
print(prod)


#palindrome 
n=int(input("enter the number "))
temp=n
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp//=10
if(rev==n):
    print("palindrome")
else:
    print("no pali")


#armstrong

n=int(input("enter the number "))
temp=n
arm=0
while temp>0:
    rem=temp%10
    arm+=rem**3
    temp//=10
if(arm==n):
    print("arm")
else:
    print("no arm")


#armstrong
n=int(input("enter the number "))
temp=n
arm=0
count=0
while temp>0:
    count+=1
    temp//=10
temp=n
while temp>0:
    rem=temp%10
    arm+=rem**count
    temp//=10
if(arm==n):
    print("arm")
else:
    print("no arm")


for n in range (1,1000):
    temp=n
    arm=0
    rem=0
    count=0 
    while temp>0:
        count+=1
        temp//=10
    temp=n
    while temp>0:
        rem=temp%10
        arm+=rem**count
        temp//=10
    if(arm==n):
        print(n)

#fact

n=int(input("Enter "))
x=int(input("Enter "))
sum=1
fact=1
for i in range (1,n+1):
    fact*=i
    sum+=(x**i)/fact
print(sum)


#function
def myfun():
    print("Hello")


if __name__ =="__main__":
    myfun()


#automorphic

n=int(input("Enter "))
nn=n**2
temp=n
rem=0
j=1
while n>0:
    rem+=(nn%10)*j
    nn//=10
    n//=10
    j*=10
if rem==temp:
    print("Yes")
else:
    print("No")


#peterson

n=int(input("Enter "))
tem=n
sum=0
while tem>0:
    x=tem%10
    fact=1
    while x>0:
        fact*=x
        x-=1
    sum+=fact
    tem//=10
if n==sum:
    print("peterson")
else:
    print("No")

#tech number
n=input("Enter ")
l=len(n)
if l%2!=0:
    print("no")
    exit
a=int(n[0:int(l/2)])
b=int(n[int(l/2):l])
sum=a+b
print(sum)
res=sum*sum
print(res)
if res==int(n):
    print("Tech")
else:
    print("NO")

#pattern 

for i in range (1,6):
    if i==3:
        continue
    print (i,11-i)

#find
s="tybgn uerfdn rerhn8gen"
print(s.find("rer"))
print(s.rfind("n"))

#count
s="esfdfedsfdsdf"
print(s.count('f'))

print(s.count('f',2,9))
print(s.count('fd'))

#replace
s="esf dfedsf dsdf"
s1=s.replace('df','ef')
print(s1)


#string Fn
s1='Mohit2'
s2='Mphd'
s3='8525'
print(s1.isalnum())
print(s2.isalpha())
print(s3.isdigit())

s='Mohit Singh'
s1=s[::-1]
s2=''.join(reversed(s))
print(s1,s2)

s="sdfghj"
l=len(s)
x=""
for i in range (l):
    x+=s[l-i-1]
print(x)

s="ffgh"
rev=""
for x in s:
    rev=x+rev
print(rev)

s="gvfcdddd"
t=""
for x in s:
    if x not in t:  
        t+=x 
print(t)

