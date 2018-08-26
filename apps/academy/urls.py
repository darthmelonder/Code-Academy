from django.urls import path
from . import views
urlpatterns = [
	path('',views.index,name="index"),
	path('profile/', views.profile, name="profile"),
	path('register/', views.register, name='register'),
	path (r'verify/',views.verify,name="verify"),
	path(r'problems/',views.problems,name='problems'),
	path(r'submit/',views.submit,name='submit'),
	path(r'question/<int:problem_id>', views.question, name='question'),
	path(r'(?P<error_message>)/',views.index,name='index'),
	path(r'register/(?P<error_message>)/',views.register,name='register'),
]