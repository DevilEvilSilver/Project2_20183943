from django.urls import path
from .views import *

urlpatterns = [
    #account
    path('student_info', StudentInfoView.as_view()),
    path('personal_info', PersonalInfoView.as_view()),
    path('health_info', HealthInfoView.as_view()),
    path('parent', ParentListView.as_view()),
    path('parent/<int:parent_pk>', ParentDetailView.as_view()),
    path('achievement', AchievementListView.as_view()),
    path('achievement/<int:achievement_pk>', AchievementDetailView.as_view()),

    #timetable
    path('timetable', TimeTableView.as_view()),
    path('timetable/<int:course_pk>', TimeTableCourseView.as_view()),

    #grade
    path('grade/<int:school_year>/<int:term>', GradeListView.as_view()),

    #conduct
    path('conduct', ConductListView.as_view()),
    path('conduct/<int:conduct_pk>', ConductDetailView.as_view()),

    #file
    path('file', FileListView.as_view()),
    path('file/<int:course_pk>', FileCourseView.as_view()),
    path('file/<int:file_pk>', FileDetailView.as_view()),
]