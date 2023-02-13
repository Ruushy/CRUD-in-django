from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Students
from .forms import studentForm
# Create your views here.
def index(request):
    students = Students.objects.all()
    return render(request, 'students/index.html' , {'students': students})

def view_stud(request , id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            nstudentNumber = form.cleaned_data['studentNumber']
            nfirst_name = form.cleaned_data['first_name']
            nlast_name = form.cleaned_data['last_name']
            nemail = form.cleaned_data['email']
            nfield_of_study = form.cleaned_data['field_of_study']
            ngpa = form.cleaned_data['gpa']
            
            new_student = Students (
                studentNumber = nstudentNumber,
                first_name = nfirst_name , 
                last_name = nlast_name , 
                email = nemail , 
                field_of_study = nfield_of_study , 
                gpa = ngpa
            )
            new_student.save()
            return render(request , 'students/add.html' , {
                'form' : studentForm(),
                'success': True
    
          })
    else :
        form = studentForm()
    return render(request , 'students/add.html' , {
                'form' : studentForm(),
     })
    
def edit(request , id):
    if request.method == "POST":
        student = Students.objects.get(pk=id)
        form = studentForm(request.POST , instance=student)
        if form.is_valid():
            form.save()
            return render(request , 'students/edit.html' , {
                'form': form ,
                'success': True
            })
    else :
        student = Students.objects.get(pk=id)
        form = studentForm(instance=student)
    return render(request , 'students/edit.html' , {
        'form': form
    })
def delete(request , id):
    if request.method == "POST":
        student = Students.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
    
            