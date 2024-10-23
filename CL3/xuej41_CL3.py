#!/usr/bin/env python
# coding: utf-8

# # Computing 3 Assignment
# 

# ---
# ## Background
# 
# Generating statistics from a set of data is a task that computers love. In this assignment, you will be implementing a grade processing system that will generate the mean and standard deviation for a set of final exam grades.
# 
# We will assume that final grades are stored in a list, where each entry in the list is a string with the following format:
# 
# <div align="center">
# "studentNum-finalGrade%"
# </div>
# 
# The string represents the final exam mark (*finalGrade*) that the student (*studentNum*) achieved. For example, the cell below contains a list of final exam marks from two students. Student **1007089** achieved a mark of **91%**, and student **1009989** achieved a mark of **77.5%**.
# 
# ```
# grades = ['1007089-91%','1009989-77.5%']
# ```
# 
# We want to calculate the mean final exam mark from a list of grades. If we assume that we have **N** grades, the mean **$\bar{x}$** can be calculated from the following formula:
# 
# 
# <br/>
# \begin{align}
#   \bar{x} = \frac{1}{N}\sum_{i=0}^{N-1} x_i \tag{1}
# \end{align}
# <br/>
# 
# The variable **$x_i$** represents each grade in our list at index i. We assume that we start counting at 0.
# 
# We also want to be able to calculate the standard deviation from a list of grades. The standard deviation measures the amount of variability in our data set. For example, let’s say we want to compute the average and standard deviation for the grades [80, 90, 70, 60]. The average of these grades is 75, and the standard deviation is 11.2. Now imagine we want to compute the average and standard deviation for the grades [80, 76 ,74, 70]. The average of these grades is 75, but the standard deviation is 3.6. Although both sets of grades have the same average, the second set has a smaller standard deviation. The reason is because the grades are not as “spread out” as the grades in the first set. The grades in the second set deviate from their average by a small amount.
# 
# The standard deviation $\sigma$ is calculated using our mean $\bar{x}$ and the following formula:
# 
# <br/>
# \begin{align}
#   \sigma = \sqrt{\frac{1}{N}\sum_{i=0}^{N-1} (x_i-\bar{x})^2} \tag{2}
# \end{align}
# <br/>
# 
# The requirements of the program are given below.
# 
# 
# 

# ---
# ## Program Requirements (12 Marks)
# 
# The requirements of the program are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks.
# 
# ### Part A (6 Marks) 
# 
# 1. Define a function **extract_grade**(*x*):
#   - ***x***: A *string* containing a student number and grade in the format "studentNum-Grade%"
#   - **Return**: The student's grade as a *float*. <br/> (*Hint: Use the **.split()** and **.strip()** methods*)
# 
# ### Part B (6 Marks) 
# 
# 1. Define a function **class_average**(*final_marks*):
#   - ***final_marks***: A *list* of strings, where each string is formatted as "studentNum-Grade%".
#   - **Return**: The mean grade of the grades in *final_marks* calculated using equation (1) outlined below.<br/>*(Hint: Use your **extract_grade** function and a for loop!)*
#   
# <br/>
# \begin{align}
#   \bar{x} = \frac{1}{N}\sum_{i=0}^{N-1} x_i \tag{1}
# \end{align}
# <br/>
# 
# 
# 2. Define a function **class_std_dev**(*final_marks*):
#   - ***final_marks***: A *list* of strings, where each string is formatted as "studentNum-Grade%".
#   - **Return**: The standard deviation of the grades in *final_marks* calculated using equation (2) outlined below.<br/>*(Hint: Use your **class_average** function and a for loop!)*
#   
# <br/>
# \begin{align}
#   \sigma = \sqrt{\frac{1}{N}\sum_{i=0}^{N-1} (x_i-\bar{x})^2} \tag{2}
# \end{align}
# <br/>

# ---
# ## Implementation
# Please define all functions in the cell below

# In[61]:


#DEFINE YOUR PART A FUNCTION BELOW:

#********************************************
# Write your extract_grade function below: (6 marks)
#********************************************

def extract_grade(x):
    grade = x.split("-")
    grade = float(grade[1].strip("%"))
    return grade

#DEFINE YOUR PART B FUNCTIONS BELOW: 

#********************************************
# Write your class_average function below: (3 marks)
#********************************************

def class_average(final_marks):
    global avg
    avg = 0
    for i in range(len(final_marks)):
        grade = final_marks[i]
        avg += float(extract_grade(grade))
    avg /= len(final_marks)
    return avg


#********************************************
# Write your class_std_dev function below: (3 marks)
#********************************************

def class_std_dev(final_marks):
    stddev = 0
    for i in range(len(final_marks)):
        grade = final_marks[i]
        stddev += (float(extract_grade(grade)) - avg)**2
    stddev /= (len(final_marks))
    stddev = stddev**0.5
    return stddev


# ---
# ## Testing
# 
# The cell below contains a main function that you can use to test your functions. 
# 
# ### Important
# Run the cell where you implemented your functions ***first*** and ensure it outputs with no errors. Then, run the cell below with the main function to verify that your code works correctly with the provided input. The following message should be printed after the main() function is run:
# 
# >*Final exam class average: 70.12 %<br/>
# >Final exam standard deviation: 32.27 %<br/>*
# 
# Note that your code is not necessarily correct if your output matches the expected output. Your code will be checked against multiple inputs for correctness. The cell below is **not** graded, so feel free to modify the code as you wish!

# In[63]:


def main():
    final_exam_grades = ["400123848-71%","1001425-99.5%","1009980-8.2%","1001480-84.0%","400199444-87.9%"]
    avg = class_average(final_exam_grades)
    std_dev = class_std_dev(final_exam_grades)
    print("Final exam class average:",round(avg,3),"%")
    print("Final exam standard deviation:",round(std_dev,3),"%")
main()


# ---
# ## Reflective Questions
# 
# 1. Assume that you always supply the correctly formatted input into your **class_average** and **class_std_dev** functions. That is, a list where entries are strings that follow the “studentNum-finalGrade%” format. Is there any input that can cause your program to fail?
# 
# 2. How would your code change if the string format was changed from “studentNum-finalGrade%” to “studentNum:finalGrade”? You do not need to implement this change but explain what needs to be modified. 
# 
# 3. Can you compute the average and standard deviation grade using a single for loop? Why or why not.
# 
# Please answer all questions in the cell below!

# ```
# 1. If the length of the list was 0, the program would fail because the for loop would not run. Other than that, any other input should be fine as the program is only taking the percentage mark which can only be between 0 and 100. The program should have no problem working with those numbers assuming everything is formatted correctly.
# 
# 2. I would need to change my Part A function that extracts the grade to split the string from ":" rather than "-". Everything else would remain the same.
# 
# 3. You can't because if you tried, you would calculate the average of only the first value and plug it into the standard deviation equation, then obtain the average of the first and second value and plug it into the std_dev equation again. You need a for loop that calculates the total average first then plugs it into the std_dev equation.
# 
# 
# ```

# ---
# ## Submission
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 3 dropbox on avenue with the naming convention: macID_CL3.py
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely receive zero.**
# 
# This assignment is due the day of your Lab section at the end of your lab.
# 
# Late labs will not be accepted
# 

# In[ ]:




