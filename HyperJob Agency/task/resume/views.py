from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# ModelForm
from .forms import ResumeModelForm
from django.views.generic.edit import FormView


# Create your views here.
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        context = {'resumes': resumes}
        return render(request, 'resume/resume_template.html', context=context)


class ResumeNewFormView(FormView):
    def get(self, request, *args, **kwargs):
        resume_form = ResumeModelForm
        template_name = 'resume/resume_new.html'
        context = {'resume_form': resume_form}

        # Check if a staff member tries to create a resume. If so, then raise an exception
        if User().is_staff:
            return HttpResponseForbidden(status=403)
        else:
            return render(request, template_name, context=context)

    def post(self, request, *args, **kwargs):
        resume_form = ResumeModelForm(request.POST)

        if not User().is_staff:
            if resume_form.is_valid():
                # Extract data from a form
                data = resume_form.cleaned_data['description']
                # Take user object and save it before assigning it to the new resume
                user = request.user
                user.save()

                # Save data to the database
                create_resume = Resume(description=data, author=user)
                create_resume.save()

                success_url = '/home'
                return redirect(success_url)
        else:
            return HttpResponseForbidden(status=403)
