import math
import random

def primary_school_quiz(flag, n):
    # Your code for primary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    count=0
    for i in range(n):
        x=random.randint(0,9)
        y=random.randint(0,9)
        if flag==0:
            a=str(x)+'-'+str(y)
            b="Question"+ str(i+1) + ":\n" "What is the result of "+ a +" ? "
            answer=int(input(b))
            z=x-y
    
        elif flag==1:
            a=str(x)+'^'+str(y)
            b='Question'+str(i+1)+':\n' 'What is the result of '+a+ " ? "
            answer=int(input(b))
            z=x**y
        if answer==z:
            count=count+1
    return(count)         


def high_school_eqsolver(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    if a==0 and b==0 and c==0:
        print('The quadratic equation',str(a)+'\u00B7x','+',str(b),'+',str(c),'= 0\nis satisfied for all numbers x')
    elif a==0 and b==0 and c!=0:
        print('The quadratic equation',str(a)+'\u00B7x','+',str(b)+'x','+',str(c),'= 0\nis satisfied for no numbers x')
    elif a==0 and b!=0:
        x1= -c/b
        print('The linear equation',str(b)+'\u00B7x','+',str(c),'= 0\n'+'has the following roots/solution:', str(x1))
    elif b**2-4*a*c >0 and a!=0:
        x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        print('The quadratic equation',str(a)+'\u00B7x^2','+',str(b)+'\u00B7x','+',str(c),'= 0\nhas the following two real roots:')
        print(x1,'and',x2)
    elif b**2-4*a*c <0 and a!=0:
        x_1=(-b)/(2*a)
        x_2=math.sqrt(4*a*c-b**2)/(2*a)
        print('The quadratic equation',str(a)+'\u00B7x^2','+',str(b)+'\u00B7x','+',str(c),'= 0\nhas the following two complex roots:')
        print(str(x_1),'+ i',str(x_2),'\nand')
        print(str(x_1),'- i',str(x_2))
    elif b**2-4*a*c == 0 and a!=0:
        x=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        print('The quadratic equation', str(a)+'\u00B7x^2','+',str(b)+'\u00B7x','+',str(c),'= 0\nhas only one solution, a real root:')
        print(x)
    

def ascii_name_plaque(x):
    '''print a message about the area of square with the given name'''
    y=len('*  __'+x+'__  *')
    print('*'*y)
    print('*'+' '*(y-2)+'*')
    print('*  __'+x+'__  *')
    print('*'+' '*(y-2)+'*')
    print('*'*y)




# main

# your code for the welcome tmessage goes here

greeting='Welcome to my math quiz-generator / equation-solver'
ascii_name_plaque(greeting)

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    # your code goes here
    ascii_name_plaque(name+' welcome to my quiz-generator for primary school students.')
    flag=input(name+' what would you like to practice? Enter\n0 for subtraction\n1 for exponentiation\n')
    n=input('How many practice questions would you like to do? ')
    print(name+', here is your '+n+' questions:')
    result=primary_school_quiz(flag, int(n))
    grade=result/n
    if grade>=0.9:
        print('Congratulations '+name+' ! You’ll probably get an A tomorrow. Now go eat your dinner and go to sleep. Good bye '+name+' !')
    elif grade>=0.7:
        print('You did well '+name+', but I know you can do better. Good bye '+name+' !')
    else:
        print('I think you need some more practice '+name+'. Good bye '+name+' !')
    
elif status=='2':

    # your code for welcome message
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
 
else:
    # your code goes here
    pass

print("Good bye "+name+"!")
