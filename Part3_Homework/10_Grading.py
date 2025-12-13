# You are tasked with creating a simple grading system for a class. 
# Write a Python program that takes a student's score as input
#  and calculates and prints its corresponding letter grade based on the following grading scale:

# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
number = int(input('Type in your grade:'))
if number>=90:
   print('A')
elif number>=80<=89:
   print('B')
elif number>=70<=79:
   print('C')
elif number>=60<=69:
   print('D')
else:
   print('F')