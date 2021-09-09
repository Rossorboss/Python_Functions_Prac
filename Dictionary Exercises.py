#Convert 2 lists into a dictionary 
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
sampleDict = dict(zip(keys, values))

print(sampleDict)

#merge 2 python dictionaries into one  
#python 3.5 +
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}

print(dict3)

#other versions
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
 
#Delete set of keys from a dic.
sampleDict = {
    'name': 'Kelly',
    'age':25,
    'salary': 8000,
    'city': 'New york'
}
keystoremove = ['name', 'salary'] 
sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keystoremove}
print(sampleDict)

#check if a value (200) exists in a dictionary 
sampleDict1 = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict1.values())   #This will return True

#rename key (city) t0 (location) in the following dictionary 
