#Simple Assignment 
name = 'Rogerio' 
username = 'rogeriorodrigues.io'
passcode = 'potato_42_starwars'
img_url = 'https://avatars1.githubusercontent.com/u/16908177?s=400&u=cb8dd6b5a741d5d8da751338339c6ec2159a474c&v=4'

#Simple Variable Printing 
print()
print("Simple Variable Printing")
print(name)
print(username)
print(passcode)

#Variable + Text Label 
print()
print("Variable + Text Label")
print("Name: ", name)
print("Username: ", username)
print("Passcode: ", passcode) 

#Multiple Assignments 
movie, music, game = "Star Wars", "Armored Dawn", "Resident Evil"

print("\nMultiple Assignments' Output")
print("Movie: ", movie, "\nMusic: ", music, "\nGame: ", game)

#Multiline Comments are Available when Using 3 quotes 
#Python reads the content and ignore it 
#Uncomment 33 to 35 to see the error 

#Error When Combining Text and Number
'''
text = 'Python'
number = 3.8
print(text + number) 
'''

#Bonus = Functions!
title = 'Incredible!'

def myFunc():
    print('\n' + name + " You're " + title)

myFunc()

age = 25
def mySum(n1):
    n2 = 10 
    print('\nResult:', (n1 + n2))

mySum(age)


