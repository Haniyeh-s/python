#Exercises #1 / Tutorial on 9.11.2023

#1 Finger-flexing
#a
# %%
import math
# %%
a = (42**3 + 17)/((3/8)-(14**1/2))
b = math.sin(math.cos((math.tan(0.524)**math.log(18))))
print(a,b)
#b
a = input("give me a number: ")
a = int(a)
print(a**3, a**2)

# %%
def SumString():
    a = input("give me one name: ")
    b = input("gime me onother one: ")
    c = a+b
    return c
#%%
def WrongNum():
    a = input ("give me a numer: ")
    if a == 1 or  a == 17 or  a == 42:
        print ("True") 
    else:
        print ("False")
#%%
#2 Quadratic equation solver
def quadratic_equation(a, b, c):
    while True:
        # a = input(" inter the coefficient a:  ")
        # b = input(" inter the coefficient b:  ")
        # c = input(" inter the constant c:  ")
        a = int(a)
        b = int(b)
        c = int(c)
        discriminant = b**2 - 4*a*c
        x1 = -b + discriminant**1/2
        x2 = -b - discriminant**1/2
        if discriminant >= 0:
            return (f"the equation is y = {a}x**2 + {b}x + {c} with two solutions, {x1:.3f} and {x2:.3f}")
        else:
            return (f"the equation is y = {a}x**2 + {b}x + {c} with no real solutions")
#%%        
#3 Pocket calculator of Doom
def aritmatic_op():
    operand1 = input("operand1: ")
    operand2 = input("operand2: ")
    op = input("desire mathematical operation (+,-,/,*): ")
    operand1 = int(operand1)
    operand2 = int(operand2)
    
    if op == "*":
        return operand1*operand2
    elif op == "/":
        return operand1/operand2
    elif op == "+":
        return operand1+operand2
    elif op == "-":
        return operand1-operand2
        
    