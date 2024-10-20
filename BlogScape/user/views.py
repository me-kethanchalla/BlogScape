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
    

    

def profile (request,username1) :
    user_self =  request.user.username  
    user = User.objects.get(username=user_self) 
    user1 = User.objects.filter( username=  username1).first()
    # if user1 is None:
    #     # Handle the case where the user profile being viewed does not exist
    #     return render(request, 'user/profile_not_found.html', {'username': username1}) 

    if user_self == username1 :
        blogs_by_user = blog.objects.filter(author_name = user)
        total = blogs_by_user.count()
        
        
        context = {
        'blog_by_author' :  blogs_by_user,
        'total' : total,
        'username' : user_self,
        'email' : request.user.email
        }
    else:
        blogs_by_user = blog.objects.filter(author_name = user1)
        total = blogs_by_user.count()

        context = {
        'blog_by_author' :  blogs_by_user,
        'total' : total,
        'username' : username1, 
        'email' :None

        }

    return render (request, 'user/profile.html', context )



