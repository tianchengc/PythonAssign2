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
        
        
