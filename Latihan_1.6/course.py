from course_record import CourseRecord
from not_yet_set_exception import NotYetSetException


class Course:
    PASSING_MARK = 60
    FINAL_EXAM_MIN_AVERAGE = 60

    def __init__(self, title=""):
        self.title = title
        self.course_records = []

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def add_course_record(self, course_record):
        self.course_records.append(course_record)

    def get_course_records(self):
        return iter(self.course_records)

    @staticmethod
    def _average(record):
        marks = []
        for assignment in record.get_assignments():
            try:
                marks.append(assignment.get_mark())
            except NotYetSetException:
                continue
        return sum(marks) / len(marks) if marks else None

    def print_course_students(self):
        """Cetak semua mahasiswa yang mengambil mata kuliah ini."""
        print(f"Daftar mahasiswa pada mata kuliah: {self.title}")
        if not self.course_records:
            print("Belum ada mahasiswa.")
            return

        for number, record in enumerate(self.course_records, start=1):
            student = record.get_student()
            name = student.get_name() if student else "(nama belum diisi)"
            print(f"{number}. {name}")

    def print_best_student(self):
        """Cetak mahasiswa dengan nilai rata-rata terbaik."""
        results = []
        for record in self.course_records:
            average = self._average(record)
            if average is not None:
                student = record.get_student()
                name = student.get_name() if student else "(nama belum diisi)"
                results.append((name, average))

        print(f"Mahasiswa dengan nilai rata-rata terbaik - {self.title}")
        if not results:
            print("Belum ada nilai yang bisa dihitung.")
            return

        best_average = max(average for _, average in results)
        for name, average in results:
            if average == best_average:
                print(f"{name}: rata-rata {average:.2f}")

    def print_final_exam_students(self):
        """Cetak mahasiswa yang layak mengikuti ujian akhir (rata-rata >= 60)."""
        print(f"Mahasiswa yang layak mengikuti ujian akhir - {self.title}")
        found = False
        for record in self.course_records:
            average = self._average(record)
            if average is not None and average >= self.FINAL_EXAM_MIN_AVERAGE:
                student = record.get_student()
                name = student.get_name() if student else "(nama belum diisi)"
                print(f"{name}: rata-rata {average:.2f}")
                found = True

        if not found:
            print("Belum ada mahasiswa yang memenuhi syarat.")
