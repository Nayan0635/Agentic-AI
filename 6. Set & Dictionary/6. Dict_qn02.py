
users_address = [
    {
        "id": 1,
        "name": "Sourav",
        "languages": ["Bengali", "Hindi", "English"],
        "address": {
            "state": "WB",
            "city": "Medinipur",
            "pinCode": 712234
        }
    },
    {
        "id": 2,
        "name": "Sourajit",
        "languages": ["Bengali", "Hindi", "English", "Urdu"],
        "address": {
            "state": "WB",
            "city": "Kolkata",
            "pinCode": 712231
        }
    },
    {
        "id": 3,
        "name": "Soumik",
        "languages": ["Hindi", "English", "Tamil"],
        "address": {
            "state": "Karnataka",
            "city": "Bangalore",
            "pinCode": 712232
        }
    },
    {
        "id": 4,
        "name": "Nayan",
        "languages": ["English", "Tamil", "Telegu"],
        "address": {
            "state": "Tamilnadu",
            "city": "Chennai",
            "pinCode": 612234
        }
    }
]

# 1. Sort all users by number of languages (descending)
sorted_users = sorted(users_address, key=lambda user: len(user["languages"]), reverse=True)

print("Sorted Users:")
for user in sorted_users:
    print(user["name"], len(user["languages"]))

# 2. Select users from WB
wb_users = [
    user for user in users_address
    if user["address"]["state"] == "WB"
]

print("\nUsers from WB:")
for user in wb_users:
    print(user["name"])

# 3. Select users who know more than 2 languages
multi_language_users = [
    user for user in users_address
    if len(user["languages"]) > 2
]

print("\nUsers knowing more than 2 languages:")
for user in multi_language_users:
    print(user["name"])

# 4. Generate list of all unique languages
all_languages = set()

for user in users_address:
    all_languages.update(user["languages"])

print("\nUnique Languages:")
print(list(all_languages))





# print(type(user_address)) #<class 'list'>
# for user in user_address:
#     # print(len(user.get("languages"))) #it gives length of "languages" for all user
#     # user.sort(key = lambda len(user.get("languages")) : user.get("name") #XXX
#     sorted_name = sorted(user_address, key = lambda x : x[len(user.get("languages"))])
#     print(sorted_name)






# print(type(user_address[0]))#<class 'dict'>
# print(type(user_address[0]["name"]))#<class 'str'>
# print(type(user_address[0]["languages"]))#<class 'list'>
# print(type(user_address[0]["address"]))#<class 'dict'>
# print(type(user_address[0]["address"]["state"]))#<class 'str'>
# print(type(user_address[0]["address"]["pinCode"]))

