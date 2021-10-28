#!/usr/bin/env python
# coding: utf-8

# In[21]:


import mysql.connector as Connector
import pandas as pd
import numpy as np 
import matplotlib.pyplot as Mat


# In[22]:


Database = Connector.connect(host="localhost",user='root',password="00000000",database="project")


# In[23]:


print(Database)


# In[24]:


Project = Database.cursor()


# In[25]:


Project.execute("SELECT * from Users;")


# In[26]:


Output = Project.fetchall()


# In[27]:


DataFrame = pd.DataFrame(Output)


# In[28]:


DataFrame


# In[29]:


Gender = Database.cursor()


# In[30]:


Gender.execute("SELECT gender FROM USERS;")


# In[31]:


GenderDatabase = Gender.fetchall()


# In[32]:


DataGender = pd.DataFrame(GenderDatabase)


# In[33]:


DataGender


# In[34]:


M = DataGender[DataGender=="Male"]


# In[35]:


F = DataGender[DataGender=="Female"]


# In[36]:


VM = int(M.count())


# In[37]:


VF = int(F.count())


# In[38]:


VM


# In[39]:


VF


# In[40]:


expel = [0.1,0]
Mat.pie([VF,VM], labels=["Female","Male"], explode=expel, shadow=True, colors=["Red","Blue"])
Mat.title("Number of Males and Females:")
Mat.legend(loc="center right")
Mat.show()


# In[ ]:




