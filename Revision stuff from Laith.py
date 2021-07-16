import random

def couples():
    couples_list = [['x1', 'y1'],['x2', 'y2'],['x3', 'y3'],['x4', 'y4'],['x5', 'y5']]
    random.shuffle(couples_list)
    list1 = couples_list
    print('Christmas Draw for 2021 is as follows')
    print(f'{list1[0][0]} and {list1[1][1]} buy for each other')
    print(f'{list1[0][1]} and {list1[2][0]} buy for each other')
    print(f'{list1[1][0]} and {list1[2][1]} buy for each other')
    print(f'{list1[3][0]} and {list1[4][0]} buy for each other')
    print(f'{list1[3][1]} and {list1[4][1]} buy for each other')
    print('                                                   ')
    print('                                                   ')
    print('                                                   ')
    print('The Chritmas draw for 2022 is as follows') 
    print(f'{list1[0][0]} and {list1[4][0]} buy for each other')
    print(f'{list1[0][1]} and {list1[1][0]} buy for each other')
    print(f'{list1[1][1]} and {list1[4][1]} buy for each other')
    print(f'{list1[2][0]} and {list1[3][1]} buy for each other')
    print(f'{list1[2][1]} and {list1[3][0]} buy for each other')
 
                                                                    
couples()
