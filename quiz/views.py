from django.shortcuts import render
from .models import Questions

def index(request):
        '''This function collects the questons'''
        questions = Questions.objects.all()
        return render(request, 'question.html', {'questions': questions})

def score(request):
        questions = Questions.objects.all()
        score = 0
        for question in questions:
            if question.mark == 0:
                return render(request, 'question.html', {'questions': questions, 'error_message': "You are not answered these questions."})
            else:
                score += question.mark 
        return render(request, 'score.html', {'questions': questions, 'score': score})


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
        
