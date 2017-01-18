from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.generic import View
from .models import Questions
from .forms import UserForm

def index(request):
        '''This function collects the questons'''
        questions = Questions.objects.all()
        return render(request, 'question.html', {'questions': questions})
def register(request):
    questions = Questions.objects.all()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return render(request, 'question.html', {'questions': questions})

    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form}) 

@login_required
def score(request):
        questions = Questions.objects.all()
        score = 0
        for question in questions:
            if question.mark == 0:
                return render(request, 'question.html', {'questions': questions, 'error_message': "You are not answered these questions."})
            else:
                score += question.mark 
        return render(request, 'score.html', {'questions': questions, 'score': score})

@login_required
def result(request):
        questions = Questions.objects.all()
        
        '''The function mark will collect selected answers and check is it correct or not,
           if it is correct the mark is incrimented by one otherwise decremented by 0.25 and
           return the mark '''
        score = 0
        for question in questions:
            if question.mark != 0:
                return render(request, 'question.html', {'questions': questions, 'error_message': "You are already answered these questions."})
            else:
                user_selection = request.POST.get(str(question.id))
                if user_selection:
                    question.choice = user_selection
               
                    if(user_selection == question.answer):
                            question.mark += 1
                    else:
                            question.mark -= 0.25
                else:
                    question.choice = "Answer is not selected!"
                
                    question.mark -= 0.25
                question.save()
        for question in questions:
            score += question.mark 
        return render(request, 'result.html', {'questions': questions, 'score': score})
        
