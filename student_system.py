excellent_count = 0
very_good_count = 0
good_count = 0
pass_count = 0
fail_count = 0
marks = []
students = []

while True:
    print("\n1. Add Student")
    print("2. Display")
    print("3. Class Summary")
    print("4. Exit")
    choice = input("Choose (1-4): ")

    if choice == "1":
        student_number = int(input("Student Number: "))
        name = input("Student Name: ").strip().title()
        mark = int(input("Mark: "))

        if mark >= 80:
            grade, decision = "A", "Excellent"
            excellent_count += 1
        elif mark >= 70:
            grade, decision = "B", "Very good"
            very_good_count += 1
        elif mark >= 60:
            grade, decision = "C", "Good"
            good_count += 1
        elif mark >= 50:
            grade, decision = "D", "Pass"
            pass_count += 1
        else:
            grade, decision = "E", "Fail"
            fail_count += 1

        students.append([student_number, name, mark, grade, decision])
        marks.append(mark)
        print(f"Grade: {grade} | Decision: {decision}")

    elif choice == "2":
        if not students:
            print("No students yet.")
        else:
            print(f"Excellent: {excellent_count}")
            print(f"Very good: {very_good_count}")
            print(f"Good: {good_count}")
            print(f"Pass: {pass_count}")
            print(f"Fail: {fail_count}")
            print("\n-- All Students --")
            for s in students:
                print(f"{s[0]} | {s[1]} | Mark: {s[2]} | Grade: {s[3]} | Decision: {s[4]}")

    elif choice == "3":
        if marks:
            print(f"Highest: {max(marks)} | Lowest: {min(marks)} | Average: {sum(marks)/len(marks):.2f}")
        else:
            print("No marks yet.")

    elif choice == "4":
        print("Bye!")
        break