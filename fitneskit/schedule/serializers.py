from rest_framework import serializers
from .models import Schedule, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    teacher_v2 = TeacherSerializer(read_only=True)

    class Meta:
        model = Schedule
        exclude = ['id']
       

