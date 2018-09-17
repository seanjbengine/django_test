from rest_framework import serializers
from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'city', 'student_count', 'max_students')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'student_uuid', 'first_name', 'address', 'last_name', 'school', 'school_name')


class StudentOfSchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'student_uuid', 'first_name', 'address', 'last_name', 'school', 'school_name')
        read_only_fields = ('school', )

    def create(self, validated_data):
        school = School.objects.get(pk=self.context['view'].kwargs['school_pk'])
        validated_data['school'] = school
        return super(StudentOfSchoolSerializer, self).create(validated_data)
