student_names = []
student_marks = []

# menu screen where the user decides on what they want to do
while True:
    print("\nMenu")
    print("1. Add student")
    print("2. View/Sort List")
    print("3. Remove student info")
    print("4. Stats")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    # this is the way students' marks and names are added
    if choice == 1:
        num_students = int(input("Enter number of students: "))
        if num_students <= 0:
            print("Invalid number")
            continue

        for i in range(num_students):
            name = input("Enter student name: ")
            marks = float(input("Enter student mark: "))
            student_names.append(name)
            student_marks.append(marks)
            print("Student has been added")

 # user gets to view the records
    elif choice == 2:
        if not student_names:
            print("List is empty")
            continue

        # Create a list of (name, mark) pairs
        student_data = list(zip(student_names, student_marks))
        ascending = sorted(student_data)
        descending = sorted(student_data, reverse=True)

        # original list
        print("\nOriginal Student List:")
        for i, (name, marks) in enumerate(student_data, 1):
            print(f"{i}. {name}: {marks}")

        # Sort ascending by name
        print("\nAscending Order (by Name):")
        for i, (name, marks) in enumerate(ascending, 1):
            print(f"{i}. {name}: {marks}")

        # Sort descending by name
        print("\nDescending Order (by Name):")
        for i, (name, marks) in enumerate(descending, 1):
            print(f"{i}. {name}: {marks}")
    # can remove student when they choose
    elif choice == 3:
        num = int(input("Enter the number you want to remove: "))
        if num <= 0 or num > len(student_names):
            print("Invalid input")
        else:
            removed_name = student_names.pop(num - 1)
            removed_mark = student_marks.pop(num - 1)
            print(f"Removed: ({removed_name}, {removed_mark})")

    # this display the average, highest or lowest mark and the students who passed or failed
    elif choice == 4:
        passed_students = []
        failed_students = []
        student_data = list(zip(student_names, student_marks))

        # this checks whether lists are empty
        if not student_marks:
            print("No students to calculate stats.")
            continue

        average = sum(student_marks) / len(student_marks)
        highest_mark = max(student_marks)
        lowest_mark = min(student_marks)

        # separates the students who passed or failed and places in two different lists
        for name, marks in student_data:
            if marks >= 50:
                passed_students.append(name)
            else:
                failed_students.append(name)
        # display the infomation
        print(f"\nAverage Mark: {average:.2f}")
        print(f"Highest Mark: {highest_mark}")
        print(f"Lowest Mark: {lowest_mark}")
        print(f"Passed Students: {', '.join(passed_students) if passed_students else 'None'}")
        print(f"Failed Students: {', '.join(failed_students) if failed_students else 'None'}")

    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid value")
