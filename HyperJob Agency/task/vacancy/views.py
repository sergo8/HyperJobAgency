from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# ModelForm
from .forms import VacancyModelForm
from django.views.generic.edit import FormView


# Create your views here.
class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        context = {'vacancies': vacancies}
        return render(request, 'vacancy/vacancy_template.html', context=context)


class VacancyNewFormView(FormView):
    def get(self, request, *args, **kwargs):
        vacancy_form = VacancyModelForm
        template_name = 'vacancy/vacancy_new.html'
        context = {'vacancy_form': vacancy_form}

        # Check if a regular user tries to create a vacancy. If so, then raise an exception
        if not User().is_staff:
            return HttpResponseForbidden(status=403)
        else:
            return render(request, template_name, context=context)

    def post(self, request, *args, **kwargs):
        vacancy_form = VacancyModelForm(request.POST)

        if User().is_staff:
            if vacancy_form.is_valid():
                # Extract data from a form
                data = vacancy_form.cleaned_data['description']
                # Take user object and save it before assigning it to the new resume
                user = request.user
                user.save()

                # Save data to the database
                create_vacancy = Vacancy(description=data, author=user)
                create_vacancy.save()

                success_url = '/home'
                return redirect(success_url)
        else:
            return HttpResponseForbidden(status=403)
