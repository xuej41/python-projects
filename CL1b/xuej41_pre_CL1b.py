#!/usr/bin/env python
# coding: utf-8

#   # ENG 1P13 - Computing 1B - Trial and Errors
#   
#   ## CP 1B in-lab test 
# 2. Find the distance between lines $y_{1}$ and $y_{2}$
# 
#     $y_{1}$ = -4x+8 <br>
#     $y_{2}$ = -4x+9
#     ![image-2.png](attachment:image-2.png)
#     where $C_{n}$ is the y-intercept in each line and $m$ is the slope  

# In[18]:


import math

c2 = 9
c1 = 8
m = -4

d = (math.fabs(c2 - c1))/(math.sqrt(1 + m**2))

print(d)


# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 1b Pre-Assigment dropbox on avenue with the naming convention: macID_pre_CL1b.py
# 
# **Make sure the final version of your file runs without errors, otherwise, you will likely receive zero.**

# In[ ]:




