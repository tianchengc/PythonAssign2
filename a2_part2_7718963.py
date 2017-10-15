def min_enclosing_rectangle(radius, x, y):
    if radius<0:
        return None
    else:
        co_x=x-radius
        co_y=y-radius
        return (co_x,co_y)

def series_sum():
    num=int(input("Please enter a non-negative integer: "))
    summary=1000
    if num<0:
        return None
    else:
        for i in range(num):
            n=i+1
            summary+=(1/(n**2))
        print(summary)
    
def pell(n):
    n=int(n)
    p1=0
    p2=1
    p3=0
    if n<0:
        return None
    elif n==0 or n==1:
        print(n)
    else:
        for i in range(n-1):
            p3=2*p2+p1
            p1=p2
            p2=p3
        print(p3)
                
def countMembers(s):
    source='efghijFGHIJKLMNOPQRSTUVWX23456!,\\'
    count=0
    for i in s:
        if i in source:
            count+=1
    print(count)

def casual_number(s):
    number='1234567890'
    output=''
    length=len(s)
    rest=length%4
    for n in range(length):
        if (s[n] not in number):
            if n==0 and s[n]=='-' and s[n+1] in number:
                output=output+s[n]
            elif (n-rest)%4==0 and s[n]==',':
                pass
            else:
                return None
        else:
            output=output+s[n]
    print(output)

def alienNumbers(s):
    value=s.count('T')*1024+s.count('y')*598+s.count('!')*121+s.count('a')*42+s.count('N')*6+s.count('U')*1
    print(value)

def alienNumbersAgain(s):
    value=0
    for i in s:
        if i=='T':
            value+=1024
        elif i=='y':
            value+=598
        elif i=='!':
            value+=121
        elif i=='a':
            value+=42
        elif i=='N':
            value+=6
        elif i=='U':
            value+=1
    print(value)

def encrypt(s):
    s=list(s)
    length=len(s)
    output=[]
    for n in range(length):
        output.append(s.pop())
        s.reverse()
    output_r=''.join(output)
    print(output_r)

def oPify(s):
    #s=list(s)
    length=len(s)
    output=''
    for n in range(length):
        if n==length-1:
            output=output+s[n]
            break
        elif s[n].isalpha() and s[n+1].isalpha():
            if s[n].isupper():
                block=s[n]+'O'
            else:
                block=s[n]+'o'
            if s[n+1].isupper():
                block=block+'P'
            else:
                block=block+'p'
            output=output+block
        else:
            output=output+s[n]
    print(output)

def nonrepetitive(s):
    length=len(s)
    flag=True
    for n in range(length//2):
        for x in range(length-2*n-1):
            if s[x:x+n+1]==s[x+n+1:x+n+n+2]:
                flag=False
    print(flag)
            
    


    
