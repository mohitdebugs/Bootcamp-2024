#slicing 

a="raghav"
b="joshi"
c=a+b
print(c)
print(a[0])
print(c[0:5])
print(a[::-1])
print()
for i in range (10):
    for j in range (i):
        print(c[j],end="")
    print()

#type cast
a=5.2
print(int(a))

a="10"
print(int(a))  #if a was a float it wont conver as a string to int a="10.5" 
#ValueError: invalid literal for int() with base 10: '10.5'
a="10.5"
print(float(a))

#complex

a=10.5
b=2
print(complex(a,b))
print(complex(True,False)) #0+0j

#list

list=[]
for i in range(0,5):
    list.append(int(input()))
print(list)


#operator 

a=10
b=10
print(a is not b)
x=True
y=True
print(x is y)

#add first and last

a=int(input())
b=int(a[0])
c=int(a[-1])
sum=b+c
print(sum)