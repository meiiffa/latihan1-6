from assignment import Assignment
from course import Course
from course_record import CourseRecord
from student import Student
from not_yet_set_exception import NotYetSetException


def make_record(name, marks):
    student = Student(name)
    record = CourseRecord(student)
    for mark in marks:
        assignment = Assignment()
        assignment.set_mark(mark)
        record.add_assignment(assignment)
    return record


def main():
    course = Course("Implementasi dan Pengujian Sistem Informasi")

    course.add_course_record(make_record("sean", [85, 90, 88]))
    course.add_course_record(make_record("anna", [70, 75, 80]))
    course.add_course_record(make_record("james", [55, 65, 58]))

    empty_assignment = Assignment()
    try:
        empty_assignment.get_mark()
    except NotYetSetException as error:
        print(f"Contoh exception: {error}")

    print()
    course.print_course_students()
    print()
    course.print_best_student()
    print()
    course.print_final_exam_students()


if __name__ == "__main__":
    main()
