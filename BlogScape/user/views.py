from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

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

    return render (request, 'user/profile.html' )



