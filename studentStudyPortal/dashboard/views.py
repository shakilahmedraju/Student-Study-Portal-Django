from django.shortcuts import render, redirect
from .models import Notes, Homework, Todo
from . forms import NotesForm, HomeworkForm, DashboardSearchForm, TodoForm, ConversionForm, ConversionLengthForm, ConversionMassForm, UserRegistationForm
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
import requests
import wikipedia
from django.contrib.auth.decorators import login_required

# Create your views here.
#========================= Home Part start =============================
def home(request):
    return render(request, 'dashboard/home.html')#appname/filename
#========================= Home Part end =============================


#========================= Notes Part start =============================
@login_required
def notes(request):
    if request.method == "POST":#until click on submit btn
        form = NotesForm(request.POST)#pass POST into the object
        if form.is_valid():#form field validation
            notes = Notes(user=request.user, title=request.POST['title'], description=request.POST['description'])
            notes.save()#save the value in table
        messages.success(request, f"Notes Added from {request.user.username}")
    else:
        form = NotesForm()#show before clicking on submit btn
    
    notes = Notes.objects.filter(user=request.user)#object created and request.user loginned user
    context = {
        'notes': notes, 
        'form':form
        }#dictionary created and dic name used in html template
    return render(request, 'dashboard/notes.html', context)#pass the object 

@login_required
def delete_note(request, pk=None):#primarykey none [get id when click url]
    Notes.objects.get(id=pk).delete()#id is Notes table column value
    return redirect('notes')


class NotesDetailView(generic.DetailView):#generic object pass Detailview
    model = Notes #show details from Notes table

#========================= Notes Part end =============================

#========================= HomeWork Part start =============================
@login_required
def homework(request):

    if request.method == "POST":##if click on submit button
        form = HomeworkForm(request.POST)#created object of form and pass POST
        if form.is_valid():            
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except: 
                finished = False
            homework = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished
            )
            homework.save()
            messages.success(request, f'Homework added from {request.user}!!')

    else:
        form = HomeworkForm()#if not click submit button just show the form
    
    homework = Homework.objects.filter(user=request.user)#object of model

    if len(homework) == 0:#number of homework table 
        homework_done = True
    else:
        homework_done = False    

    context = {
        'homeworks': homework,
        'homework_done': homework_done,
        'form': form
        }  
    return render(request, 'dashboard/homework.html', context)


@login_required
def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)#id is Homework table pk is primary key   
    
    if homework.is_finished == True:        
        homework.is_finished == False        
    else:        
        homework.is_finished == True   
        
    homework.save()#save the update in database
    messages.success(request, f'Checkbox updated successfully from {request.user}!!')
    return redirect('homework')


@login_required
def delete_homework(request, pk=None):
    Homework.objects.get(id=pk).delete()
    messages.success(request, f'Deleted item successfully')
    return redirect('homework')

#========================= HomeWork Part end =============================

#========================= Youtube Part start =============================
def youtube(request):
    if request.method == "POST":
        form = DashboardSearchForm(request.POST)#pass POST through DashboardSearchForm
        text = request.POST['text'] #'text' is name we given in DashboardSearchForm[forms.py]
        video = VideosSearch(text, limit=10)#limit 10 result show
        #print(video.result())
        result_list = []#emty list
        for i in video.result()['result']:
            result_dict = {
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'thumbnail': i['thumbnails'][0]['url'],
                'channel': i['channel']['name'],
                'link': i['link'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime'],
                #'desc': i['descriptionSnippet']['text']
            }
            desc = ''#emty string
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']#concate multiple text [text is from descriptionSnippet]
            result_dict['description'] = desc
           
            result_list.append(result_dict)
            context = {
                'form': form,
                'results':result_list
            }
            #print(result_list)
        return render(request, 'dashboard/youtube.html', context)
    else:
        form = DashboardSearchForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/youtube.html', context)

#========================= Youtube Part end =============================

#========================= todo Part start =============================
@login_required
def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished == request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            todos = Todo(
                user = request.user,
                title = request.POST['title'],
                is_finished = finished
            )
            todos.save()
            messages.success(request, f'Todo added from {request.user.username} successfully!!')
    else:
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)

    if len(todo) == 0:
        todos_done = True
    else:
        todos_done = False

    context = {
        'todos': todo,
        'form': form,
        'todos_done': todos_done
    }
    return render(request, 'dashboard/todo.html', context)

