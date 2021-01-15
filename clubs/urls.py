
from django.urls import path

from clubs import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('clubs/', views.all_clubs, name='clubs'),


    path('socialclubs/<str:pk>', views.socialclubs, name='socialclubs'),
    path('socialclubsdef/', views.socialclubs_def, name='socialclubs_def'),
    path('announcements/<str:pk>', views.announcement, name='announcement'),
    path('posts/<str:pk>', views.post, name='post'),
    path('chat/<str:pk>', views.chat, name='chat'),
    path('surveys/<str:pk>', views.survey, name='survey'),
    path('discussions/<str:pk>', views.discussion, name='discussion'),


    path('message/', views.messages, name='message'),
    path('clubDetail/', views.clupDetail, name='clubDetail'),

    path('addpost/', views.addPost, name='addPost'),
    path('addevent/', views.addEvent, name='addEvent'),
    path('addsurvey/<str:pk>', views.addSurvey, name='addSurvey'),
    path('adddiscussion/', views.addDiscussion, name='addDiscussion'),
    path('join/', views.join, name='join'),
    path('report/', views.report, name='report'),

    path('userpage/', views.userPage, name='userpage'),

    path('eventpage/', views.eventPage, name='eventPage'),
    path('eventpagejoined/', views.eventPageJoined, name = 'eventPageJoined'),
    path('ccalendar/', views.ccalendar, name= 'ccalendar'),

]