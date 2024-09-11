a=4
x=bin(a).replace("0b","")
c=x.count('1')
print(c)
print(x[0])


s="abaaa"
count=0
se=[]
for i in range(len(s)):
    str=''
    for j in range(i,len(s)):
        str+=s[j]
        if(str==str[::-1]):
            se.append(str)
se=set(se)
print(len(se))
