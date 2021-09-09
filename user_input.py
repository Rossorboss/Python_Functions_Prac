def user_name():       #for a 1st name all only letters of the alphabet, less than 20 letters
    First_name = "11"
    length_of_name= False

    while First_name.isalpha() == False or length_of_name== False:
        First_name = input('Please enter your first name here (a-z): ')
        if First_name.isalpha() == False:
                print('Ensure you name contains only letters of the alphabet')
        if First_name.isalpha() == True:
            if len(First_name) <20:
                length_of_name = True
            if len(First_name) >20:
                print('Please shorten your name')
                length_of_name = False
                
    return First_name

def user_choice():
    choice = 'WRONG' #this can be anything as long as it is not an int - for is digit 
    acceptable_range = range(0,10)
    within_range = False 
    
    #Two conditions to check
    #Digit or within_range ==False 
    
    while choice.isdigit() == False or within_range == False:
        choice = input("Please pick a number (0-10): ")
        #Digit check
        if choice.isdigit() == False:
            print("Sorry that is not a digit")
        #Range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry you are out of acceptable range")
                within_range = False
    return int(choice)