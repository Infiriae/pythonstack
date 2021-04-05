x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

print(x)
print(students)
print(sports_directory)
print(z)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(arra):
    output = ''
    for x in range(len(arra)):
        output+="\n"
        for key in arra[x].items():
            for z in range(len(key)):
                if z == len(key)-1:
                    output+= key[z] + ", "
                else:
                    #print(key[z])
                    output+= key[z] + " - "
    return output

opa = iterateDictionary(students)
print(opa)

def iterateDictionary2(kn,sl):
    for x in range(len(sl)):
        for key in sl[x]:
            if key == kn:
                print(sl[x][key])


iterateDictionary2('last_name',students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictb):
    for key in dictb:
        print(len(dictb[key]), key.capitalize())
        for x in range(len(dictb[key])):
            print(dictb[key][x])

printInfo(dojo)

