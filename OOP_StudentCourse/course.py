


class Course():

    def __init__(self):
        self.course_info = [
            {
                's_name': 'Amir',
                'midterm_mark': 18,
                'final_mark': 20
            },
            {
                's_name': 'John',
                'midterm_mark': 15,
                'final_mark': 17
            },
            {
                's_name': 'James',
                'midterm_mark': 20,
                'final_mark': 17
            },
            {
                's_name': 'Claire',
                'midterm_mark': 15,
                'final_mark': 12
            },
            ]
    
    def search_student(self, studentObj):
        for student in self.course_info:
            if student['s_name'] == studentObj.name:
                return student
        return None
    
    def calc_avg(self, studentObj):
        student = self.search_student(studentObj)
        if not student:
            raise KeyError(f'Invalid name, {studentObj.name} does not exist!')
        return (student['midterm_mark'] + student['final_mark']) / 2