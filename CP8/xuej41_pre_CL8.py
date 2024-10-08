#!/usr/bin/env python
# coding: utf-8

# # ENG 1P13 - Computing 8 - The Object of the Exercise 
#   
#   ## CP 8 Pre-Assignment
#   
# Create a class called **Car**  with the requirements below.
# - Create an **\_\_init\_\_**(*make*,*model*,*year*) method that takes the following arguments as strings and stores them as instance variables: ***make, model, year***    
# - Create the **accessor** method *car_info*(): The method returns the string "The make of your car is a *<u>year</u>* *<u>make</u>*, and the model of your car is *<u>model</u>*."
# - Create two objects one for a Mercedes (make), GLA (model), 2020 (year) and the second object is for a Toyota (make), RAV4 (model), 2023 (year).
# 
# 
# 

# In[17]:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        return "The make of your car is a " + self.year + " " + self.make + " and the model of your car is "+ self.model +"."

car1 = Car("Mercedes", "GLA", "2020")
car2 = Car("Toyota", "RAV4", "2023")    


# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 8 Pre-Assigment dropbox on Avenue with the naming convention: **macID_pre_CL8.py**
# 
# **Make sure the final version of your file runs without errors, otherwise, you will likely receive zero.**

# In[ ]:




