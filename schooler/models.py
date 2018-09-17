import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError


class School(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(default='', blank=True, max_length=200)
    max_students = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @property
    def student_count(self):
        return self.students.count()


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(default='', blank=True, max_length=250)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    student_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def school_name(self):
        return str(self.school)

    def __str__(self):
        return self.full_name


@receiver(pre_save, sender=Student)
def student_pre_save(sender, instance, **kwargs):
    if instance.school.students.count() >= instance.school.max_students:
        raise ValidationError(f'No room left for {instance} at {instance.school}')
