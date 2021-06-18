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