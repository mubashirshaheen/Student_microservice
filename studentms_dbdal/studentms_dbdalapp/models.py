from djongo import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_credit = models.IntegerField()
    course_subjects = models.CharField(max_length=15)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    student_name = models.CharField(max_length=100)
    student_course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    student_mail = models.EmailField()
    student_contact = models.CharField(max_length=20)
    student_gender = models.CharField(max_length=1, choices=GENDER, default='M')
    
    
    def __str__(self):
        return self.name
    

class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_mail = models.EmailField()
    college_contact = models.CharField(max_length=15)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None, related_name='student')
