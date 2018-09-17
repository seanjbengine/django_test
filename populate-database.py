import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_django.settings')

import django
django.setup()

import random
from schooler.models import School, Student
from faker import Faker
from rest_framework.exceptions import ValidationError

fakegen = Faker()
schools = ['Stanford Thailand', 'Harvard Thailand', 'Yale Thailand', 'Princeton Thailand', 'New school']


def add_school():
    fake_city = fakegen.city()
    fake_max_students = random.randint(10, 20)
    school, created = School.objects.get_or_create(name=random.choice(schools), defaults={'city': fake_city, 'max_students': fake_max_students})
    return school


def populate(N=100):
    for entry in range(N):

        school = add_school()
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_address = fakegen.address()

        try:
            Student.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, defaults={'address': fake_address, 'school': school})
        except ValidationError:
            pass


if __name__ == '__main__':
    print(Student.objects.count())
    populate(N=500)
    print(Student.objects.count())
