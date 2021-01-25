from django.shortcuts import render
from django.views.generic.base import View

from .models import Work 
# Create your views here.

class WorkerView(View):
    #list work
    def get(self, request):
        works = Work.objects.all()
        return render(request, "work/work_list.html", {"worker_list": works})