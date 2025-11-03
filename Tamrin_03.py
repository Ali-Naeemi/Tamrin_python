def calculate_student_gpa(student):
    grades = student["grades"]
    average = sum(grades) / len(grades)
    return average

students = []

print("tedad daneshjoo ha: ")
num_students = int(input())

for i in range(num_students):
    print(f"\nDaneshjoo {i+1}:")
    
    print("student id: ")
    student_id = input()
    
    print("name: ")
    name = input()
    
    print("tedad dars ha: ")
    num_grades = int(input())
    
    grades = []
    for j in range(num_grades):
        print(f"nomre dars {j+1}: ")
        grade = float(input())
        grades.append(grade)
    
    student = {
        "student_id": student_id,
        "name": name,
        "grades": grades
    }
    
    students.append(student)

print("\nNatije:")
for student in students:
    gpa = calculate_student_gpa(student)
    print(f"{student['name']} - GPA: {gpa:.2f}")