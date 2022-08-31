studentList=[]

while True:
    print("1 to add students\n 2 to view all stdents\n 3 to Exit\n")
    choice=int(input("Enter your choice : "))

    if(choice==1):
        getName=input("Enter the name of the student:")
        getRoll=input("Enter the roll number:")
        getAdmissionNo=input("Enter the admission number:")
        getCollege=input("Enter the college:")

        data={"name":getName, "rollNo":getRoll, "AdminNo":getAdmissionNo, "college":getCollege}
        print(data)
        studentList.append(data)
    elif(choice==2):
        print(studentList)
    else:
        break