@login_required
def update_todo(request, pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished == False
    else:
        todo.is_finished == True
    todo.save()
    messages.success(request, f'Todo updated successfully!!')
    return redirect('todo')

@login_required
def delete_todo(request, pk=None):
    todo = Todo.objects.get(id=pk).delete()
    messages.success(request, f'Todo deleted successfully!!')
    return redirect('todo')

#========================= todo Part end =============================

#========================= books Part start =============================
def books(request):
    if request.method == 'POST':
        form = DashboardSearchForm(request.POST)
        text = request.POST['text']#'text' is name in DashboardSearchForm class
        url = 'https://www.googleapis.com/books/v1/volumes?q='+text
        r = requests.get(url)#pip install requests [import requests]
        answer = r.json()#json object
        result_list = []
        for i in range(10):
            result_dict = {
                #annswer json object i is item er 1, 2, 3....
                #https://developers.google.com/books/docs/v1/using                
                'title': answer['items'][i]['volumeInfo']['title'], 
                'subtitle': answer['items'][i]['volumeInfo'].get('subtitle'),
                'description': answer['items'][i]['volumeInfo'].get('description'),
                'count': answer['items'][i]['volumeInfo'].get('count'),
                'categories': answer['items'][i]['volumeInfo'].get('categories'), 
                'rating': answer['items'][i]['volumeInfo'].get('rating'),
                'thumbnail': answer['items'][i]['volumeInfo']['imageLinks'].get('thumbnail'), 
                'preview': answer['items'][i]['volumeInfo'].get('previewLink'),
            }
            result_list.append(result_dict)
            context = {
                'form': form,
                'results': result_list
            }
        return render(request, 'dashboard/books.html', context)

    else:
        form = DashboardSearchForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/books.html', context)

#========================= books Part end =============================

#========================= dictionary Part start =============================
def dictionary(request):
    if request.method == 'POST':
        form = DashboardSearchForm(request.POST)
        text = request.POST['text'] #'text' is a name of form DashboardForm
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+text
        r = requests.get(url)#pip install requests [import requests]
        answer = r.json()#json object
        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context = {
                'form': form,
                'input': text,
                'phonetics': phonetics,
                'audio': audio,
                'definition': definition,
                'example': example,
                'synonyms': synonyms
            }
        except:
            context = {
                'form': form,
                'input': '',
            }
        return render(request, 'dashboard/dictionary.html', context)
    else:
        form = DashboardSearchForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/dictionary.html', context)
#========================= dictionary Part end =============================

#========================= wikipedia Part start =============================
def wiki(request):
    if request.method == 'POST':
        form = DashboardSearchForm(request.POST)
        text = request.POST['text']#'text' is a name of form DashboardForm
        search = wikipedia.page(text)
        context = {
            'form': form,
            'title': search.title,
            'link': search.url,
            'details': search.summary
        }
        return render(request, 'dashboard/wiki.html', context)
    else:
        form = DashboardSearchForm()
        context = {    
            'form': form
            }
    return render(request, 'dashboard/wiki.html', context)

#========================= wikipedia Part end =============================

#========================= Conversion Part start =============================
def conversion(request):
    if request.method == 'POST':
        #this part is submit form 1st form
        form = ConversionForm(request.POST)
        if request.POST['measurement'] == 'length':
            measurement_form = ConversionLengthForm()
            context = {
                'form': form,
                'm_form': measurement_form,
                'input': True #name in ConversionLengthForm
            }
            #this part is conversion submit form 2nd form
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first == 'yard' and second == 'foot':
                        answer = f'{input} yard = {int(input)*3} foot'
                    if first == 'foot' and second == 'yard':
                        answer = f'{input} foot = {int(input)/3} foot'
                context = {
                    'form': form,
                    'm_form': measurement_form,
                    'input': True,
                    'answer': answer
                }
                
        #this part is submit form 1st form
        if request.POST['measurement'] == 'mass':
            measurement_form = ConversionMassForm()
            context = {
                'form': form,
                'm_form': measurement_form,
                'input': True #name in ConversionLengthForm
            }
            #this part is conversion submit form 2nd form
            if 'input' in request.POST:#if sec
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first == 'pound' and second == 'kilogram':
                        answer = f'{input} pound = {int(input)*0.453592} kilogram'
                    if first == 'kilogram' and second == 'pound':
                        answer = f'{input} kilogram = {int(input)*2.20462} pound'
                context = {
                    'form': form,
                    'm_form': measurement_form,
                    'input': True,
                    'answer': answer
                }
                
    else:
        form = ConversionForm()
        context = {
        'form': form,
        'input': False
        }
    return render(request, 'dashboard/conversion.html', context)

#========================= Conversion Part end =============================

#========================= Registration, profile, logout Part start =============================
def register(request):
    if request.method == 'POST':
        form = UserRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')#if form is validated we can access value by cleaned_data
            messages.success(request, f'Account created for {username}!!')
            return redirect('login') #after registration redirect to login
    else:
        form = UserRegistationForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/register.html', context)

@login_required
def profile(request):
    #filter by not finished rows
    homeworks = Homework.objects.filter(is_finished=False, user=request.user)
    todos = Todo.objects.filter(is_finished=False, user=request.user)
    if len(homeworks) == 0:#check is there any filterd row
        homework_done = True
    else:
        homework_done = False
    if len(todos) == 0:#check is there any filterd row
        todo_done = True
    else:
        todo_done = False
    context = {
        'homeworks': homeworks,
        'todos': todos,
        'homework_done': homework_done,
        'todo_done': todo_done
    }

    return render(request, 'dashboard/profile.html', context)

def logout(request):
    return render(request, 'dashboard/logout.html')

#========================= Registration, profile, logout Part end =============================