import math
import random
import cmath


def primary_school_quiz(flag, n):
    count=0
    for i in range(n):
        x=random.randint(0,10)
        y=random.randint(0,10)
        if flag==0:
            a=str(x)+'-'+str(y)
            b="question"+ str(i+1) + ":\n" "what is the result of "+ a +" ?"
            answer=int(input(b))
            z=x-y
    
        elif flag==1:
            a=str(x)+'^'+str(y)
            b='question'+str(i+1)+':\n' 'what is the result of '+a+ '?'
            answer=int(input(b))
            z=x**y
        if answer==z:
            count=count+1
    print(count)            
        
        
    # Your code for primary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    pass
    
def high_school_eqsolver(a,b,c):
    if b**2-4*a*c >0 and a!=0:
        x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        print('The quadratic equation',str(a)+'.x^2','+',str(b)+'.x','+',str(c),'= 0\nhas the following two real roots:')
        print(x1,'and',x2)
    if b**2-4*a*c <0 and a!=0:
        x1=(-b+cmath.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-cmath.sqrt(b**2-4*a*c))/(2*a)
        print('The quadratic equation',str(a)+'.x^2','+',str(b)+'.x','+',str(c),'= 0\nhas the following two complex roots:')
        print(str(x1),'\nand\n'+str(x2))
    if a==0 and b!=0 and c!=0:
        x1= -c/b
        print('The linear equation',str(b)+'.x','+',str(c),'= 0\n'+'has the following roots/solution:', str(x1))
    if a==0 and b==0 and c==0:
        print('The quadratic equation',str(a)+'.x','+',str(b),'+',str(c),'= 0\nis satisfied for all numbers x')
    if (a==0 and b==0 and c!=0) or (a==0 and b!=0 and c==0) or (a!=0 and b==0 and c==0):
        print('The quadratic equation',str(a)+'.x','+',str(b)+'x','+',str(c),'= 0\nis satisfied for no numbers x')
        
    
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    pass

# main

# your code for the welcome tmessage goes here
y=len('*__'+'Welcome to my math quiz-generator / equation-solver'+'__*')
print('*'*y)
print('*'+(y-2)*' '+'*')
print('*__'+'Welcome to my math quiz-generator / equation-solver'+'__*')
print('*'+(y-2)*' '+'*')
print('*'*y)

name=input("What is your name?")
name=name.capitalize()
#print(name)
welcome="Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n"
status=input(str(welcome))
if status =='1':
    y=len('*__'+name+' welcome to my quiz-generator for primary school students.'+'__*')
    print('*'*y)
    print('*'+(y-2)*' '+'*')
    print('*__'+name+' welcome to my quiz-generator for primary school students.'+'__*')
    print('*'+(y-2)*' '+'*')
    print('*'*y)

elif status=='2':
    y=len('*__'+name+' welcome to my quiz-generator for high school student.'+'__*')
    print('*'*y)
    print('*'+(y-2)*' '+'*')
    print('*__'+name+'__*')
    print('*'+(y-2)*' '+'*')
    print('*'*y)

elif status=='3':
    y=len('*__'+name+' welcome to my quiz-generator for none of above.'+'__*')
    print('*'*y)
    print('*'+(y-2)*' '+'*')
    print('*__'+name+'__*')
    print('*'+(y-2)*' '+'*')
    print('*'*y)
    
pratice= name+' what would you like to practice? Enter\n0 for subtraction\n1 for exponentiation'
status2=input(str(pratice))

#if status=='1':
    # your code goes here
    #pass

#elif status=='2':

    # your code for welcome message
    #flag=True
    #while flag:
        #question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here

        #if question!="yes":
            #flag=False
        #else:
            #print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
 
#else:
    # your code goes here
    #pass

#print("Good bye "+name+"!")
#pass
