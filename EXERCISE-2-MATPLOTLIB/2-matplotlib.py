#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
#DRAW LINE

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 18, 45 ])
ypoints = np.array([3, 10, 12, 20,32 ])

plt.plot(xpoints, ypoints ,'o:r', mec = 'g',mfc = 'g')
plt.show()


# In[2]:


#Q2
#PLOT

xpoints = np.array([12,14,16,18,20,22,24])
ypoints = np.array([100,200,250,400,300,450,500])

plt.plot(xpoints, ypoints ,'o:r', mec = 'g',mfc = 'b')
plt.xlabel("Temperature in degree Celsius")
plt.ylabel("Sales")
plt.show()


# In[12]:


#Q3
#LINE USING VALUES TAKEN FROM TEXT FILE
import csv
x=[]
y=[]
with open('file1.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for r in plots:
        x.append(int(r[0]))
        y.append(int(r[1]))
plt.plot(x, y)
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
# Set a title 
plt.title('Graph')
plt.show()


# In[4]:


#Q4
#TWO LINES ON THE SAME PLOT
x1 = [5,10,20]
y1 = [10,20,30]
plt.plot(x1, y1, label = "LINE 1")

x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label = "LINE 2")
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.title('TWO LINES ON THE SAME PLOT')
plt.legend()
plt.show()


# In[47]:


#Q5
#MULTIPLE PLOTS

fig = plt.figure()
x = range(5)
y = range(5)

#1st plot
plt.subplot(2, 2, 1)
plt.plot(x, y, linestyle='dashed', color='y')

#2nd plot
plt.subplot(2, 2, 2)
plt.plot(x, y, linestyle='dashdot', color='blue')

#3rd plot
plt.subplot(2, 2, 3)
plt.plot(x, y, linestyle='solid', color='green')

#4th plot
plt.subplot(2, 2, 4)
plt.plot(x, y, linestyle='dotted', color='k')

plt.suptitle('MULTIPLE PLOTS')
plt.tight_layout()
plt.show()


# In[15]:


#Q6
#BAR CHART
x = ['JAVA', 'PYTHON', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 77, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='black')

plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("POPULARITY OF PROGRAMMING LANGUAGES\n" )
plt.xticks(x_pos, x)
plt.show()


# In[16]:


#HORIZONTAL BARCHART

x = ['JAVA', 'PYTHON', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 77, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='black')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("P0PULARITY OF PROGRAMMING LANGUAGES\n")
plt.yticks(x_pos, x)
plt.show()


# In[17]:


#BAR CHART WITH DIFF COLORS

x = ['JAVA', 'PYTHON', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 77, 6.7]
x_pos = [i for i, _ in enumerate(x)]
c = ['black', 'yellow', 'green', 'blue', 'orange','red']
plt.bar(x_pos, popularity, edgecolor='blue',color = c)

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("POPULARITY OF PROGRAMMING LANGUAGES")
plt.xticks(x_pos, x)
plt.show()


# In[9]:


#Q7
#BAR PLOT

n_groups = 5
men_means = (22, 30, 35, 30, 26)
women_means = (25, 32, 30, 35, 29)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, men_means, bar_width,
alpha=opacity,
color='r',
label='MEN')

rects2 = plt.bar(index + bar_width, women_means, bar_width,
alpha=opacity,
color='b',
label='WOMEN')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('SCORES BY PERSON')
plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()

plt.tight_layout()
plt.show()


# In[18]:


#Q8
#PIE CHART

languages = 'JAVA', 'PYTHON', 'PHP', 'JAVASCRIPT', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 77, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0, 0,0,0)  
# plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


# In[20]:


#Q9
#PIE CHART

import pandas as pd
df =  pd.read_csv('medal.csv')
country_data = df["country"]
medal_data = df["gold_medal"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)  
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("GOLD MEDAL")
plt.show()


# In[27]:


#Q10
#SCATTER PLOT

import pandas as pd
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range, math_marks, label='MATHS', color='r')
plt.scatter(marks_range, science_marks, label='SCIENCE', color='b')
plt.title('SCATTER PLOT')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()


# In[28]:





# In[ ]:



