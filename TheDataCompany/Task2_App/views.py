from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Student, Branch
from .forms import StudentForm
from django.shortcuts import render

def task(request):
    return render(request,'Task2_App/Taskpage.html')

class StudentListView(ListView):
    model = Student
    form_class = StudentForm
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_changelist')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm  
    success_url = reverse_lazy('student_changelist')

def load_branches(request):
    college_id = request.GET.get('college')
    branches = Branch.objects.filter(college_id=college_id).order_by('name')
    return render(request, 'Task2_App/branch_dropdown_list_options.html', {'branches': branches})
