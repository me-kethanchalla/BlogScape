from django.shortcuts import render, redirect,get_object_or_404
from .models import blog
from .forms import blogform, commentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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



def blog_detail(request, blog_id):
    blog_now = get_object_or_404(blog, id=blog_id)
    comments = blog_now.comments.all()
    if (request.method == 'POST'):
        comments_form = commentForm(request.POST)
        if comments_form.is_valid():
            instance = comments_form.save(commit=False)
            instance.blog = blog_now
            instance.author_name = request.user
            instance.save()
            redirect('BlogDetail', blog_id=blog_id)

    else:
        comments_form = commentForm()     

    context = {
        'blog' : blog_now,
        'comments' : comments,
        'comment_form' : comments_form
    }        

    return render(request, 'blogs/detail.html', context)