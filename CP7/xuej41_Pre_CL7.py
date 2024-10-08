#!/usr/bin/env python
# coding: utf-8

# # ENG 1P13 - Computing 7 - Exceptional Algorithm Design 
#   
#   ## CP 7 Pre-Assignment

# 1. Rewrite the following code to handle a TypeError where the number is inputted as a string instead of an integer. 
# 
# 
# <img src="attachment:image-4.png" 
#      align="left" 
#      width="300" />

# In[1]:


def addition(number):
    try:
        sum = number + 18
        print("Sum is equal to", sum)
    except TypeError:
        print("Number must be inputted as an integer")


# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 7 Pre-Assigment dropbox on avenue with the naming convention: macID_Pre_CL7.py
# 
# **Make sure the final version of your file runs without errors, otherwise, you will likely receive zero.**
