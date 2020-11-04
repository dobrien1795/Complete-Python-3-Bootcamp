##This is for section 4 & 5 of the course

##-------------------------------##
#Section 4
'''#Equals sign
a = 2 == 4
print(a)
#Greater than or equal
b = 3 >= 1
print(b)'''

##-------------------------------##

'''#Multiple comparisons
#True
print(1 < 2 < 3)
#Flase
print(1 < 2 > 3)
#Use and
print(1 < 2 and 4 < 7)
#Use or
print(1 > 100 or 2 == 2)
#Not returns opposite boolean
print(not 1 ==1)'''

##-------------------------------##

#If & Loops

'''#If, elif, else
#White space and indentation is key for python conditions and loops
    if some_condtions:
        do something
    elif some_other_conditon:
        do something else
    else:
        do alternative

if 2 < 3:
    print("it's true")

hungry = 'Maybe'

if hungry == 'Yes':
    print('Feed me!')
elif hungry == 'Maybe':
    print('Give me a small bit of food')
else:
    print("I'm not hungry")'''

##-------------------------------##

#Loops
'''#For loop
my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num)

#Using conditions with loops
for num in my_list:
    if num % 2 == 0:
        print('Even number is: ' + str(num))
    else:
        print('Odd number is: ' + str(num))

#Tuple unpacking
my_list_t = [(1,2), (3,4), (5,6)]

for v in my_list_t:
    print(v)
#If you only want the first item of a tuple in a list
for a,b in my_list_t:
    print(a)

#Iterating through dictionaries
my_dict = {'k1':1, 'k2':2, 'k3':3}

#prints keys
for k in my_dict:
    print(k)
#prints values
for value in my_dict.values():
    print(value)'''

##-------------------------------##

#While loop
'''x = 0
while x < 5:
    print(f'x is: {x}')
    x = x + 1
else:
    print('x is not less than 5')

#Pass
#just allows you to do nothing.
# Mainly used as a placeholder so I can add something to it later
x = [1,2,3]
for item in x:
    pass
 
#Break
#exit out of loop if condition is met
mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)'''

##-------------------------------##

#Useful operatiors
'''#Range
#Just create a list of numbers to iterate through
#No need to create a list and store to memory
for num in range(0,10,3):
    print(num)

#Enumerate
#Allows you to count as well as iterate through stuff
word = 'abcde'
for index,letter in enumerate(word):
    print('Index number {} corresponds to letter {}'.format(index, letter))

#Zip
#This matches up lists
#Only zips the shortest list and ignores anything else
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d']
for item in zip(mylist1, mylist2):
    print(item)

#Output the zip as a list:
print(list(zip(mylist1, mylist2)))'''

'''#in
#just checks if some element is in a string/list/dict
a = 'x' in 'xyz'
print(a)

#Randint
#Generate random int in a range
from random import randint
x = randint(0,100)
print(x)

#User input
#Takes in values as strings
result = input('What is your name? ')
print(result)'''

'''#List comprehension
#If you want to assign a string to a list
mystring = 'hello'
mylist = [letter for letter in mystring]
print(mylist)

#Or if you want to manipulate data before saving to list
mylistnum = [num**2 for num in range(0,11)]
print(mylistnum)

#More complex use of list comprehension
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)'''

##-------------------------------##
