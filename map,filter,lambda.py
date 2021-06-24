#map, lambda statements
def square(num):
    return num ** 2
my_nums = [1,2,3,4,5]
for x in map(square,my_nums):     #the map function allows it to be used numerous times at once
    print(x)

# Luke i am your father example--using map to call all 3 at the same time
def relation_to_luke(name):
    if name == 'Darth Vader':
        return('Luke, I am your father')
    elif name == 'Leia':
        return('Luke, I am your sister')
    elif name == 'Han':
        return('Luke, I am your brother in law')
    else:
        return('Luke, I dont know you')
relation = ['Darth Vader', 'Leia', 'Han']
for item in map(relation_to_luke,relation):
    print(item)

#age(years) to days now using map to calculate numerous ages at once
def calc_age(x):
    days_old = x * 365
    return(days_old)
ages = [10,20,30]
for age in map(calc_age,ages):
    print(age)
#-------------
#lamba function you only use once...no need to def function to use it
#return the first letter
names_of_people =['Ross', 'Chelsea', 'Hallie', 'Bonnie']
list(map(lambda letter: letter[0],names_of_people))
#this would return ['R','C','H','B']
names_of_people =['Ross', 'Chelsea', 'Hallie', 'Bonnie']
list(map(lambda letter: letter[::-1],names_of_people))
#this would return ['ssoR','aeslehC','eillaH','einnoB']

#-------------------
#filter allows you to filter results
def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6,7,8,9,10]
for n in filter(check_even,mynums):     #the filter function will only return even numbers while if we used the map() it would return either true or false for all numbers in mynums
    print(n)