from django.urls import path
from .views import ResumeView, ResumeNewFormView


urlpatterns = [
    path('resumes/', ResumeView.as_view(), name='resumes'),
    path('resume/new', ResumeNewFormView.as_view(), name='new_resume'),
]