employees=[
  {"id":1,"name":"John","sal":12000,"doj":"01-01-2021"},
  {"id":2,"name":"Dean","sal":13000,"doj":"02-02-2023"},
  {"id":3,"name":"Sampurna","sal":14500,"doj":"09-09-2020"},
  {"id":4,"name":"Diana","sal":22000,"doj":"12-21-2024"}  
]

#  Task 1: List all employees whose name ends with 'a'. XXX
#          Calculate their total sal , average sal. XXX

# emp_list = []
# total_salary = 0
# for emp in employees:
#     # name = emp.get("name")
#     name = emp["name"]
#     if name[-1].lower() == 'a':
#         emp_list.append(name)
#         total_salary += emp["sal"]
# avg_salary = total_salary/ len(emp_list) if emp_list else 0

matches = [emp for emp in employees if emp["name"].lower().endswith('a')]
emp_list = [emp["name"] for emp in matches]
total_salary = sum(emp["sal"] for emp in matches)
avg_salary = total_salary/len(matches) if matches else 0

print("Employees whose name ends with 'a': ")
print(emp_list)
print("Total salary is : ", total_salary)
print("Average salary is : ",avg_salary)



#Task 2: find out 2nd highest salary getter. XXX 

# highest = second_highest = float('-inf')
# for emp in employees:
#     salary = emp.get("sal")
#     if salary > highest:
#         second_highest = highest
#         highest = salary
#     # elif salary > second_highest and salary < highest:
#     elif second_highest < salary < highest:
#         second_highest = salary

salaries = sorted(set(emp["sal"] for emp in employees), reverse= True)
# print(salaries)
second_highest = salaries[1]
third_highest = salaries[2]
third_lowest = salaries[-3]
person = [emp["name"] for emp in employees if emp["sal"] == second_highest]
print("\nSecond highest salary: ",person,"\n")
print("third highest salary: ",third_highest,"\n")
print("third lowest salary: ",third_lowest,"\n")



#  Task 3: Calculate total work experience in yrs for all
#          employees. XXX

from datetime import datetime
from math import floor

def work_experience(emp: dict):
    joinDate = datetime.strptime(emp.get("doj"), "%m-%d-%Y")
    # today = datetime.now()
    # exp_days = (today - joinDate).days
    years = floor((datetime.now() - joinDate).days/365.25)
    # return years
    return {**emp, "work_exp" : years} #copy all original keys + add new one, it doesnt modify the original

# for emp in employees:
#     work_exp = work_experience(emp)
#     print(f"{emp["name"]} : {work_exp} years")

newEmployees = list(map(work_experience, employees))

for emp in newEmployees:
  years = emp["work_exp"]
  print(emp["name"], years)




#  Task 4: Sort all employees by most recent joining to past.XXX

# def sort_emp(emp):
#   return emp["work_exp"]

sorted_employees = sorted(newEmployees, key = lambda x : x["work_exp"])
print(sorted_employees)



#  Task 5: Provide 2% DA, 3% HRA , 1% TDS to those employees
#          who are working more than equal 2 yrs on same
#          company.XXX
print("\n")
def updated_salary(user):
    DA, HRA, TDS = 0.02, 0.03, 0.01
    salary = user.get("sal")
    DA *= salary
    HRA *= salary
    TDS *= salary
    if user.get("work_exp") >= 2:
      salary = salary + DA + HRA - TDS
    # return salary
    return {**user, "sal": salary}

updated_salary_employees = list(map(updated_salary, newEmployees))
# print("\nUpdated Salaries: ", updated_salary_employees)
for emp in updated_salary_employees:
  print(emp["name"], emp["sal"])