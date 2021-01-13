from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=30)
    year = models.CharField(max_length=15)


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subjects = models.ManyToManyField(Subject, through='StudentSubject')


class StudentSubject(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.FloatField()
