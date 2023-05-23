from django import forms
from . models import Notes, Homework, Todo, User #import Notes to bind
from django.contrib.auth.forms import UserCreationForm

#============== Notes Form Start ================
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes #bind Notes model form in here
        fields = ['title', 'description']#show only title and description not user field
#============== Notes Form End ================

#============== Homework Form Start ================
class DateInput(forms.DateInput):#forms DateInput object pass
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}#created DateInput class
        fields = ['subject', 'title', 'description', 'due', 'is_finished']
#============== Homework Form end ================

#============== Search Form start for youtube, books, dictionary, wiki ================
class DashboardSearchForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter your Search")

#============== Search Form end ================

#============== todo Form start ================
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']

#============== Search Form end ================
#============== Conversion Form start ================
class ConversionForm(forms.Form):
    CHOICES = [('length', 'Length'), ('mass', 'Mass')]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES = [('yard', 'Yard'), ('foot', 'Foot')]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput( #input field
        attrs = {'type': 'number', 'placeholder': 'Enter the number'}
    ))
    measure1 = forms.CharField(#two choices one is for yard
        label='', widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(#another is for converted for foot
        label='', widget = forms.Select(choices = CHOICES)
    )

class ConversionMassForm(forms.Form):
    CHOICES = [('pound', 'Pound'), ('kilogram', 'Kilogram')]
    input = forms.CharField(required=False, label=False, widget=forms.TextInput( #input field
        attrs = {'type': 'number', 'placeholder': 'Enter the number'}
    ))
    measure1 = forms.CharField(#two choices one is for yard
        label='', widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(#another is for converted for foot
        label='', widget = forms.Select(choices = CHOICES)
    )
#============== Conversion Form end ================
#============== Registraion Form start ================
class UserRegistationForm(UserCreationForm):#UserRegistationForm inherits UserCreationForm
    class Meta:
        model = User #User table
        fields = ['username', 'password1', 'password2']
