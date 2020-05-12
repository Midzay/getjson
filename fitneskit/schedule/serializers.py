from rest_framework import serializers
from .models import Schedule, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ['id']


class ScheduleSerializer(serializers.ModelSerializer):
    teacher_v2 = TeacherSerializer(read_only=True)
    startTime = serializers.TimeField(format="%H.%M")
    endTime = serializers.TimeField(format="%H.%M")
    class Meta:
        model = Schedule
        exclude = ['id']
       

