

class Student():

    def __init__(self, courseObj):
        self.name = None
        self.courseObj = courseObj

    def set_name(self, name):
        self.name = name

    def get_avg(self):
        avg = self.courseObj.calc_avg(self)
        return avg

    def get_avg_verbose(self):
        avg = self.courseObj.calc_avg(self)

        if avg > 18: 
            grade = 'A'
        elif avg >= 15:
            grade = 'B'
        elif avg >= 10:
            grade = 'C'
        else:
            grade = 'F'
        return grade

        
