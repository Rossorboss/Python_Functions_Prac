#Reverse a list - this will only return a list
alist = [100, 200, 300 ,400, 500]
newlist = alist[::-1]
print(newlist)

#iterate 2 lists reverse 1 and print both results
list4=[10, 20, 30, 40, 50]     
list5=[100, 200, 300, 400, 500]
for x, y in zip(list4, list5[::-1]):
    print(x,y)
#will return
#10 500
#20 400
#30 300
#40 200
#50 500

#filter out empty strings in list
list6=['Mike', '', 'Emma', '', 'Kelly', '', 'Brad']  
reslist = list(filter(None, list6))
print(reslist)

#appending a set number to a set place in a list (7000 after 6000)
list7 = [10, 20, [300, 400, [5000, 6000],500], 30, 40]   
list7[2][2].append(7000)
print(list7)


#sublist to be added to a list (adding h,i,j after the g)
list8=['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']     
sublist = ['h', 'i', 'j']
list8[2][1][2].extend(sublist)
print(list8)

#replacing a certain number with another number when it appears in a list (20 for 200)
list9 = [5, 10, 15, 20, 25, 50 ,20]   
index = list9.index(20)
list9[index] = 200
print(list9)

