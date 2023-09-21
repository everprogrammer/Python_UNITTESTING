import unittest

from OOP_StudentCourse.course import Course
from OOP_StudentCourse.student import Student


"""
What should be tested?
- is created CourseObj of type Course? 
- if sample data exists
- search student function
- calculate average 
"""

class TestIntegrationCourse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._course = Course()
        cls._studentObj = Student(cls._course)

    def test_isObjectCorrectType(self):
        self.assertIsInstance(self._course, Course)
        self.assertIsInstance(self._studentObj, Student)

    def test_checkSampleExists(self):
        sample_data = {
            's_name': 'John',
            'midterm_mark': 15,
            'final_mark': 17
                      }
        self.assertIn(sample_data, self._course.course_info)

    def test_checkSampleDoesNotExist(self):
        sample_data = {
            's_name': 'James',
            'midterm_mark': 10,
            'final_mark': 10
                      }
        self.assertNotIn(sample_data, self._course.course_info)

    def test_searchStudentObjReturnsVal(self):
        # HAPPY path testing
        self._studentObj.name = 'Amir'
        student = self._course.search_student(self._studentObj)
        self.assertIsNotNone(student)

    def test_searchStudentObjReturnsNone(self):
        # SAD path testing
        self._studentObj.name = 'asdasd'
        student = self._course.search_student(self._studentObj)
        self.assertIsNone(student)

    def test_calcAvgReturnsVal(self):
        # HAPPY path testing
        self._studentObj.name = 'Amir'
        avg = self._course.calc_avg(self._studentObj)
        self.assertIsInstance(avg, float)

    def test_calAvgReturnsNone(self):
        self._studentObj.name = 'asdasd'
        with self.assertRaises(KeyError):
            avg = self._course.calc_avg(self._studentObj)
        