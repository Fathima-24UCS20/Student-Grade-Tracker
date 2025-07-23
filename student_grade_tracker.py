
def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

students = {}
n = int(input("Enter the number of students: "))

for _ in range(n):
    name = input("\nEnter student name: ")
    m = int(input("Enter number of subjects: "))
    subject_marks = {}
    for i in range(m):
        subj = input(f"Enter subject name {i+1}: ")
        score = float(input(f"Enter mark for {subj}: "))
        subject_marks[subj] = score
    students[name] = subject_marks

topper = ""
highest_average = 0

print("\n===== Student Report =====")
for name, marks in students.items():
    avg = calculate_average(list(marks.values()))
    grade = get_grade(avg)
    
    print(f"\nName     : {name}")
    print(f"Marks    : {marks}")
    print(f"Average  : {avg:.2f}")
    print(f"Grade    : {grade}")
    
    if avg > highest_average:
        highest_average = avg
        topper = name

print("\n===========================")
print(f"\n🏆 Topper: {topper} with an average of {highest_average:.2f}")
