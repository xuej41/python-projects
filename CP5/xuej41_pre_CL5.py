#!/usr/bin/env python
# coding: utf-8

# # ENG 1P13 - Computing 5 - In and Out 
#   
#   ## CP 5 in-lab test
#  
# 1. Define a function that writes to a file: <br>
# ```This student's name is XXXXX``` <br>
# ```This student's MACID is YYYYY``` <br>
# (where XXXXX is your name and YYYYY is your MACID)
# 
#   Define a function **writeFile**(*file_name*,*name*,*mac_id*):
#   
#    - ***file_name***: A string containing the name of the file, including its file extension.
#    - ***name*** A string containing user *name*.
#    - ***mac_id***: A tring containing user *mac_id*.
#    - **Return**: The variable *text* which is a string containing the text written to the file.

# In[ ]:


def writeFile(file_name,name,mac_id):
    file = open(file_name, "w")
    text = file.write("This student's name is "+ name + "\n" + "This student's MACID is " + mac_id)
    file.close()
    return text


#  2. Define a function that reads the text from a file (the text from the file you wrote in 1.) and prints it.
#  
#   Define a function **readFile**(*file_name*):
#    - ***file_name***: A string containing the name of the file, including its file extension <br> (You can test your code with the text file from the previous function).
#    - **Return**: The variable *text* which is a string containing the text read from the file.

# In[ ]:


def readFile(file_name):
    file = open(file_name, "r")
    text = file.read()
    file.close()
    return text


# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 5 Pre-Assigment dropbox on avenue with the naming convention: macID_pre_CL5.py
# 
# **Make sure the final version of your file runs without errors, otherwise, you will likely receive zero.**

# In[ ]:





# In[ ]:




