

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
makes_twenty(10,20)