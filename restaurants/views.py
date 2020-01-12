from django.shortcuts import render

# Create your views here.


def function_name(request):
    context ={
    'msg': 'Hello World!'
    }
    return render(request, 'task.html', context)

