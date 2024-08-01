def calculate_grade(written_test, lab_exams, assignments):
    return (written_test * 0.70) + (lab_exams * 0.20) + (assignments * 0.10)

def main():
    print("Enter the marks scored by the student:")
    written_test = float(input("Written test = "))
    lab_exams = float(input("Lab exams = "))
    assignments = float(input("Assignments = "))

    grade = calculate_grade(written_test, lab_exams, assignments)
    print(f"Grade of the student is {grade:.2f}")
main()