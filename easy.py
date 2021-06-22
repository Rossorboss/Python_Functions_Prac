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

#christmas eve
import datetime
def is_it_christmas_eve(datetime.date(year,month,day)):
    if date.month == 12 and date.date == 24:
        return True
        print('True')
    else:
        return False
        print(False)        
is_it_christmas_eve(datetime.date)
