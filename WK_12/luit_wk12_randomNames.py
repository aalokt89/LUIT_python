import random
import string

nameList = []
deptOptions = ["Marketing", "Accounting", "FinOps"]


def initAsk():
    deptName = input("Enter department name (Marketing, Accounting, or FinOps): ")
    
    #validate dept name
    if deptName.lower() in str(deptOptions).lower():
        nameCount = int(input("Enter number of names to generate: "))
        createName(deptName, nameCount)
        
        print(nameList)
        return 0
        
    else:
        print(f"'{deptName}' is not a valid department. You must choose between 'Marketing, Accounting, or FinOps.'")
        return 1
    
#functiion to create random names___________________________________________
def createName(deptName, nameCount):
    
    #iterate over nameCount
    for i in range(nameCount):
    
        #create random alphanumeric string 8 characters long
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        
        #associate suffix with deptName
        #newName = ((deptName, suffix))
        
        #join deptName and random suffix into one string
        finalName = str(f"{deptName.lower()}_{suffix}") 
        
        #add finalName to nameList
        nameList.append(finalName)
    
    return nameList
    
initAsk()