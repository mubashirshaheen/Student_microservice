from rest_framework import serializers
from .models import Student, College, Course


class StudentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', False)
        super(StudentSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Student
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', False)
        super(CollegeSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = College
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', False)
        super(CourseSerializer, self).__init__(many=many, *args, **kwargs)



    class Meta:
        model = Course
        fields = '__all__'
