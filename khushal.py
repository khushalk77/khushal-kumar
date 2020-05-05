#!/usr/bin/env python
# coding: utf-8

# # lab 2

# In[2]:


n=int(input("enter number of days :"))
if (n==365):
    print("this is not a leap yeaar")
elif(n==366):
     print("this is a leap year")
else:
    print("invalid days :"+n)
        


# In[5]:


print('        '+"*")
print('     '+"*" +'    '+"*")
print('  '+"*" +'    '+"*"'     '+"*")
print(' '+"*"   +'   '+"*"'     '+"*"'   '+"*")


# In[5]:


a=int(input("enter any number :"))
fact=1
if(a<0) :
    print("factorial not possible")
elif(a==0):
         print("factorial of 0 is 1")
else:
    for i in range(1,a+1):
        fact=fact*i
    print("factorial of " ,a, "is",fact)


# In[6]:


a=str(input("enter any number :"))
b=str(input("enter any number :"))
if (a>b) :
    print("a is greater :" +a )
else:
    print("b is greater :" +b)


# In[7]:


n=str(input("enter any alphabet :"))
if (n =='a' or n =='e' or n =='i'or n =='o' or n =='u' ) :
    print("these are vowels")
else:
    print("these are consonants :" +n)


# In[11]:


n=int(input("enter any number :"))
if(n%2)==0 :
    print("number is even")
else:
         print("number is odd")


# In[31]:


num=int(input("enter any number :"))
if num > 1: 
      for i in range(2, num): 
            if (num % i) == 0: 
                print(num, "is not a prime number") 
                break
            else: 
                print(num, "is a prime number") 
else: 
    print(num, "is not a prime number") 


# In[1]:


nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1


# In[1]:


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")


# # lab 3

# # ques 1

# In[1]:


n=str(input("enter any string:"))
len(n)


# #  ques 2
# 

# In[4]:


n=str(input("enter any string:"))
counter=0
for i in n:

    counter=counter+1
print("length of string",counter)


# # ques 3

# In[3]:


n=str(input("enter any sting :"))
if len(n)<=2:
    print("empty string")
else:
    n=n[0:2]+n[-2:]
    print(n)


# 

# In[2]:


n=str(input("enter any string:"))
l=n[0]
new_str=n.replace(l,"$")
print(l+new_str[1:])


# In[10]:


n=str(input("enter any string:"))
y=str(input("enter any string:"))
print(y[0:2]+n[-2:],"   ",n[0:2]+y[-2:])


# In[12]:


n=str(input("enter any string :"))
if len(n)<3:
    print(n)
elif n[-3:]=="ing":
    print(n +"ly")
else:
    print(n +"ing")


# In[ ]:





# In[ ]:




