from course import Course
from student import Student


# ======= INITIALIZATION ===========
courseObj = Course()
student = Student(courseObj)

# ======= DRIVER ===========
student.set_name('John')

print(student.get_avg_verbose())