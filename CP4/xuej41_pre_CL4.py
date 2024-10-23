#!/usr/bin/env python
# coding: utf-8

# # ENG 1P13 - Computing 4 - The Moment of Truth 
#   
#   ## CP 4 Pre-assignment Problem
# 1. Define a function that takes two float numbers and an operator (either +, -, *, /) as inputs and performs the calculation. 
# 
# 
#  Define a function **calculator**(*num1, num2, operator*):
#    - ***num1***: The first number of type *float*.
#    - ***num2***: The second number of type *float*.
#    - ***operator***: A string containing an operator character (+, -, *, /)
#    - **Return**: the variable *res* which is the result of the operation.

# In[6]:


def calculator(num1, num2, operator):
    res = 0
    if operator == "+":
        res = num1 + num2
    elif operator == "-":
        res = num1 - num2
    elif operator == "*":
        res = num1 * num2
    else:
        res = num1 / num2
    return res


# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 4 Pre-Assigment dropbox on avenue with the naming convention: macID_pre_CL4.py
# 
# **Make sure the final version of your file runs without errors, otherwise, you will likely receive zero.**

# In[ ]:




