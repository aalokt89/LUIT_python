import random
import string

# Online Python - IDE, Editor, Compiler, Interpreter

deptName = input("Enter department name: ").lower()
nameCount = int(input("Enter number of names to generate: "))
nameList = []


def randomName():
    #iterate over nameCount
    for i in range(nameCount):
        letters = string.ascii_lowercase
        
        #create random letters 8 characters long
        suffix = ''.join(random.choice(letters) for i in range(8))
        
        #associate suffix with deptName
        newName = ((deptName, suffix))
        
        #join deptName and random suffix into one string
        finalName = '_'.join(newName)
        
        #add finalNamee to nameList
        nameList.append(finalName)
    
    return nameList
    
randomName()
print(nameList)