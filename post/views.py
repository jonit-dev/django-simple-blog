from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):  # index

    return render(request, "post/index.html")

def create(request):

    # fetch variables from form post/index.html

    title = request.POST['title']
    content = request.POST['content']

    return HttpResponse(title + "-" + content)

    # return render(request, 'post/create.html')