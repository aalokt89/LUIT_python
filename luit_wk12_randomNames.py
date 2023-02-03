import random
import string

nameList = []

deptOptions = ["Marketing", "Accounting", "FinOps"]


def randomName(deptName, nameCount):
    
    #iterate over nameCount
    for i in range(nameCount):
    
        #create random alphanumeric string 8 characters long
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        
        #associate suffix with deptName
        #newName = ((deptName, suffix))
        
        #join deptName and random suffix into one string
        finalName = str(f"{deptName}_{suffix}") 
        
        #add finalNamee to nameList
        nameList.append(finalName)
    
    return nameList
    
#check valid dept option and execute randomize if true
def deptChecker():
    deptName = input("Enter department name: ").lower()
    nameCount = int(input("Enter number of names to generate: "))
    
    if deptName in str(deptOptions).lower():
        randomName(deptName, nameCount)
        return True
    else:
        print(f"{deptName} is not a valid option.")
        return False
        



deptChecker()    
print(nameList)