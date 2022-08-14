from django.urls import path
from .views import VacancyView, VacancyNewFormView


urlpatterns = [
    path('vacancies/', VacancyView.as_view(), name='vacancies'),
    path('vacancy/new', VacancyNewFormView.as_view(), name='new_vacancy'),
]