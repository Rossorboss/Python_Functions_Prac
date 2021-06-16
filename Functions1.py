

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