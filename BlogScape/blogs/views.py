from django.shortcuts import render, redirect
from .models import blog 
from .forms import blogform
from django.contrib.auth.decorators import login_required

def home (request) :
    # this is for getting all objects of a model
    posts = blog.objects.all()
    return render(request, 'blogs/home.html', {'post' : posts})


#for getting only 1 object of a model it looks like this    
#   def blog_detail(request, blog_id):
#       blog = get_object_or_404(Blog, id=blog_id)



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
