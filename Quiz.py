with open('data.txt', 'r') as file:
    staffData = file.readlines()
for i in range(len(staffData)):
    staffData[i] = staffData[i].replace("#", " ").split()
class Staff:
    name:str
    def __init__(self, name):
        self.name = name
ids = {}
position = {}
salary = {}
for i in range(len(staffData)):
    ids[str(staffData[i][1])] = staffData[i][0]
    position[str(staffData[i][1])] = staffData[i][2]
    salary[str(staffData[i][1])] = staffData[i][3]


def staffApp():
    print("|ID         |Name       |Postion        |Salary")
    for i in ids:
        print("|" + str(ids[i]) + "      |" + str(i) + "     |" + str(position[i]) + "     |" + str(salary[i]))
    print("1. New Staff")
    print("2. Delete Staff")
    print("3. View Summary Data")
    print("4. Save & Exit")
    choice = input("Input Choice:")
    if str(choice) == "1":
        idinput = True
        while idinput == True:
            newid = input("Input ID (SXXXX)")
            if newid[0] != "S":
                print("Pleaase follow the format")
                continue
            if int(newid[1:]) != int:
                print("Please follow the format")
                continue
            if newid in ids:
                print("ID already exists")
                continue
            else:
                idinput = False
                nameinput = True
                while nameinput == True:
                    newname = input("Input name: [0 - 20]")
                    if len(newname) < 5:
                        continue
                    else:
                        nameinput = False
                        ids[str(newname)] = str(newid)
                        positionInput = True
                        while positionInput == True:
                            newPosition = input('Input position (Staff|Officer|Manager)')
                            positionList = ("Staff", "Officer", "Manager")
                            if newPosition in positionList:
                                positionInput = False
                                position[str(newname)] = str(newPosition)
                                salaryInput = True
                                while salaryInput == True:
                                    newSalary = input("Input Salary:")
                                    if newPosition == "Staff":
                                        if salaryInput > 7000000 or salaryInput < 3500000:
                                            continue
                                        else:
                                            salary[str(newname)] = int(newSalary)
                                            salaryInput = False
                                    if newPosition == "Officer":
                                        if salaryInput < 7000001 or salaryInput > 10000000:
                                            continue
                                        else:
                                            salary[str(newname)] = int(newSalary)
                                            salaryInput = False
                                    if newPosition == "Manager":
                                        if salaryInput < 10000001:
                                            continue
                                        else:
                                            salary[str(newname)] = int(newSalary)
                                            salaryInput = False
    if str(choice) == "2":
        deleteid = True
        while deleteid == True:
            delid = input("Input ID")
            if str(delid) in ids:
                del (ids[delid])
                deleteid = False

            else:
                continue
    if str(choice) == "3":
        print("|ID         |Name       |Postion        |Salary")
        for i in ids:
            print("|" + str(ids[i]) + "      |" + str(i) + "     |" + str(position[i]) + "     |" + str(salary[i]))
    if str(choice) == "4":
        file.write(ids, position, salary)
    else:
        staffApp()
staffApp()