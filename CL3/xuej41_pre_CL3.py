#!/usr/bin/env python
# coding: utf-8

# # ENG 1P13 - Computing 3 - In the Loop 
#   
#   ## CP3 Pre-assignment Problem
# The requirements of the program are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks. You can choose to copy and paste the function names into the implementation cell to avoid spelling mistakes.

# Unlike the Fibonacci sequence, Lucas sequence start at 2,1,3,4,7,...
#   The pattern is as follows: <br>
#   $L_{0}$= 2, $L_{1}$= 1, $L_{2}$= 3, $L_{3}$= 4, ..., $L_{n}$= $L_{n-2}$+$L_{n-1}$
#   
#   Define a function **lucas_seq**(*n*): 
#   - ***n***: A number value of type *int*.
#   - **Return**: the variable *lucas* which is a list of the first n terms of the Lucas squence.

# In[27]:


#********************************************
# Write your lucas_seq function below: (3 marks)
#********************************************

def lucas_seq(n):
    lucas = [2, 1]
    for i in range(2, n):
        lucas.append(lucas[i-1] + lucas[i-2])
    return lucas

lucas_seq(10)


# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 3 Pre-Assigment dropbox on avenue with the naming convention: macID_pre_CL3.py
# 
# **Make sure the final version of your file runs without errors, otherwise, you will likely receive zero.**

# In[ ]:




