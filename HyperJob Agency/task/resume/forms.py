from django.forms import ModelForm
from .models import Resume


class ResumeModelForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['description']
