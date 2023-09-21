import unittest
from OOP_StudentCourse.course import Course
import mock

"""
What can we unit test?
For hard-coded values:
    - unit test: Course (Entity-Model)
For Data persistance (json):
    - integration test: Course <--> import .json data via db_handler

- Can create object
- Search_student
# integration_test --> coupling, importing Student()
# unittest --> decoupling
- Calculate_avg

"""

class TestCourse(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.course = Course()
        cls.mockedStudentObj = mock.Mock()

    def test_canCreateObject(self):
        # Sad path test
        with self.assertRaises(TypeError):
            c1 = Course('course 1')

    def test_courseInfoExists(self):
        self.assertIsNotNone(self.course.course_info)

    def test_searchStudentObjReturnsVal(self):
        """
        name in DB -> studnetObj
        name Not in DB -> None
        """
        # Happy path testing
        self.mockedStudentObj.name = 'John'
        student = self.course.search_student(self.mockedStudentObj)
        # breakpoint()
        self.assertIsNotNone(student)

    def test_searchStudentObjReturnNone(self):
        # Sad path testing
        self.mockedStudentObj.name = 'Arash'
        student = self.course.search_student(self.mockedStudentObj)
        self.assertIsNone(student)

    def test_calAvgReturnsVal(self):
        # Happy path testing
        self.mockedStudentObj.name = 'Amir'
        avg = self.course.calc_avg(self.mockedStudentObj)
        self.assertIsNotNone(avg)
    
    def test_calAvgReturnsNone(self):
        # Sad path testing
        self.mockedStudentObj.name = 'asdasd'
        with self.assertRaises(KeyError):
            avg = self.course.calc_avg(self.mockedStudentObj)
