
#print twinkle twinkle to a set format
print('Twinkle, twinkle, little star \n\t How i wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\n Twinkle Twinkle little star,\n\tHow i wonder what you are!')
#Twinkle, twinkle, little star
 #        How i wonder what you are!
  #              Up above the world so high,
   #             Like a diamond in the sky.
 #Twinkle Twinkle little star,
  #      How i wonder what you are!

#Python programme to get the python version i am using
import sys
print('Python version')
print(sys.version)
print('Version.info.')
print(sys.version_info)

#fucntion to return the sum of 2 numbers
def sum_of_nums(x,y):
    total = x + y
    print(total)
sum_of_nums(10,5)

#return the next number from the last
def next_num(x):
    nextnumber = x + 1
    return nextnumber
next_num(10)

#mins to seconds
def mins(num):
    seconds = num * 60
    return seconds
mins(2)

#Area of a triangle base x height / 2

def tri_area(a,b):
    area = (a * b ) / 2
    print(area)
tri_area(10,5)

#Hours to seconds
def hours_seconds(x):
    minutes = x * 60
    seconds = minutes * 60
    print(seconds)
hours_seconds(1)

#maximum edge of a triange
def next_edge(x,y):
    last_edge = (x + y) -1
    print(last_edge)
next_edge(10,10)

#return the remainder of 2 numbers
def remainder(x,y):
    left_over = x % y 
    print(left_over)
remainder(7,2)

#String as an int.
def string_int(x):
    y = int(x)
    print(y)
string_int('10')

#age(years) to days
def calc_age(x):
    days_old = x * 365
    print(days_old)
calc_age(2)

#perimeter of a recatangle
def find_perimeter(x,y):
    perimeter = (x * 2) + (y * 2)
    print(perimeter)
find_perimeter(20,10)

#power calculator power(p) = Current (I) x voltage (V)
def circuit_power(i,v):
    watts= i * v
    print(watts)
circuit_power(480,20)