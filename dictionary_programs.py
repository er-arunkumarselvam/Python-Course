# Microprogram 1
# Create a dictionary a name of grocery
grocery = {"Milk": 45, "Biscuit": 10, "Rice": 35, "Chocolate": 5, "Millet's": 25, "Oil": 78, "Ballpoint Pen": 7}
for itemName, itemPrice in grocery.items():
    # Price change increase 10% for all products
    grocery[itemName] = round(itemPrice * 1.2, 2)
print(grocery)
print()
# Delete the one product
# groceryList = list(grocery.keys())
for itemName in list(grocery.keys()):  # list() - typecasting "change from dictionary to list"
    if itemName == "Millet's":
        del grocery[itemName]
print(grocery)
# Typecasting
groceryList = list(grocery.keys())
for item in groceryList:
    print(item)
print()

# Microprogram 2
# I mistake enter the  key is name and values is id, But id is a key and value is name. how change the key and values?
officeEmployee = {"Arun": 101, "Vijay": 102, "Krishna": 103, "Shafik": 104, "Dharma": 105, "Vignesh": 106,
                  "Vinith": 107, "Arun": 108, "Vino": 109}
officeEmployee2 = {}
for key, value in officeEmployee.items():
    officeEmployee2[value] = key
print(officeEmployee2)
print()
# Microprogram 3
employeeSalary = {"Arun": 25000, "Vijay": 28000, "Krishna": 45000, "Shafik": 36000, "Dharma": 50000, "Vignesh": 78000,
                  "Vinith": 100000, "Vino": 150000}
employeeHighSalary = {}
employeeLowSalary = {}
for key, value in employeeSalary.items():
    if value > 39000:
        employeeHighSalary[key] = value
    if value < 39000:
        employeeLowSalary[key] = value
print("Experienced Pay Salary Candidates : ", employeeHighSalary)
print("Fresher Pay Salary Candidates : ", employeeLowSalary)
print()
# Microprogram 4 - Sorted()
employeeSalaryOrder = {"Arun": 85000, "Vijay": 28000, "Krishna": 15000, "Shafik": 36000, "Dharma": 50000,"Vignesh": 78000,"Vinith": 12000, "Vino": 15000}
for key in sorted(employeeSalaryOrder):
    print(key, " : ", employeeSalaryOrder[key])
for value in sorted(employeeSalaryOrder.values()):
    print(value)

# Microprogram 5
employeeSalaryOrder = {"Arun": 85000, "Vijay": 28000, "Krishna": 15000, "Shafik": 36000, "Dharma": 50000,"Vignesh": 78000,"Vinith": 12000, "Vino": 15000}
totalSalary = 0
for key in employeeSalaryOrder:
    print(key, " : ", employeeSalaryOrder[key])
    totalSalary+= employeeSalaryOrder[key]
print("Total Salary Amount is ", totalSalary)
totalSalary=0
for key in employeeSalaryOrder.values():
    print(key)
    totalSalary+= key
print("Total Salary Amount is ", totalSalary)