from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import random

# Create your views here.
# @login_required
def home(request):
    user = request.user
    blogs = Blogs.objects.all()
    
    return render(request, "blogFiles/index.html", context = {'user': user, 'blogs':blogs})

def showBlogs(request):

    blogs = Blogs.objects.filter(creater_id = request.user.id)
    return render(request, "blogFiles/yourBlogs.html", context = {'blogs': blogs})

def showOneBlog(request, id):
    colors = ["lightred", "pink", "lightgray", "lightblue"]
    color = colors[random.randint(0, 3)]
    if request.method == "GET":
        # print(id)
        blog = Blogs.objects.get(id = id)
        user = User.objects.get(email = blog.creater)
        return render(request, "blogFiles/showOneBlog.html" , context = {'blog': blog, 'user':user, 'color':color})
    return render(request, "blogFiles/showOneBlog.html" , context = {'blog': blog})


def addBlog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        new_blog = Blogs.objects.create(
            title = title,
            description = description,
            image = image,
            creater = request.user
        )
        new_blog.save()
        return redirect("/your-blogs")
    return render(request, "blogFiles/addBlog.html")

def deleteBlog(request, id):
    blog = Blogs.objects.get(id = id)
    blog.delete()
    return redirect('/your-blogs')

def updateBlog(request, id):
    blog = Blogs.objects.get(id = id)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get("description")
        image = request.FILES.get("image")

        blog.title = title
        blog.description = description
        blog.image = image
        blog.save()
        return redirect("/your-blogs")
    return render(request, "blogFiles/updateBlog.html", context={"blog": blog})

