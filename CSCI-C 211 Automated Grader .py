#!/usr/bin/env python
# coding: utf-8

# CSCI-C 211 Automated Grader  
# By: Alexander Mervar  
# https://github.com/alexandermervar  
#   
# The following code is for CSCI-C 211 grading at Indiana University.  
#   
# As you may notice, many rubrics have a line similar to "Grade: minimum of (points * .24) and 10"  
# The math involved can sometimes be a little repetitive and tedious  
# The program looks to speed up this process  
# Run program to begin user inputs  
#   
# Best Wishes :)
# 

# Example:  
# "Number of possible points: 47  
# Grade: minimum of (points * .24) and 10"  
#   
# Input Raw Max Points: 47  
# Input Point Multiplier: .24  

# In[9]:


maxFinalScore = 10

print('Welcome to the CSCI-C 211 Grader! \n Input the string "end" after the setup to end the task.')

maxPoints = int(input("Input Raw Max Points: "))

multiplier = float(input("Input Point Multiplier: "))

studentPoints = input("Input Total Raw Points the First Student Has Lost: ")

while studentPoints != "end":
    print("Score: " + str(min((maxPoints - int(studentPoints)) * multiplier, maxFinalScore)))
    studentPoints = input("Input Total Raw Points the Next Student Has Lost: ")
    
print()
print("Thank You!")

