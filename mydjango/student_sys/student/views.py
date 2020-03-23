from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from .models import Student
from .forms import StudentForm
#
# def index(request):
#     students = Student.objects.all()
#     print(students)
#     return render(request, 'base.html', context={'students': students})


# def index(request):
#     students = Student.objects.all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             student = Student()
#             student.name = cleaned_data['name']
#             student.sex = cleaned_data['sex']
#             student.email = cleaned_data['email']
#             student.profession = cleaned_data['profession']
#             student.qq = cleaned_data['qq']
#             student.phone = cleaned_data['phone']
#             student.save()
#             return HttpResponseRedirect(reverse('index'))
#
#     else:
#         form = StudentForm()
#
#     context = {
#         'students' : students,
#         'form' : form,
#     }
#
#     return render(request, 'base.html', context=context)
#
#
# def index(request):
#     students = Student.get_sex_man()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
            # cleaned_data = form.cleaned_data
            # student = Student()
            # student.name = cleaned_data['name']
            # student.sex = cleaned_data['sex']
            # student.email = cleaned_data['email']
            # student.profession = cleaned_data['profession']
            # student.qq = cleaned_data['qq']
            # student.phone = cleaned_data['phone']
    #         form.save()
    #         return HttpResponseRedirect(reverse('index'))
    #
    # else:
    #     form = StudentForm()
    #
    # context = {
    #     'students': students,
    #     'form': form,
    # }
    #
    # return render(request, 'base.html', context=context)


class IndexView(View):
    template_name = 'base.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students,
        }

        return context


    def get(self,request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form,
        })

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        # print(form)

        if form.is_valid():
            # print(form)
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        # print(context['form'])

        return render(request, self.template_name, context=context)


