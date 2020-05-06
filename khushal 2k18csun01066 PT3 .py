#!/usr/bin/env python
# coding: utf-8

# # 1. What is the syntax to call a constructor of a base class from child class 
# 
# ans: class parentclassname:
#         def _init_(self,var):
#             self.var=var
#             print(self.var)    
#      class childclassname(parentclassname):
#              pass     
#      x=10
#      obj = childclassname(x) 
#      
#      class A:
#     def _init_(self,x):
#         self.x=x
#         print(self.x)
# class B(A):
#     pass 
# x=10
# d1 = B(x)
#      
# 

# # 2. How is a class made as inherited class (syntax of child class)   
# class childclassname(parentclassname):
#            pass
#       obj = childclassname()
#       obj.methodofparentclass()
# 
# 
# 
# class A:
#     def find(self):
#         print('good morning')
# class B(A):
#     pass
# d1 = B()
# d1.find()
#  

# # 3. Print an element of a nested dictionary 
# 
# 
# d1={1:'A',2:'B',3:('C','D'),4:['E','F','G','H'],5:{'A':1,'B':2,'C':3}}
# d1
# d1[4][0]

# # set  c

# # ques 1

# In[2]:


import math
value1=int(input("enter any number : "))
value2=int(input("enter any number : "))
value3=int(input ("enter any number: "))
m=((2*value1*value2)/(value3))
print(math.sqrt(m))


# # ques 2

# In[7]:


x= input('enter the string: ')
y=x[::2]
print(y)


# In[ ]:




