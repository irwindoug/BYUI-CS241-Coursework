'''
Program: Check01b.py
Brother Mellor, CS 241
Author: Doug Irwin
Summary: Asks for your name and age. Gives you your age on your next birthday.
'''

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print()
print ("Hello %s, you are %d years old.\nOn your next birthday, you will be %d." % (name, age, age+1))