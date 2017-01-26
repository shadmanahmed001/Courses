from django.shortcuts import render, redirect
from . import models
def index(request):
    context = {
    'courses' : models.Course.objects.all()
    }
    return render (request, "courses_app/index.html", context)

def process(request):
    if request.method == 'POST':
        add_name = request.POST['addname']
        print add_name
        add_descript = request.POST['adddescript']
        print add_descript
        models.Course.objects.create(course_name= add_name, desc= add_descript)
        return redirect ('/')

def confirm (request, id):
    course_list=models.Course.objects.filter(id=id)
    course_list.delete()
    return redirect ('/')

# Create your views here.
