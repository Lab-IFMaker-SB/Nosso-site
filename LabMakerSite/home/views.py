from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req, './home/index.html')

def about(req):
    return render(req, './about/about.html')

def projects(req):
    return render(req, './projects/projects.html')

def courses(req):
    return render(req, './courses/courses.html')

def activities(req):
    return render(req, './activities/activities.html')

def contact(req):
    return render(req, './contact/contact.html')