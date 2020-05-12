from django.db import models
import uuid
from colorfield.fields import ColorField

# Create your models here.

WEEKDAY = [
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
]



class Teacher(models.Model):
    short_name = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    imageUrl = models.ImageField(upload_to='files')

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def natural_key(self):
        return ({'short_name': self.short_name, 'name': self.name})
    
    def __str__(self):
        return self.name



class Schedule(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    place = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    startTime = models.TimeField(auto_now=False, auto_now_add=False)
    endTime = models.TimeField(auto_now=False, auto_now_add=False)
    weekDay = models.IntegerField(choices=WEEKDAY)
    appointment_id = models.UUIDField(default=uuid.uuid4)
    service_id = models.UUIDField(default=uuid.uuid4)
    pay = models.BooleanField()
    appointment = models.BooleanField()
    teacher_v2 = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True)
    color = ColorField(default='#FFC0CB')
    availability = models.IntegerField()

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedule"
