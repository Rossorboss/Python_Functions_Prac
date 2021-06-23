#map, lambda statements
def square(num):
    return num ** 2
my_nums = [1,2,3,4,5]
for x in map(square,my_nums):     #the map function allows it to be used numerous times at once
    print(x)

# Luke i am your father example
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