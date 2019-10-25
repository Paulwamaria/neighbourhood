from django.shortcuts import render


def index(request):
    message = "Hello World"
    context = {
        "message":message
    }

    return render(request,'neighbourhood/index.html',context)

