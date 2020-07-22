#!/usr/bin/env python
# coding: utf-8

# # sum of n number using while loop

# In[ ]:


sum1=0
num=int(input("enter th value of n-"))
while num>0:
    sum1=sum1+num
    num=num-1
    
print("final sum->",sum1)


# # prime no or not

# In[ ]:


num=int(input("enter the number"))
if num>1:
    for i in range(2,num-1):
        if(num%i)==0:
            print(num,"not prime number")
            break
        else:
            print(num,"is prime number")
else:
    print("number is not prime number")

