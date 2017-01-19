from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.generic import View
from .models import User, Questions
from .forms import UserForm

def index(request):
        '''This function collects the questons'''
        questions = Questions.objects.all()
        return render(request, 'question.html', {'questions': questions})
def signup(request):
    questions = Questions.objects.all()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            ##username = request.POST.get('username', '')
            ##email = request.POST.get('email', '')
            ##password = request.POST.get('password', '')
            ##user_obj = User(username=username, email=email, password=password)
            ##user_obj.save()
            return render(request, 'question.html', {'questions': questions})

    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form}) 

@login_required
def score(request):
        usernames = User.objects.all()
        questions = Questions.objects.all()
        ##current_user = request.user
        score = 0
        for users in usernames:
            if users.username == request.user.username:
                ##print(users.mark)
                return render(request, 'score.html', {'usernames': usernames, 'questions': questions})
        return render(request, 'question.html', {'questions': questions, 'error_message': "You are not answered these questions."})
                

@login_required
def result(request):
        usernames = User.objects.all()
        questions = Questions.objects.all()
        ##current_user = request.user
        '''The function mark will collect selected answers and check is it correct or not,
           if it is correct the mark is incrimented by one otherwise decremented by 0.25 and
           return the mark '''
        for users in usernames:
            if users.username == request.user.username:
                return render(request, 'question.html', {'usernames': usernames, 'error_message': "You are already answered these questions."})   
        mark = 0
        a=[]
        for question in questions:
            ##print(question)
            user_selection = request.POST.get(str(question.id))
            ##print(user_selection)
            if user_selection:
                question.choice = user_selection
                a.append(user_selection)
                if(user_selection == question.answer):
                        mark += 1
                else:
                        mark -= 0.25
            else:
                question.choice = "Answer is not selected!"
                a.append("Answer is not selected!")
                mark -= 0.25
            question.save()
        ##choice = "answered"
                ##user_obj = User(username=username, email=email, password=password)
        user_obj = User(username=request.user.username,choice=a, mark=mark)
        user_obj.save()
            
        
        return render(request, 'result.html', {'user_obj': user_obj, 'questions': questions})
        
