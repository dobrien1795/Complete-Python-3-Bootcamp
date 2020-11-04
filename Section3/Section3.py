#Python file to run section 3 code

#-----------------------------#
'''
#Python Numbers
print(2+1)
#Remainder/mod
print(7%4)
#Check if even/odd
print(20%2)
#Powers
print(2**3)
'''
#-----------------------------#

#Variable assignment
#Can't use symbols in a varaible name. e.g. :",<>/?|...

#Keep variable names lowercase

'''
x = 'Donal'
print(x)
a = 5.1
print(type(a))

my_income = 100000
my_tax = 0.1
my_tax_pay = my_income*my_tax
print(my_tax_pay)
'''
#-----------------------------#

#Strings

#Indexing gets a specific character of a string - []
#Indexing starts at 0. You can go reverse index by starting at -1
#slicing is a section of indexing [start:stop:step]

'''#Apostrophe
a = "I'm Donal"
print(a)
#Tab
b = 'hello \tworld'
print(b)
#Length
print(len(b))
#Slicing and step through string
mystring='abcdefghik'
print(mystring[2:])
print(mystring[:3])
print(mystring[::3])
#Reverse string
print(mystring[::-1])

#Concatenation
c = 'Hello World'
d = ' it is beatuiful outside'
print(c + d)
#Concatenation with .format() method
e = 'This is my {} string with {}'.format('format', 'concatenation')
print(e)
e = 'The {2} {1} {0}'.format('fox', 'brown', 'quick')
e = 'The {q} {b} {f}'.format(f='fox', b='brown', q='quick')
print(e)
#Formatting with decimal places
#Format is as follows {value:width.precision f}
result = 0.234565489
print('The result is {r:1.4f}'.format(r=result))
#F string
name = 'Donal'
print(f'Hello my name is {name}')

#Uppercase all values of a string
c = c.upper()
print(c)'''

#-----------------------------#

#Lists
'''
my_list = [1,2,3]
print(my_list)
#add to end of list
my_list.append('appended_value')
print(my_list)
popped = my_list.pop()
print(popped)
#.sort() is in place, so you can't assign it to another list
my_list.sort()
my_sorted_list = my_list
print(my_sorted_list)
'''
#-----------------------------#

#Dictionaries
'''
my_dict = {'apple':2.99, 'pear':1.99, 'orange':[.69,1.29]}
print(my_dict['orange'][1])
#add new value to dict
my_dict['milk'] = 3.00
print(my_dict)
'''

#-----------------------------#

#Input/Output of files
#Read as one string
my_file = open('myfile.txt')
print(my_file.read())
#if you want to read again, you have to reset the curser
my_file.seek(0)
my_file.read()
#Read each line separately
my_file.readlines()
my_file.close()

#Open and close in the one
#Modes are: r=read, w=write, a=append
with open('myfile.txt', mode='r') as my_file:
    contents = my_file.readlines()

with open('myfile.txt', mode='a') as a:
    a.write('\nNew appended line')

with open('myfile.txt', mode='r') as my_file:
    contents = my_file.readlines()
print(contents)
#-----------------------------#