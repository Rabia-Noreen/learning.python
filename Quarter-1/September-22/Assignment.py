def manage_student_database():

    student_list = []
    student_id = 1

    while True:
        student_name = input("Please enter the student's name (or type 'stop' to finish): ")

        if student_name.lower() == 'stop':
            break

       
        if any(student_name == student[1] for student in student_list):
            print(f"This name is already in the list.")
        else:
        
            student_list.append((student_id, student_name))
            student_id += 1

    print("\nComplete List of Students (Tuples):")
    print(student_list)

    print("\nList of Students with IDs:")
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}")

    total_students = len(student_list)
    total_name_length = sum(len(student[1]) for student in student_list)
    longest_name = max(student_list, key=lambda student: len(student[1]))[1] if student_list else None
    shortest_name = min(student_list, key=lambda student: len(student[1]))[1] if student_list else None

    print(f"\nTotal number of students: {total_students}")
    print(f"Total length of all student names combined: {total_name_length}")
    if longest_name:
        print(f"The student with the longest name is: {longest_name}")
    if shortest_name:
        print(f"The student with the shortest name is: {shortest_name}")

manage_student_database()
