from django.forms import ModelForm
from .models import Vacancy


class VacancyModelForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['description']
