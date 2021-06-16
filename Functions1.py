Functions

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
