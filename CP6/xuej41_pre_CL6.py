#!/usr/bin/env python
# coding: utf-8

# # ENG 1P13 - Computing 6 - Nesting and Testing
#   
#   ## CP 6 in-lab test 
#   
# 1. Define a function **max_int**(a,b,c):
#     - ***a***: an integer
#     - ***b***: an integer
#     - ***c***: an integer
#     - **Return**: The maximum number of the three integers using if-elif-else statements.

# In[12]:


def max_int(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Create test cases for this code to ensure it functions accordingly. 
# 
# Please comment out the test cases before submitting.

# In[21]:


#Normal test case:
#max_int(10,2,1)

#Boundary test case:
#max_int(3,2,1)
#max_int(3,3,1)
#max_int(2,3,3)
#max_int(-3,-2,-1)


# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 6 Pre-Assigment dropbox on avenue with the naming convention: macID_pre_CL6.py
# 
# **Make sure the final version of your file runs without errors, otherwise, you will likely receive zero.**

# In[ ]:




