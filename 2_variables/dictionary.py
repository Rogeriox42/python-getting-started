user = {
    'name': 'Rogerio', 
    'username': 'rogeriorodrigues.io', 
    'age': '25'
}

print(user)

#Accessing Items inside a Dictionary 
print(user['name'])

age = user.get('age')
print(age) 

#Changing Value 
user['age'] = 40 
print(user['age'])

#Looping Through Keys in a Dictionary 
print("\nLooping Through Keys in a Dictionary")
for info in user:
    print(info)

#Looping Through Values in a Dictionary - 1st way 
print("\nLooping Through Values in a Dictionary - 1st way ")
for info in user: 
    print(user[info])

#Looping Through Values in a Dictionary - 2nd way 
print("\nLooping Through Values in a Dictionary - 2nd way")
for info in user.values():
    print(info)

#Looping Through Keys and Values in a Dictionary - 1st way
print("\nLooping Through Keys and Values in a Dictionary - 1st way")
for info in user:
    print(info, user[info])

#Looping Through Keys and Values in a Dictionary - 2nd Way
print("Looping Through Keys and Values in a Dictionary - 2nd Way")
for key, value in user.items():
    print(key, value)

#References 
'''
https://www.w3schools.com/python/python_dictionaries.asp
'''


