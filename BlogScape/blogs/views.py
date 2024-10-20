from django.shortcuts import render, redirect,get_object_or_404
from .models import blog
from user.models import User
from .forms import blogform, commentForm, SearchForm
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


def search ( request ):
    form = SearchForm()
    results_in_blogs = []    
    results_in_authors = []    

    if request.method == 'GET' :
        query = request.GET.get('query')
        if query:
            results_in_blogs = blog.objects.filter(title__icontains=query)
            results_in_authors = User.objects.filter(username__icontains=query)

        context  = { 'form': form, 'results_in_blogs':results_in_blogs, 'results_in_authors' :results_in_authors, 'searched_yet':True }

    else :
        context = { 'form': form,'results_in_blogs':results_in_blogs, 'results_in_authors' :results_in_authors, 'searched_yet' : False}
        

    return render (request, 'blogs/search.html', context)   




