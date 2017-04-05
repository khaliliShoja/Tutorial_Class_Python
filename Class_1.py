
# coding: utf-8

# In[108]:

class Employee:
    pass


emp_1=Employee()
emp_2=Employee()
print (emp_1)
print (emp_2)

emp_1.first="A"
emp_1.last="B"
emp_1.email="A.B@gmail.com"
emp_1.pay=7000




emp_2.first="C"
emp_2.last="D"
emp_2.email="C.D@gmail.com"
emp_2.pay=7000



print(emp_1.email)
print(emp_2.email)


# In[109]:


class Employee:
    def __init__(self, first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+"@gmail.com"
 
        
        
    def fullname(self):
        return "The name is: {} and the family is: {}".format(self.first,self.last)
emp_1=Employee("A","B",5000)
print(emp_1.first)

print("The name is: {} and the family is: {}".format(emp_1.first,emp_1.last))
print(emp_1.fullname())



print(Employee.fullname(emp_1))


# In[110]:


class Employee:
 raise_amount=1.04
 def __init__(self, first,last,pay):
     self.first=first
     self.last=last
     self.pay=pay
     self.email=first+'.'+last+"@gmail.com"
 
     
     
 def fullname(self):
     return "The name is: {} and the family is: {}".format(self.first,self.last)     
     
 def apply_raise(self):
     self.pay= self.pay*self.raise_amount
     
     
emp_1=Employee("A","B",5000)   
print(emp_1.pay) 
emp_1.apply_raise()
print(emp_1.pay) 


# In[111]:


print(emp_1.__dict__)   
     
  


# In[112]:

print(Employee.raise_amount)
print(emp_1.raise_amount) 


# In[113]:

print(emp_1.__dict__) 


# In[114]:

print(Employee.__dict__)  


# In[115]:

Employee.raise_amount=1.06  


# In[116]:

print(Employee.raise_amount)
print(emp_1.raise_amount) 


# In[117]:

print(Employee.__dict__)  

print(emp_1.__dict__)    


# In[118]:


emp_1.raise_amount=1.08  

print(emp_1.__dict__)   


# In[ ]:



