#list

list=eval(input("Enter list: "))
print(list)
print(type(list))

lt=list(range(0,11,3))
print(lt)

l=[3,34,53.654]
s="Mohit"
sl=list(s)
print(sl)

l=[13,321,232,'sfd']
print(l[0],l[3])
print(l[1:3])

l=[0,1,2,3,4,5,6,7,8,9]
i=0
while(i<len(l)):
    print(l[i],end=" ")
    i+=1

print()
for i in l:
    print(i,end=" ")

n=[0,1,2,3,0,5,0,7,2,9]
print(len(n))
print(n.count(0))
print(n.count(2))
print(n.count(4))

l=[4,34,45,2]
l.append(5)
print(l)

#insert at specific

l=[23,34,322]
l.insert(2,999)
l.insert(0,1)
print(l)

#remove if multiple occurance only one is removed first left to right
n=[32,53,23,233,23,233]
n.remove(23)
print(n)


n=[1,2,3,4]
n.pop()
print(n)

n.reverse()
print(n)

n.sort()
print(n)

n=[10,20,30,40]
print(n)
n.clear()
print(n)

n=['fsdfs','dsfsd']
print(n[0][1])

n=[10,20,[30,40]]
print(n[2][1])

a=int(input("Enter no of sem : "))
l=[]
for i in range (a):
    print("Enter no of subjects in ",i+1," sem : ",end="")
    l.append(int(input()))
m=[]
j=1
for x in l:
    i=0
    t=[]
    while i<x:
        print("Enter marks of ",i+1," subject of ",j," sem : ",end="")
        t.append(int(input()))
        i+=1
    m.append(t)
    j+=1
for i in range (a):
    print("max marks for sem",i+1,"=",max(m[i]))
    

#next largest element

n=[115,52,75,10,95]
ans=[]
for i in range (len(n)):
    max=n[i]
    key=0
    for j in range (i+1,len(n)):
        if max<n[j]:
            key=1
            max=n[j]
            break;
    if(key):
        ans.append(max)
    else:
        ans.append(-1)
print(ans)

#compress
s='aaaaabbbccccc'
l=len(s)
c=s[l-1]
ans=''
i=0
while i<l:
    x=s[i]
    count=0
    while (i<l and x==s[i]):
        count+=1
        i+=1
    ans+=x
    ans+=str(count)
print(ans)


s='aabbccc'
a=''
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        a+=s[i-1]+str(count)
        count=1
a+=s[i-1]+str(count)
print(a)


#anagram
a='Listen'
b='Silent'

a=a.lower()
b=b.lower()
print(sorted(a)==sorted(b))

t=eval(input("Enter : "))
l=len(t)
sum=0
for i in range(l):
    sum+=t[i]
print (sum)
avg=sum/l
print(avg)


import operator
t1=(10,20,30)
t2=(10,20,30)
t3=(40,50,60)
print(t1==t3)


#set
l=[10,20,10,30,40,10]
s=set(l)
sorted(s)
print(s)

s={10,12,6,5,55}
print(s.pop())
s.remove(10)
print(s)


#dictionary
d={}
d[100]="mohit"
d[101]="singh"
print(d)

d1={10:"mohit",11:"singh",10:"rohit"}
print(d1[10])

d={100:'mohit',200:'singh'}
for k,v in d.items():
    print(k,v)

d=dict()
n=int(input("Enter no of key value pair : "))
for i in range (n):
    k=int(input("Enter key : "))
    v=input("Enter value : ")
    d[k]=v
print(d)
ou=''
for v in d.values():
    ou+=v
print(ou)


#function
def myfun(a,b)->int:
    print("Hello")
    res=a+b
    return res,a,b

if __name__ == "__main__":
    print("hello")
    sum,a,b=myfun(10,20)
    print(sum,a,b)

def varArg(*n):
    print(n)

varArg(10,203,30)

#lambda function
#lambda argument:expresion

s=lambda n:n*n

print(s(4))

a=lambda x,y:x+y
print(a(10,20))

l=lambda a,b: a if a>b else b
print(l(10,20))