#This file contains most of the basic graphs that we can use for analysis using matplotlib
#!/usr/bin/env python
# coding: utf-8

# In[14]:


from matplotlib import pyplot as plt
from matplotlib import style


# In[7]:


#Simple Graph
plt.plot([1,2,3],[4,5,1])


# In[10]:


#Labeled Graph
x=[4,5,6]
y=[12,6,6]
plt.plot(x,y)
plt.title('Info')
plt.xlabel('X')
plt.ylabel('Y')


# In[15]:


#with legends simple graph
X1 = [4,5,6]
Y1 = [12,7,8]
X2 = [6,9,1]
Y2 = [6,15,6]
plt.plot(X1,Y1,'g',label = 'Line 1',linewidth = 5)
plt.plot(X2,Y2,'r',label =  'Line 2', linewidth = 5)
plt.title('Info')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid(True,color = 'k')


# In[20]:


#Bar Graph
X1 = [4,5,6]
Y1 = [12,7,8]
X2 = [1,2,3]
Y2 = [4,5,6]
plt.bar(X1,Y1,label = "Example 1", color = 'r')
plt.bar(X2,Y2,label = 'Example 2', color = 'g')
plt.legend()
plt.title('Bar Graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')


# In[31]:


#Histogram
Score = [2,3,4]
bins = [0,1,2,3,4]
plt.hist(Score,bins,histtype = 'bar', rwidth = 0.8)
plt.title('Hisstogram')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()


# In[34]:


#ScatterPlot
X=[2,3,4,6,7,8,9]
Y=[5,2,3,1,4,6,7]
plt.scatter(X,Y,label = 'skitscat',color = 'r')
plt.title('Scatter Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()


# In[38]:


#Pie Chart
slices = [7,2,3,12]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
plt.pie(slices,
        labels = activities,
        colors = cols,
        startangle = 90,
        shadow = True,
        explode = (0,0.1,0,0),
        autopct = '%1.1f%%'
)
plt.title('Pie Plot')

