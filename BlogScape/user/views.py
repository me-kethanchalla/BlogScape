from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignupForm
from blogs.models import blog

def register ( request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginPage')
        else:   
            context = {
                'form': form
            }
            return render(request, 'user/register.html', context)
        
    else :
        form = SignupForm() 
        context = {
            'form' : form
        }
        return render(request, 'user/register.html', context)
    

    

def profile (request) :
    user_self =  request.user.username 
    user = User.objects.get(username=user_self) 
    blogs_by_user = blog.objects.filter(author_name = user)
    total = 0
    for i in blogs_by_user  :
        total = total + 1
    
    
    context = {
    'blog_by_author' :  blogs_by_user,
    'total' : total
    }
    return render (request, 'user/profile.html', context )



