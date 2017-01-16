from django.shortcuts import render
from .models import Questions

def index(request):
        '''This function collects the questons'''
        questions = Questions.objects.all()
        return render(request, 'question.html', {'questions': questions})

def result(request):
	questions = Questions.objects.all()
	marks = mark(request, questions)
	return render(request, 'result.html', {'marks': marks})

def mark(request, questions):
        '''The function mark will collect selected answers and check is it correct or not,
           if it is correct the mark is incrimented by one otherwise decremented by 0.5 and
           return the mark '''
        marks = 0
        for question in questions:
                user_selection = request.POST.get(str(question.id))
                if(user_selection == question.answer):
                        marks += 1
                else:
                        marks -= 0.5
        return marks
        
