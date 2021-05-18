from rest_framework.views import APIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from accounts.permissions import IsOwner

from rest_framework import status, serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import *

from students.models import Student, Parent
from teachers.models import Teacher
from school.models import Classroom, Course, Timetable, FileManage
from persons.models import Achievement
from django.contrib.auth import get_user_model

from students.serializers import StudentSerializer, StudentGradeSerializer, ParentSerializer, GradeSerializer
from school.serializers import ClassroomSerializer, CourseSerializer, TimetableSerializer, FileManageSerializer
from persons.serializers import AchievementSerializer
from students.utils import get_student, get_parent, get_grade, get_conduct
from teachers.utils import get_teacher
from school.utils import get_classroom, get_course, get_timetable, get_record, get_file
from persons.utils import get_achievement

#Account
class StudentInfoView(APIView):

    def get(self, request, student_pk):
        student = get_student(student_pk)
        # if IsOwner.has_object_permission(request=request, obj=student):
        serializer = StudentSerializer(student)
        return Response(serializer.data)

class PersonalInfoView(APIView):

    def get(self, request, student_pk):
        student = get_student(student_pk)
        serializer = PersonSerializer(student.person)
        return Response(serializer.data)

class HealthInfoView(APIView):

    def get(self, request, student_pk):
        student = get_student(student_pk)
        serializer = HealthSerializer(student.health)
        return Response(serializer.data)

class ParentListView(APIView):

    def get(self, request, student_pk):
        parent = Parent.objects.filter(students=student_pk)
        serializer = HealthSerializer(parent, many=True)
        return Response(serializer.data)

class ParentDetailView(APIView):

    def get(self, request, parent_pk):
        parent = get_parent(parent_pk)
        serializer = HealthSerializer(parent)
        return Response(serializer.data)

class AchievementListView(APIView):

    def get(self, request, student_pk):
        student = get_student(student_pk)
        achievement = Achievement.objects.filter(id=student.achievements)
        serializer = HealthSerializer(achievement, many=True)
        return Response(serializer.data)

class AchievementDetailView(APIView):

    def get(self, request, student_pk, achievement_pk):
        achievement = get_achievement(achievement_pk)
        serializer = HealthSerializer(achievement)
        return Response(serializer.data)

#TimeTable
class TimeTableView(APIView):

    def get(self, request, student_pk):
        student = get_student(student_pk)
        timetable = Timetable.objects.filter(classroom=student.classroom)
        serializer = TimetableSerializer(timetable, many=True)
        return Response(serializer.data)

class TimeTableCourseView(APIView):

    def get(self, request, student_pk, course_pk):
        student = get_student(student_pk)
        timetable = Timetable.objects.filter(classroom=student.classroom).filter(course=course_pk)
        serializer = TimetableSerializer(timetable)
        return Response(serializer.data)

#Grade
class GradeListView(APIView):

    def get(self, request, student_pk, school_year, term):
        grade_list = Grade.objects.filter(student=student_pk).filter(school_year=school_year).filter(term=term)
        serializer = GradeSerializer(grade_list)
        return Response(serializer.data)

#Conduct
class ConductListView(APIView):

    def get(self, request, student_pk):
        conduct = Conduct.objects.filter(student=student_pk)
        serializer = ConductSerializer(conduct, many=True)
        return Response(serializer.data)

class ConductDetailView(APIView):

    def get(self, request, student_pk, conduct_pk):
        conduct = get_conduct(conduct_pk)
        serializer = ConductSerializer(conduct)
        return Response(serializer.data)

#File
class FileListView(APIView):

    def get(self, request, student_pk):
        file = FileManage.objects.all()
        serializer = FileManageSerializer(file, many=True)
        return Response(serializer.data)

class FileCourseView(APIView):

    def get(self, request, student_pk, course_pk):
        file = FileManage.objects.filter(course=course_pk)
        serializer = FileManageSerializer(file, many=True)
        return Response(serializer.data)

class FileDetailView(APIView):

    def get(self, request, student_pk, file_pk):
        file = get_file(file_pk)
        serializer = FileManageSerializer(file)
        return Response(serializer.data)