myServices = []

#add items
myServices.extend(["EC2", "S3", "Lambda", "DynamoDB", "CloudFormation", "CloudWatch"])


print(len(myServices))
print(myServices)

#function to remve items
def removeItem(list, item):
    if item in list:
        list.remove(item)
        print(f"{item} removed from list")
    else:
        print(f"{item} does not exist")
    
#call function
removeItem(myServices, "EC2")
removeItem(myServices, "S3")

print(len(myServices))
print(myServices)
