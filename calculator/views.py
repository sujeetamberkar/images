from django.shortcuts import render
from .forms import ArithmeticForms
# Create your views here.

def welcomeCalculator(request):
    result = None
    if request.method == 'POST':
        form = ArithmeticForms(request.POST)
        if form.is_valid():
            num1 = int(form.cleaned_data['number1'])
            num2 = int(form.cleaned_data['number2'])
            opperation = form.cleaned_data['opperation']
            
            if opperation == 'add':
                result = num1 + num2
            elif opperation =='subtract':
                result = num1-num2
            elif opperation == 'multiply':
                result = num1*num2
            elif opperation == 'divide':
                if num2 != 0:
                    result = num1/num2
                else:
                    result = "Cannot Divide by 0"
                    
    else :
        form = ArithmeticForms()
    
    params = {
        'form':form,
        'result':result,
            }

    return render(request,'calculator/welcomeCalculator.html',params)