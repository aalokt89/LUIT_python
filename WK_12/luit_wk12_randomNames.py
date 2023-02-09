import random
import string


deptOptions = ["Marketing", "Accounting", "FinOps"]


def initAsk():
    deptName = input(f"Enter department name ({', '.join(deptOptions)}): ")
    
    #convert deptOptions to lowercase
    deptOptions_lower = [i.lower() for i in deptOptions]
    
    #validate dept name
    if deptName.lower() in deptOptions_lower:
        nameCount = int(input("Enter number of names to generate: "))
        nameList = createName(deptName, nameCount)
        
        print(nameList)
        return nameList
        
    else:
        print(f"'{deptName}' is not a valid department. You must choose between 'Marketing, Accounting, or FinOps.'")
        return 1
    
#functiion to create random names___________________________________________
def createName(deptName, nameCount):
    names = []
    #iterate over nameCount
    for i in range(nameCount):
    
        #create random alphanumeric string 8 characters long
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    
        #join deptName and random suffix into one string
        finalName = str(f"{deptName.lower()}_{suffix}") 
        
        #add finalName to nameList
        names.append(finalName)
    
    return names
    
initAsk()