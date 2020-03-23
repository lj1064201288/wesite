from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import RedirectView
# Create your views here.



class Myview(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello Wrold111!')


# def ase(request):
#     return HttpResponse('Hello World!')