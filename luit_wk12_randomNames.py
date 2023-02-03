import random
import string

# Online Python - IDE, Editor, Compiler, Interpreter

deptName = input("Enter department name: ").lower()
nameCount = int(input("Enter number of names to generate: "))
nameList = []


def randomName():
    #iterate over nameCount
    for i in range(nameCount):
    
        #create random alphanumeric string 8 characters long
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        
        #associate suffix with deptName
        newName = ((deptName, suffix))
        
        #join deptName and random suffix into one string
        finalName = '_'.join(newName)
        
        #add finalNamee to nameList
        nameList.append(finalName)
    
    return nameList
    
randomName()
print(nameList)