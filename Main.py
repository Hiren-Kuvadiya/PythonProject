from Student import Student

class Main:

    student1 = Student("Hiren K", "12th", 18)
    print("Student 1:", student1.name, student1.student_class, student1.age, student1.place)

    # Creating a student with place
    student2 = Student("Jon Doe", "10th", 16, "New York")
    print("Student 2:", student2.name, student2.student_class, student2.age, student2.place)