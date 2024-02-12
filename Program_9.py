def checkAttendance(roll):
    present_list = [106,107,108,109,115,116,120,125,162]
    if roll in present_list:
        return "Student is Present!"
    else:
        return "Student is Absent!"

roll = int(input("Enter the roll number of student : "))
print(checkAttendance(roll))