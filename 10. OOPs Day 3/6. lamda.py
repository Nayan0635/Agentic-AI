# Anonymous /Lamda function :



add = lambda a,b: a+b
mult= lambda a,b:a*b
print(add(12,23))
print(mult(12,23))

#filter
numbers = [12,23,34,56]
#Find out all even nos
evennos = list(filter(lambda a:a%2==0,numbers))
print(evennos)
#map
#Multiply all numbers by 2
multiply_result= list(map(lambda n: n*2,numbers ))
print(multiply_result)

#sorted
users = [
    {
        "id":1,"name":"John","sal":12000,
    },
    {
        "id":2,"name":"Geeta","sal":14000
    },
    {
        "id":3,"name":"Nayan","sal":23000
    },
    {
        "id":4,"name":"Goutam","sal":21000
    }
]

sorted_users= sorted(users,key=lambda u:u.get("sal"),reverse=True)
print(sorted_users)


#Find Out those users whose name begins with 'g'
print("users whose name begins with 'g'")
searched_users= list(filter(lambda u : u.get("name").lower()[0]=='g',users))
print(searched_users)

#Show those users whose salary is between 15k-20k

#Company has decided to provide 2% DA, 3% HRA , 1% Incentive
print("Generating Payslip:")
calculated_users= list(map(lambda u:{
                                    "id":u.get("id"),
                                    "name":u.get("name"),
                                    "sal":u.get("sal"),
                                    "DA":u.get("sal")*0.02,
                                    "TDS":u.get("sal")*0.01,
                                    "HRA":u.get("sal")*0.03,
                                    "gross":u.get("sal")+u.get("sal")*0.03+u.get("sal")*0.02-u.get("sal")*0.01
                                    },
                                    users))
#print(calculated_users)
import json
print(json.dumps(calculated_users))