    # Employee class
    # empid, empName, departments, salary
    # Show 5 employees data
    # Calculate Average, Total salary of all employees
    
class employee:
    def __init__(self, empid: int, empName: str, departments: list, salary: int):
        self.__empid = empid
        self.__empName = empName
        self.__departments = departments
        self.__salary = salary

    def getUser(self) -> dict:
        return {
            "empid": self.__empid,
            "empName": self.__empName,
            "departments": self.__departments,
            "salary": self.__salary
        }

# MainScript
emp1 = employee(31752, "kjwgh", ["eat", "feed", "sleep", "run"], 12000)
emp2 = employee(45236, "segg", ["eat", "feed", "run"], 145000)
emp3 = employee(52176, "esgeg", ["eat", "sleep", "run"], 56090)
emp4 = employee(41752, "seger", ["feed", "sleep", "run"], 64537)
emp5 = employee(47621, "gjjtytt", ["eat", "feed", "sleep"], 74567)

employee_list = []  # Empty list
employee_list.append(emp1.getUser())
employee_list.append(emp2.getUser())
employee_list.append(emp3.getUser())
employee_list.append(emp4.getUser())
employee_list.append(emp5.getUser())

print(employee_list, len(employee_list))

for emp in employee_list:
    dept = ",".join(d for d in emp['departments'])
    print(emp['empid'], emp['empName'], emp['salary'], dept)

# --- Calculations ---
total_salary = sum(emp['salary'] for emp in employee_list)
average_salary = total_salary / len(employee_list)

print(f"\nTotal Salary: {total_salary}")
print(f"Average Salary: {average_salary}")