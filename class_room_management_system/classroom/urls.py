from django.urls import path
from .import views

urlpatterns = [
    path('primary',views.primary,name='primary'),
    path('login',views.loginPage, name='login'),
    path('register',views.registerPage, name='register'),
    path('logout',views.logoutUser,name="logout"),
    path('main',views.mainView,name='main'),
    path('home',views.homeView, name='home'),
    path('buildings',views.academicbuildings,name='buildings'),
    path('calender',views.calender_page,name='calender'),
    path('classrooms/<name>/<int:id>',views.classrooms_views,name='classrooms'),
    path('classroomdetail/<id>/<name>/',views.classroomdetailview,name='classroomdetail'),
    path('myschedule',views.my_schedule,name='myschedule'),
    path('delschedule/<id>/',views.del_my_schedule,name='delschedule'),
]