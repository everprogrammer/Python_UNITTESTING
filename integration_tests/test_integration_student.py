import unittest

from OOP_StudentCourse.course import Course
from OOP_StudentCourse.student import Student


"""
What should be tested?
- Are created objects of correct type?
- Association is implemented correctly? Does the StudentObj contain CourseObj
"""

class TestIntegrationStudent(unittest.TestCase):
    """
    setters/getters are usually tested in unittest
    """

    @classmethod
    def setUpClass(cls):
        cls._courseObj = Course()
        cls._studentObj = Student(cls._courseObj)

    def test_isObjectCorrectType(self):
        self.assertIsInstance(self._courseObj, Course)
        self.assertIsInstance(self._studentObj, Student)

    def test_studentContainsCourseObj(self):
        # breakpoint()
        self.assertIn('courseObj', self._studentObj.__dict__)
        self.assertIsInstance(self._studentObj.courseObj, Course)

    def test_getAvgReturnsVal(self):
        # Happy path testing
        self._studentObj.set_name('Amir')
        self.assertIsNotNone(self._studentObj.get_avg())
        
    def test_getAvgRaisesError(self):
        # Sad path testing
        self._studentObj.set_name('asdasd')
        with self.assertRaises(KeyError):
            self._studentObj.get_avg()

    def test_getAvgVerbose(self):
        """
        Testing boiler-plate (has extra logic): should be unit/integration tested
        """
        student_ls_gr = {'Amir': 'A', 'John': 'B', 'Claire': 'C', 'James': 'F'}

        # HAPPY path testing
        for name in student_ls_gr:
            self._studentObj.set_name(name)
            grade = self._studentObj.get_avg_verbose()
            self.assertEqual(grade, student_ls_gr[name])

        # SAD path testing
        self._studentObj.set_name('asdasd')
        with self.assertRaises(KeyError):
            grade = self._studentObj.get_avg_verbose()