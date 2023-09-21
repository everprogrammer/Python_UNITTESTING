import unittest
from OOP_StudentCourse.student import Student
import mock
"""
What should be tested?
- Is this class instantiable?
"""

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        courseMockedObj = mock.Mock()
        cls._student = Student(courseMockedObj) 

    def test_canCreateObj(self):
        # Happy path testing
        s = Student('Dummy')
        # Sad path testing
        with self.assertRaises(TypeError):
            Student()

    def test_setName(self):

        """
        Testing setters/getters in unit/integration testing can be skipped
        """
        self._student.set_name('John')
        self.assertEqual(self._student.name, 'John')

    def test_getAvg(self):
        """
        Testing boiler-plate (has not extra logic): should be skipped in unittest
            - mocking takes time
        """
        self._student.courseObj.calc_avg.return_value = True
        self.assertIsNotNone(self._student.get_avg)

    def test_getAvgVerbose(self):
        """
        Testing boiler-plate (has extra logic): should be unit/integration tested
            - mocking takes time
        """
        # values, 19, 16, 12, and 8 are assigned to the courseObj as iterable
        self._student.courseObj.calc_avg.side_effect = [19, 16, 12, 8]
        # grade = self._student.get_avg_verbose() # first time -> 9
        # breakpoint()
        lst = ['A', 'B', 'C', 'F']
        idx = 0
        for _ in range(4):
            grade = self._student.get_avg_verbose()
            self.assertEqual(grade, lst[idx])
            idx += 1

