employees=[
  {"id":1,"name":"John","sal":12000,"doj":"01-01-2021"},
  {"id":2,"name":"Dean","sal":13000,"doj":"02-02-2023"},
  {"id":3,"name":"Sampurna","sal":14500,"doj":"09-09-2020"},
  {"id":4,"name":"Diana","sal":22000,"doj":"12-21-2024"}  
]

#  Task 1: List all employees whose name ends with 'a'.
#          Calculate their total sal , average sal.
#  Task 2: find out 2nd highest salary getter.
#  Task 3: Calculate total work experience in yrs for all
#          employees.



#  Task 4: Sort all employees by most recent joining to past.
#  Task 5: Provide 2% DA, 3% HRA , 1% TDS to those employees
#          who are working more than equal 2 yrs on same
#          company.

from datetime import datetime
from math import floor

def getWorkExpr(empObj:dict):
   join_date = datetime.strptime(empObj.get("doj"),"%m-%d-%Y")
   curDate = datetime.now()
   dateDiff = curDate-join_date
   work_expr = floor(dateDiff.days/365)
   return {
       "id":empObj.get("id"),
       "name":empObj.get("name"),
       "sal" :empObj.get("sal"),
       "doj" :empObj.get("doj"),
       "work_expr":work_expr
   }

newEmployees= list(map(getWorkExpr,employees)) #map() -> "turn this into something else"
print("Showing all work experiences:")

def sort_experience(empObj:dict):
    return empObj.get("work_expr")

sorted_experience = sorted(newEmployees, key= sort_experience)
print(sorted_experience, end="\n")





# def updated_salary(user: dict):
#     DA, HRA, TDS = 0.02, 0.03, 0.01
#     salary = user.get("sal")
#     DA *= salary
#     HRA *= salary
#     TDS *= salary
#     for item in employees:
#         work_exp = user.get(work_exp)
#         if work_exp >= 2:
#             salary = salary + DA + HRA - TDS

# new_salary= list(map(updated_salary,newEmployees))
# print(new_salary, end= " ")




print("\n\n\n\n\n\n")

# print(employees,type(employees))
# for emp in employees:
#     if emp.get("name")[-1].lower() == 'a':
#         print(emp.get("name"))

# def getEmpByName(empObj:dict):
#     if empObj.get("name")[-1]=='a':
#         return empObj
   
# print("using filter function:")
# selectedEmps = list(filter(getEmpByName,employees))

# for emp in selectedEmps:
#     print(emp['name'],emp['sal'],emp['doj'])

# def getSalSorted(empObj:dict):
#     return empObj.get("sal") #sal column has to be returned as a key for sorted function.

# empSalSorted= sorted(employees,key=getSalSorted,reverse=True) #Descending order.
# print("Getting 2nd Highest salary getter:")
# print(empSalSorted[1]['name'],empSalSorted[1]['sal'])

#Third Highest , Third lowest salary getter.











#Calculating total work exprience in yrs
# from datetime import datetime
# from math import floor

# def getWorkExpr(empObj:dict):
#    dojDate = datetime.strptime(empObj.get("doj"),"%m-%d-%Y")
#    curDate = datetime.now()
#    dateDiff = curDate-dojDate
#    work_expr = floor(dateDiff.days/365)
#    return {
#        "id":empObj.get("id"),
#        "name":empObj.get("name"),
#        "sal" :empObj.get("sal"),
#        "doj" :empObj.get("doj"),
#        "work_expr":work_expr
#    }

# newEmployees= list( map(getWorkExpr,employees))
# print("Showing all work experiences:")
# for emp in newEmployees:
#     print(emp['name'],emp['doj'],emp['work_expr'])


# filter




# prevous method
# newEmployees=[] #Empty list
# for emp in employees:
#     doj = emp.get("doj")
#     dojDate = datetime.strptime(doj,"%m-%d-%Y")
#     #print(dojDate)
#     curDate = datetime.now()
#     dateDiff = curDate - dojDate
#     #print(floor(dateDiff.days/365))
#     work_expr = floor(dateDiff.days/365)
#     data:dict = {
#         "id":emp['id'],
#         "name":emp['name'],
#         "doj": emp['doj'],
#         "sal": emp['sal'],
#         "work_expr":work_expr
#     }
#     newEmployees.append(data)


# print("Showing all work experiences :")
# for emp in newEmployees:
#     print(emp['name'],emp['doj'],emp['work_expr'])


# what i did
# a_user = []
# total_salary = 0

# for user in employees:
#     name = user["name"]
#     if user["name"][len(name) - 1] == "a":
#         total_salary+= user.get("sal")
#         a_user.append(name)
# print(a_user)
# print("Total salary is : ", total_salary)
# print("Average salary is : ", (total_salary/ len(a_user)), "\n")


# maxi = 0
# second_max = 0

# for user in employees:
#     salary = user.get("sal")
#     # print(salary)
#     if salary > maxi:
#         second_max = maxi
#         maxi = salary
#     elif second_max < salary < maxi:
#         second_max = salary

# print("Second highest salary: ",second_max)