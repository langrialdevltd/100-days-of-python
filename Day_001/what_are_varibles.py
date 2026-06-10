"""
Rules of naming variables
1. Make sure your variable names are descriptive
2. Don't have spaces between words
3. Don't start with numbers
4. Don't use special words like print or input
5. Choose simple words that are less likely to become typos
6. Check the company style guidelines if you start work at a company
"""
from operator import length_hint

input("what is your name")
# change the above statement and assign it to a variable
name = input("what is your name")
print(name)

# the len function very useful while trying to know the number of characters the user has input
print(len(name))

user_name = input("what is your name")
length = len(user_name)
print(user_name)
print(length)