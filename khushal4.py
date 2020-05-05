#!/usr/bin/env python
# coding: utf-8

# tup1=(23,46,"false",49)
# print(tup1)
# print(type(tup1))

# In[2]:


tup1=(23,46,"false",49)
print(tup1[2])
print(type(tup1))


# In[4]:


tup1=(23,46,"false",493,46,"true",49)
print(tup1[2:5])
print(type(tup1))


# In[7]:


tup1=(23,46,"false",49,True,"apple","mango")
print(tup1[-4:-1])
print(type(tup1))


# In[9]:


tup1=(23,46,"false",49,True,"apple","mango")
y=list(tup1)
y[1]="orange"
tup1=tuple(y)
print(tup1)
      


# In[10]:


tup1=(23,46,"false",49,True,"apple","mango")
tup[1]="orange"
print=(tup1)


# In[12]:


tup1=(23,46,"false",49,True,"apple","mango")
if"apple" in tup1:
    print("element present")
print(len(tup1))


# In[13]:


tup1=(23,46,"false",49,True,"apple","mango")
tup1=(29,)
print(tup1)


# In[15]:


tup1=(23,46,"false",49,True,"apple","mango")
tup1=(29,)
print(tup1)
del tup1
print(tup1)


# In[16]:


x=(2,4,6)
y=(3,5,7)
z=x+y
print(z)


# #### x=(2,4,6,2,8,9,6)
# print(x.count(6))

# # lab4

# In[19]:


x=(2,4,6,2,8,9,6)
print(x.index(6))


# In[20]:


tup1=(23,46,"false",49)
print(tup1)
print(type(tup1))


# In[21]:


tup1=(23,46,"false",49)
print(tup1)
print(type(tup1))


# In[22]:


tuplex=4,8,3
print(tuplex)
n1,n2,n3=tuplex
print(n1+n2+n3)
n1,n2,n3,=tuplex


# In[23]:


x=(2,4,6)
y=(3,5,7)
z=x+y
print(z)


# In[25]:


tup1=(26,35,"false",True,"race","khushal","chirag","vasu")
print(tup1[3:-4])
print(type(tup1))


# In[26]:


x=(2,4,6,3,5,6,2,8,2)
print(x.count(2))


# In[27]:


tup1=(23,46,"false",493,46,"true",49,"apple")
if "apple" in tup1:
    print("element present")
    print(len(tup1))


# In[32]:


from copy import deepcopy
tup1=('hello',5,[],True)
print(tup1)
tup2=deepcopy(tup1)
tup2[2].append(50)
print(tup2)
print(tup1)


# # lab 5
# 

# # ques1

# In[2]:


list =[1,2,3,4,5,6]
sum(list)


# # ques2

# In[3]:


list=[1,2,3,4,5,6]
result=1
for i in list:
    result*=i
print(result)


# # ques3

# In[4]:


list=[1,2,3,4,5,6]
max=list[0]
for i in list :
    if i>max :
        max=i
    else:
        continue
print(max)


# # ques4

# In[6]:


list=[1,2,3,4,5,6]
min=list[0]
for i in list :
    if i<min :
        min=i
    else:
        continue
print(min)


# # ques5

# In[9]:


def match_words(words):
    ctr=0
    for word in words:
        if len(word) > 1 and word[0]==word[-1]:
            ctr += 2
        return ctr
match_words(['aba','xyz','1221'])


# # ques6

# In[16]:


a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
def sort_tuple(a):
    last=len(a)
    for i in range(0,last):
        for j in range (0,last-i-1):
            if(a[j][1]>a[j+1][1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
print(sort_tuple(a))


# # lab6

# In[1]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
print(thisdict)
for i in thisdict:
    print(i)


# In[3]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
print(thisdict)
for x,y in thisdict.items():
    print(x,y)


# In[4]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
print(thisdict)
for i in thisdict.values():
    print(i)
for x,y in thisdict.items():
    print(x,y)
    


# In[5]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
print(thisdict)
for i in thisdict.values():
    print(i)
for x,y in thisdict.items():
    print(x,y)
if "model"in thisdict:
    print("found")


# # ques1

# In[10]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
print(thisdict)
for i in thisdict.values():
    print(i)
for x,y in thisdict.items():
    print(x,y)
if "model"in thisdict:
    print("found")
thisdict["name"]="khushal"
print(thisdict)
thisdict.pop("name")
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict["model"]="GD"
print(thisdict)
b=thisdict.copy()
print(b)
c=dict(thisdict)
print(c)


# # ques2

# In[11]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
i=thisdict["year"]
print(i) 


# In[31]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
b="2020"
for key,value in thisdict.items():
    if b==value:
         print(key) 


# # ques3

# In[12]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
thisdict["model"]="aspire"
print(thisdict)


# # ques4

# In[19]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
thisdict["model no"]="m001"
thisdict["colour"]="black"
print(thisdict)


# # ques5

# In[26]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
print(thisdict)
for i in thisdict.values():
    print(i)
for x,y in thisdict.items():
    print(x,y)
    


# # ques6

# In[30]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
thisdict["model"]="aspire"
print(thisdict)
if thisdict["model"]=="aspire":
    print("found")


# # ques7

# In[27]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
thisdict.pop("brand")
print(thisdict)


# # lab7

# In[1]:


thisset={"a","x","y"}
print(thisset)


# In[2]:


thisset={"a","x","y"}
print(thisset)
for i in thisset:
    print(i)


# In[3]:


thisset={"a","x","y"}
print("x" in thisset)


# In[4]:


thisset={"a","x","y"}
thisset.add("z")
print(thisset)


# In[5]:


thisset={"a","x","y"}
thisset.update(["p","q","r"])
print(thisset)


# In[6]:


print(len(thisset))


# In[7]:


thisset={"a","x","y"}
thisset.remove("y")
print(thisset)


# In[8]:


thisset={"a","x","y"}
thisset.discard("x")
print(thisset)


# # lab 7 questions

# In[9]:


thisdict={}
print(thisdict)


# In[10]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
for i in thisdict.values():
    print(i)


# In[11]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
thisdict.popitem()
thisdict.popitem()
thisdict.popitem()
print(thisdict)


# In[12]:


thisdict={"brand":"ford","model":"mustang","year":"2020"}
for i in thisdict.values():
    print(i)


# In[15]:


a={"band":"ford","model":"mustang","year":1964}
print(a)
for i in a :
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)


# # lab --

# In[ ]:


def mul(x,y):
    z=x*y
    return(z)

x=int(input("num1"))
y=int(input("num2"))
z=mul(x,y)
print(z)


# In[ ]:




