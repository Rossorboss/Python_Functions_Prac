

def lesser_of_two_evens(a,b):     #A function that will retun the lesser of 2 numbers if both are even and the greater if both are odd
    if a%2 == 0 and b%2 == 0:     
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    print(result)
lesser_of_two_evens(5,7)  #this will return 7 this will return 7 as its lower and they are both 
lesser_of_two_evens(2,4)  #this will return 2 as its lower and they are both even

#Animal Crackers- Take a 2 word string and print True if both words being with the same letter

def animal_crackers(text):
    wordlist = text.split()
    word1 = wordlist[0][0]
    word2 = wordlist[1][0]
    if word1 == word2:
        print('True')  

animal_crackers('Levelheaded Lama') #This will print True
animal_crackers('Levelheaded Ama') #this wont print anything

#Makes 20. given 2 int return True if the sum is 20,or if 1 of the int is 20 if not retun false
def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 ==20:
        return True
    else:
        return False
makes_twenty(10,20)    #this will show True

#Old Macdonald, write a function that capitalizes the first and 4th letters
def old_macdonald(name):
    first_word = name[:1]
    second_word = name[1:3]
    third_word = name[3:]
    full_capital_name = first_word.capitalize() + second_word + third_word.capitalize()
    print(full_capital_name)
old_macdonald('macdonald')  #this wil show MacDonald

#Master Yoda- given a sentence, return a sentence with the words reversed
def master_yoda(text):
    sentence = text.split()
    reverse_word_list = sentence[::-1]
    (reverse_word_list) = ' '.join(reverse_word_list)   # ' '.join changes the list into a string with whatever is inside the () 
    print(reverse_word_list)
master_yoda('I am home')    #this will show- home am I

#Almost There- given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    (abs(100-10) <= 10) or (abs(200-n) <= 10)
    print('True')
almost_there(91)   #this will return true as it is less than 10

#Find 33 - given a list of ints, True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
    for i in range(0,len(nums)-1):      #this will ensue it doesnt error at the end of the listing looking for the next number
        if nums[i] ==3 and nums[i+1] ==3:
            return True
    return False
has_33([1, 1, 3, 3])   #this will return True

#Paper Dolls- Given a string return a string where for every character in the original there are three characters 
def paper_dolls(text):
    result = ''                   # adding empty string, 
    for char in text:               
        result += char * 3          #adding character *3 everytime
    print(result) 
paper_dolls('hello')

#Blackjack- given 3 integers between 1-11, if their sum is less than or equal to 21 return their sum, if their sum exceeds 21 and theres and 11 reduce the total sum by 10, if the sum stil exceeds 21 then return bust
def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:     #sum of abc is less than or equal to 21 return sum
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])-10 <= 21:     #if 11 is in abc, and the sum of abc -10 for the 11 is less than or equal to 21
        return sum([a,b,c])-10                         # returns the sum of abc -10 for the 11
    else:
        return "Bust"

#summer of 69- Print the sum of the numbers in the 'array', except ignore sections of the numbers starting with a 6 and extending all the way to the next 9. Return 0 for no numbers
def summer_69(arr):
    total = 0
    add = True
    for num in arr:            #this first loop will tell it to add if the number is not =6, it will then break the loop at 6
        while add:
            if num!= 6:
                total += num
                break
            else:                     
                add = False 
        while not add:            #as the numbers at not = 9 it will continue to not add untill it hits 9 then it will break
            if num!= 9:
                break
            else:                 #it will then contiune to add
                add = True
                break
    print(total)
summer_69([2, 1, 6, 9, 11])     #this will return 14    2+1 break 6 and 9 then + 11

#List of numbers - print the list of numbers and returning True or Flase if the first and last number match

def list_of_numbers(nums):          
    print('Given list is',nums)
    if nums[0] == nums[-1]:
        return True
    else:
        return False
list_of_numbers([10, 20, 30, 40, 20])
#This will return =  Given list is [10, 20, 30, 40, 20] (and return False)

#Divisable by 5, this will return 'Divisable by 5' and then list the numbers from the list that are divisable by 5
def divisable_by_five(numlist):
    print('Divisable of 5 in a list')
    for num in numlist:
        if (num %5 == 0):
            print(num)

divisable_by_five(10, 20 , 36, 41, 50)
#Divisable of 5 in a list
#10
#20
#50

#Print first 10 numbers
i = 0
while i <= 10:
    print(i)
    i += 1

#Print Number triangle pattern
lastnumber=7
for row in range(1, lastnumber):
    for column in range(1, row +1):
        print(column, end=' ')
    print('')
#1
#12
#123
#1234
#12345
#123456

#Multiplication Table
def multiplication_table(x):
    for i in range(1, 13,):     #thiis will return the multiplication table of x up untill x12 e.g 9x12
        product = x*i
        print(product)

multiplication_table(9)       #9 times table

