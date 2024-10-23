#!/usr/bin/env python
# coding: utf-8

#  # ENG 1P13 - Computing 2 - Form Follows Function 
#   
#   ## CP 2 Pre-assignment Problem
# The requirements of the program are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks. You can choose to copy and paste the function names into the implementation cell to avoid spelling mistakes.

# Define a function **volume**(*l*, *w*, *h*): 
#   - ***l***: A number value of type *float*.
#   - ***w***: A number value of type *float*.
#   - ***h***: A number value of type *float*.
#   - **Return**: The volume of a pyramid. The volume can be calculated using the formula below.
# ![image.png](attachment:image.png)

# In[6]:


#********************************************
# Write your volume function below: (3 marks)
#********************************************
def volume(l, w, h):
    volume = (l * w * h)/3
    return volume


# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 2 Pre-Assigment dropbox on avenue with the naming convention: macID_pre_CL2.py
# 
# **Make sure the final version of your file runs without errors, otherwise, you will likely receive zero.**
