from .models import Student, Subject, StudentSubject
from typing import List
# from django.db.models import Q


class SchoolDB():
    # def _get_or_create_student(
    #     self,
    #     name: str,
    #     last_name: str
    # ) -> Student:
    #     """Access to the student data on the db and created if it does not
    #     exist.

    #     Args:
    #         name (str): Name of the student  to be obtained/created.
    #         last_name (str): Last name of the student to be obtained/created.

    #     Returns:
    #         Student: Student entry of the table, either the one obtained or
    #         the one created.
    #     """

    #     if not self._student_on_db(name=name, last_name=last_name):
    #         new_student = Student.objects.create(name=name, last_name=last_name)
    #     else:
    #         new_student = Student.objects.all().filter(name=name, last_name=last_name)

    #     return new_student

    # def _student_on_db(
    #     name: str, last_name: str
    # ) -> bool:
    #     """Check if the student data is already in the db.

    #     Args:
    #         name (str): Name of the student to check.
    #         last_name (str): Last name of the student to check.

    #     Returns:
    #         bool: Whether the data exists in the db.
    #     """
    #     return Student.objects.all().filter(name=name, last_name=last_name).count() != 0

    # def _get_or_create_subject(
    #     self, subject: str, year: str
    # ) -> Subject:
    #     """Access to the subject data on the db and created if it does not
    #     exist.

    #     Args:
    #         subject (str): Name of the subject to be added to the db.s on
    #         the db.

    #     Returns:
    #         Subject: Subject entry of the table, either created or obtained.
    #     """
    #     if not self._subject_on_db(subject=subject, year=year):
    #         new_subject = Subject.objects.create(subject=subject, year=year)
    #     else:
    #         new_subject = Subject.objects.all().filter(subject=subject, year=year)

    #    return new_subject

    # def _subject_on_db(
    #     subject: str, year: str
    # ) -> bool:
    #     """Check if the subject data is already in the db.

    #     Args:
    #         subject (str): Name of the subject to check.
    #         year (str): Year on which the subject was taught, to check.

    #     Returns:
    #         bool: Whether the subject entry already exists in the db.
    #     """
    #     return Subject.objects.all().filter(subject=subject, year=year).count() != 0

    # def _student_subject_on_db(
    #     name: str,
    #     last_name: str,
    #     subject: str,
    #     year: str,
    #     mark: float
    # ) -> bool:
    #     """Check if the pairing student-subject already exists in the db.

    #     Args:
    #         name (str): Name of the student to check.
    #         last_name (str): Last name of the student to check.
    #         subject (str): Name of the subject to check.
    #         year (str): Year when the student took the subject, to check.
    #         mark (float): Mark the student has on the subject, to check.

    #     Returns:
    #         bool: Whether the pairing student-subject already exists in db.
    #     """
    #     pass

    def store_data_in_db(
        self, name: str, last_name: str, subject: str, year: str, mark: float,
    ) -> None:
        """Store the data in the db after checking that it does not already
        exist.

        Args:
            name (str): Name of the student to add to the db.
            last_name (str): Last name of the student to add to the db.
            subject (str): Name of the subject to add to the db.
            year (str): Year when the student took the subject to add to
            the db.
            mark (float): Mark the student got on the subject to add to
            the db.
        """
        student, student_created = Student.objects.update_or_create(name=name, last_name=last_name)
        student.subjects.update_or_create(name=subject, year=year, mark=mark)

    def get_number_passed_by_subject_and_year(
        self, subject: str, year: str
    ) -> int:
        """Get number of students that got a mark equal or greater than
        5 on a given subject on a given year.

        Args:
            subject (str): Name of the subject to consult.
            year (str): Year the subject was taught to consult.

        Returns:
            int: Number of students that passed the subject in the given year
                as an answer for the query.
        """
        # return Student.objects.filter(Q(Student__subjects__name=subject) & Q(Student__subjects__year=year) & Q(StudentSubject__mark >= 5)).count()
        pass

    def get_number_failed_by_subject_and_year(
        self, subject: str, year: str
    ) -> int:
        """Get number of students that got a mark less than 5 on a given
        subject on a given year.

        Args:
            subject (str): Name of the subject to consult.
            year (str): Year the subject was taught to consult.

        Returns:
            int: Number of students that failed the subject in the given year
                as an answer for the query.
        """
        # return Student.objects.filter(Q(Student__subjects__name=subject) & Q(Student__subjects__year=year) & Q(Student__subjects__mark < 5)).count()
        pass

    def get_list_passed_by_subject_and_year(
        self, subject: str, year: str
    ) -> List[str]:
        """Get list of students that got a mark equal or greater than 5 on a
        given subject on a given year.

        Args:
            subject (str): Name of the subject to consult.
            year (str): Year the subject was taught to consult.

        Returns:
            List[str]: List of names and last named of students that passed
                the subject on a given year.
        """
        pass

    def get_list_failed_by_subject_and_year(
        self, subject: str, year: str
    ) -> List[str]:
        """Get list of students that got a mark less than 5 on a given subject
        on a given year.

        Args:
            subject (str): Name of the subject to consult.
            year (str): Year the subject was taught to consult.

        Returns:
            List[str]: List of names and last named of students that failed
                the subject on a given year.
        """
        pass

    def get_list_students_by_subject_and_year(
        self, subject: str, year: str
    ) -> List[str]:
        """Get list of students that were enrolled on a given subject on a
        given year.

        Args:
            subject (str): Name of the subject to consult.
            year (str): Year the subject was taught to consult.

        Returns:
            List[str]: List of names and last named of students that were
                enrolled on a subject in a given year.
        """
        pass

    def get_number_students_by_subject_and_year(
        self, subject: str, year: str
    ) -> int:
        """Get the number of students that were enrolled on a subject in a
        given year.

        Args:
            subject (str): Name of the subject to consult.
            year (str): Year the subject was taught to consult.

        Returns:
            int: number of students that were enrolled on a subject in a
                given year.
        """
        pass

    def get_list_subjects_by_year(self, year: str) -> List[str]:
        """Get the list of subjects taught in a given year.

        Args:
            year (str): Year to obtain the data from.

        Returns:
            List[str]: Response from the query to the db with the subjects
                that have an entrance with that year.
        """
        pass
