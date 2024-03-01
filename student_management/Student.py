import unittest


class Student:
    num_students = 0
    def __init__(self, name, student_class, age, place=None):
        self.name = name
        self.student_class = student_class
        self.age = age
        self.place = place
        Student.num_students += 1


# Defining a separate test case here
def run_tests():
    test_student = Student("Test Student", "11th", 17)
    assert test_student.name == "Test Student"
    assert test_student.student_class == "11th"
    assert test_student.age == 17
    assert test_student.place is None
    print("All tests passed successfully.")


# Defining a Testcase class
class TestStudent(unittest.TestCase):
    def test_create_student_without_place(self):
        student1 = Student("John Smith", "12th", 18)
        self.assertEqual(student1.name, "John Smith")
        self.assertEqual(student1.student_class, "12th")
        self.assertEqual(student1.age, 18)
        self.assertIsNone(student1.place)

    def test_create_student_with_place(self):
        student2 = Student("Jane Doe", "10th", 16, "New York")
        self.assertEqual(student2.name, "Jane Doe")
        self.assertEqual(student2.student_class, "10th")
        self.assertEqual(student2.age, 16)
        self.assertEqual(student2.place, "New York")

    def test_access_student_attributes(self):
        student3 = Student("Alice", "11th", 17)
        self.assertEqual(student3.name, "Alice")
        self.assertEqual(student3.student_class, "11th")
        self.assertEqual(student3.age, 17)
        self.assertIsNone(student3.place)

    def test_update_student_attributes(self):
        student4 = Student("Bob", "9th", 15)
        student4.name = "Bobby"
        student4.student_class = "8th"
        student4.age = 14
        student4.place = "Los Angeles"
        self.assertEqual(student4.name, "Bobby")
        self.assertEqual(student4.student_class, "8th")
        self.assertEqual(student4.age, 14)
        self.assertEqual(student4.place, "Los Angeles")

    def test_duplicate_names_different_classes(self):
        student6 = Student("Sam", "10th", 16)
        student7 = Student("Sam", "12th", 18)
        self.assertNotEqual(student6.student_class, student7.student_class)


if __name__ == '__main__':
    run_tests()
    unittest.main()
