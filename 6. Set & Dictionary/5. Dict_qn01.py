users = [ #list of dictionary
    {"id":1,"name":"John","sal":12000},
    {"id":2,"name":"Smith","sal":13000},
    {"id":3,"name":"Sourav","sal":30000},
    {"id":4,"name":"Joe","sal":22000},
    {"id":5,"name":"Ronn","sal":24000}
]

# find total salary
total_sal = 0

for user in users:
    total_sal+= user.get("sal")
    print(user.get("name"), user["sal"])
print("Total salary is : ", total_sal)
print("Average salary is : ", (total_sal/ len(users)), "\n")


# user_name starting with 'J'
for user in users:
    if user.get("name")[0].lower() == 'j':
        print(user.get("name"))

# user_name ending with 'n'
for user in users:
    if user.get("name")[len(user)-1].lower() == 'n':
        print(user.get("name"))

# user name with 'th'
for user in users:
    name = user["name"]
    for i in range(len(name) - 1):
        if 'th' in user["name"]:
            print(f"\nName with 'th': {name}")
            break
        
# user whose salary is between 10k-20k

for user in users:
    if user.get("sal") >= 10000 and user.get("sal") <= 20000:
        print(user.get("name"), "\t")
print()

# user whose salary is not between 10k-20k
for user in users:
    if not (user.get("sal") >= 10000 and user.get("sal") <= 20000):
        print(user.get("name"), "\t")
        
        
# sort user by their salary in descending order

# sorted_salary = sorted(users, key = lambda x: x["sal"], reverse= True)
for user in users:
    print(user)

# using sort() original is modified
users.sort(key = lambda x: x["sal"], reverse = True) #lamda parameter : return value;



def getSal(userObj : dict):
    return userObj.get("sal");