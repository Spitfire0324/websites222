from django.shortcuts import render
from django.http import HttpResponse

data = {
         'title': "Main page"

}

def index(request):
    return render(request,'main/index.html',data)
def about(request):
    return render(request , 'main/about.html')



