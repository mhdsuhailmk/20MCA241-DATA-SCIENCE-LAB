#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Q1 LIST TO SERIES CONVERSION

import pandas as pd
x = pd.Series(['APPLE', 'BANANA', 'ORANGE','GRAPES'])
print(x)


# In[28]:


#Q2 DATE SERIES

import pandas as pd

per1 = pd.date_range(start ='5-1-2021',
        end ='05-12-2021',freq ='24H')

for val in per1:
    print(pd.to_datetime(val).date())


# In[40]:


#Q3 DICT TO DATAFRAME

import pandas as pd
data = {'NAME': ['ELTON', 'GOUTHAM', 'JON', 'RON'],
        'AGE': ['25', '30', '28', '26']
       }
new = pd.DataFrame.from_dict(data)
new


# In[43]:


#Q4 2D LIST TO DATA FRAME

l1=[ ['ABC',30],['XYZ',20],['PQR',60],['OPT',42],['LMR',58] ]

df = pd.DataFrame(l1,columns=['TAG','NUMBER'])
df


# In[51]:


#Q5 CSV TO DATAFRAME

df = pd.read_csv('data.csv')
print(df.to_string())


# In[61]:


#Q6 DATAFRAME SORT

l1=[ ['ABC',30,'AA47'],['XYZ',20,'YR73'],['PQR',60,'QT46'],['PQR',42,'OP07'],['LMR',58,'LA32'] ]

df = pd.DataFrame(l1,columns=['TAG','NUMBER','CODE'])

df.sort_values(by=['TAG','CODE','NUMBER'])


# In[65]:


#Q7 DF CUSTOM INDEXING TO DEFUALT INDEXING

l1=[ ['ABC',30,'AA47'],['XYZ',20,'YR73'],['PQR',60,'QT46'],['PQR',42,'OP07'],['LMR',58,'LA32'] ]

df = pd.DataFrame(l1,columns=['TAG','NUMBER','CODE'])



df = df.reset_index(drop=True)
df


# In[67]:


#Q8 2 ROWS FROM DF
l1=[ ['ABC',30,'AA47'],['XYZ',20,'YR73'],['PQR',60,'QT46'],['PQR',42,'OP07'],['LMR',58,'LA32'] ]

df = pd.DataFrame(l1,columns=['TAG','NUMBER','CODE'])

df.head(2)


# In[77]:


#Q9 AVG SALARY 
l1=[ ['ALEX','DRT','45600'],['JOHN','DRT','42000'],['RAJ','MD','39850'],['KUMAR','SDE','30000'],['KOYA','SDE','32500'] ]

df = pd.DataFrame(l1,columns=['NAME','OCCUPATION','SALARY'])

df2=df["SALARY"].mean()

df2


# In[82]:


#Q10 FILL NaN VALUES
import numpy as np

nums = {'SET-1': [0, 1, 1, 2, 3, 5,np.nan,13, 21,np.nan],
'SET-2': [3, 7,np.nan, 23, 31, 41,np.nan, 59, 67,np.nan],
'SET-3': [2, 3,5,np.nan,11, 13, 17,19, 23,np.nan]}

df = pd.DataFrame(nums)

df = df.fillna(0)

df


# In[ ]:



