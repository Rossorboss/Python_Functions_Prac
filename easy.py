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

