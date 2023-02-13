from django import forms

from .models import Students

class studentForm(forms.ModelForm):
    class Meta:
       model = Students
       fields = ['studentNumber' , 'first_name' , 'last_name' , 'email', 'field_of_study' , 'gpa']
    #    labels = {
    #        'studentNumber' :'student number',
    #        'first_name' : 'first name',
    #        'last_name' : 'last name',
    #        'email' : 'Email',
    #        'field_of_study' : 'field of study',
    #        'gpa' : 'GPA', 
    #    }
       widgets = {
           'studentNumber' : forms.NumberInput(attrs={'class': 'form-control'}) ,
           'first_name' : forms.TextInput(attrs={'class': 'form-control'}) , 
           'last_name' : forms.TextInput(attrs={'class': 'form-control'}) , 
           'email' : forms.EmailInput(attrs={'class': 'form-control'}) ,
           'field_of_study' : forms.TextInput(attrs={'class': 'form-control'}),
           'gpa' : forms.NumberInput(attrs={'class': 'form-control'})
       }