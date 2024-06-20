from django.shortcuts import render, redirect
from .models import blog
from .forms import blogform
from django.contrib.auth.decorators import login_required

def home (request) :
    posts = blog.objects.all()

    return render(request, 'blogs/home.html', {'post' : posts})



def write (request ):
    if request.method == 'POST':
        form = blogform(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_name = request.user
            instance.save()
            return redirect('BlogPage')
    else :
        posts = blog.objects.all()
        form = blogform()
        context = {
            'post ':posts,
            'form' : form
        }
        return render(request, 'blogs/write.html', context)
