from assignment import Assignment
from student import Student


class CourseRecord:
    def __init__(self, student=None):
        self.student = student
        self.assignments = []

    def get_student(self):
        return self.student

    def set_student(self, student):
        self.student = student

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignments(self):
        return iter(self.assignments)
