#Section 6

##----------------------------##

'''#Methods and Objects
#List is an object
mylist = [1,2,3]
#Append is a method
mylist.append(5)
print(mylist)
help(mylist.insert)'''

#Functions
'''def say_hello(name):
    print('Hello {arg}'.format(arg=name))
#Function with default value
def say_hello1(name='Default'):
    print('Hello {arg}'.format(arg=name))

say_hello1()'''

#Return placement
'''def check_even(number_list):
    #Returns True if there is an even number
    #Returns False if ther is no even number
    for num in number_list:
        if num % 2 ==0:
            return True
        else:
            pass
    return False

print(check_even([13, 12, 17]))'''


##----------------------------##

#Tuple unpacking with function
'''work_hours = [('Abbie',100), ('Billy',400),('Cassie',800)]

def employee_of_month(work_hours):

    max_hrs = 0
    best_employee = ''

    for employee,hrs in work_hours:
        if hrs > max_hrs:
            max_hrs = hrs
            best_employee = employee
        else:
            pass
    return(employee,max_hrs)

print(employee_of_month(work_hours))'''

##----------------------------##

'''#Count number of prime numbers up to and including given input number
#Given 0 & 1 are not prime
def count_primes(num):

    #Check for 0/1 input
    if num < 2:
        return 0

    #2 is a prime so can add that straight away
    #2 is a prime
    primes = [2]

    #Counter
    x = 3
    while x <= num:
        #Go all the way up to num in steps of 2 as ever even number is not prime
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)

print(count_primes(100))'''

##----------------------------##

#Lambda & map functions
#Map function
'''def square(num):
    return num**2

my_nums = [1,2,3,4,5]

#Map a function to each individual element of the list
for item in map(square,my_nums):
    print(item)

#return a list of the map results
sq_list = list(map(square,my_nums))
print(sq_list)'''

#Filter function
'''#Only returns values that are True in a function
def check_even(num):
    return num % 2 == 0

my_nums = [1,2,3,4,5,6]
eve_list = list(filter(check_even,my_nums))
print(eve_list)'''

#Lambda function
'''#One time function
square = lambda num: num ** 2
print(square(5))

my_nums = [1,2,3,4,5,6]
k = list(map(lambda num: num**2, my_nums))
print(k)'''

##----------------------------##

#Nested statements and scope
#Assigning variables and knowing where they can be viewed from
#And when you see errors like aariable not defined


##----------------------------##