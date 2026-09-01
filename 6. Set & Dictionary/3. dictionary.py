user = {
    "id" : 1,
    "Name" : "John",
    "Age" : 23,
    "Gender" : "Male"
}

print(user, type(user))

print(user.keys(), type(user.keys()), end = "\n") 

print(user.values(),type(list(user.values())) , end = "\n")#convert into list


# update data
user.update({"Age" : 30})
print(user, end = "\n")

# or do this
user["Age"] -= 7
print(user, end = "\n")


# looping through dictionary
for key in user.keys():
    print("Key is: ", key)
    print("Value is: ", user[key], end = "\n\n")
    
# use zip to create disctionary
a = ['id', 'Name', 'Age', 'Gender']
b = [2, 'Don', 21, 'Male']

user2 = dict(zip(a, b))
print(user2)

'''
#Loop through single Object
#Loop through a single dictionary
for k in user.keys():
    print('keys=',k)
    print('values=',user[k])
'''