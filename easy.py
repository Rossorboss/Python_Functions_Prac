#luke i am your father
def relation_to_luke(name):
    if name == 'Darth Vader':
        print('Luke, I am your father')
    elif name == 'Leia':
        print('Luke, I am your sister')
    elif name == 'Han':
        print('Luke, I am your brother in law')
    else:
        print('Luke, I dont know you')
relation_to_luke('Leia')

#luke i am your father as a dictionary
def dic_relation_to_luke(name):
    print('Luke, I am your ' + {'Darth Vader': 'father.','Leia': 'sister.','Han': 'brother in law.'} [name])
dic_relation_to_luke('Leia')

#find the discount- takes 2 arguments the original price and the discount % as integers and returns the final price after the discount
def dis(x,y):
    price = x
    discount = y
    money_off = (discount * price) / 100.0
    final_price = price - money_off
    print(final_price)
dis(50,50)

#Basic Calculator
def calculator(x,y,z):
    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '/' and z == 0:
        print('Cant divide by 0')
    elif y == '/':
        print(x / z)
    elif y == '*':
        print(x * z)
calculator(10,'/', 0)

#Default Mood- Takesd a current mood and returns a sentence in the following format. 'Today i am feeling [mood]' if no argument is passed then retun Today i am feeling neutral
def mood_today(mood= 'neutral'):   #This sets the default as neutral so if no argument is passed then it defaults to this
    print(f'Today I am feeling {mood}')
mood_today('Happy')

#takes a list and returns a new list with unique elements taken away
def unique_nums(lst):
    seen_number = []
    for number in lst:
        if number not in seen_number:
            seen_number.append(number)
    print(seen_number)

#^^^^using a set def unique_set_nums(lst):
    return list(set(lst))

#function to multiply all numbers in a list
import math
def multiply(numbers):
    total = math.prod(numbers)
    print(total)

#function that checks if a word is a palindrome
def palindrome(s):
    s = s.replace(' ','')      #removes the spaces
    if s == s[::-1]:
        print(f'{s} is a palindrome')
    else:
        print(f'{s} is not a palindrome')

#write a function to check whether a string si a pangram or not (every letter of the alphabet)
import string

#string.ascii_lowercase   -- will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’.
def ispanagram(strng1, alphabet=string.ascii_lowercase):
    #create a set of the alphabet
    alphaset = set(alphabet) 
    #remove the spaces in user input (strng1)
    strng1 = strng1.replace(' ','')
    #convert user input (strng1) into lowercase
    strng1 = strng1.lower()
    #grab all the letters from the user input (strng1)
    strng1 = set(strng1)
    #alphaset == strng1 (string input)
    return strng1 == alphaset

