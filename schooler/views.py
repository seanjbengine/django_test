from django.shortcuts import render
from .models import School, Student
from rest_framework import viewsets, filters
from .serializers import SchoolSerializer, StudentSerializer, StudentOfSchoolSerializer
from .pagination import SchoolResultsSetPagination, StudentResultsSetPagination


def index(request):
    my_dict = {'insert_me': 'This is the schooler app...'}
    return render(request, 'schooler/index.html', context=my_dict)


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    pagination_class = SchoolResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter, )
    ordering_fields = ('name', 'city', )
    search_fields = ('name', )

    def get_queryset(self):
        return School.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    pagination_class = StudentResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter, )
    ordering_fields = ('first_name', 'last_name', )
    search_fields = ('first_name', )

    def get_queryset(self):
        return Student.objects.all()


class StudentOfSchoolViewSet(viewsets.ModelViewSet):
    serializer_class = StudentOfSchoolSerializer
    pagination_class = StudentResultsSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter, )
    ordering_fields = ('first_name', 'last_name', )
    search_fields = ('first_name', )

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])
