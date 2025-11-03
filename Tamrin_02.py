print("tedad dars ha : ")
counter = int(input())

print("enter name : ")
name = input()

grades = []
for i in range(counter):
    print(f"nomre dars {i+1}: ")
    grade = float(input())
    grades.append(grade)

average = sum(grades) / counter

print(f"\n{name} moadele shoma: {average:.1f}")

if average >= 12:
    print("(ghabool)")
elif 12 > average >= 10:
    print("(mashrot)")
else:
    print("(mardod)")