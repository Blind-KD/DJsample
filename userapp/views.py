from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

def registerUser(request):
	if request.method == 'POST':
		form = registerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = registerForm()
	return render(request, 'userregister.html', {'form':form})

@login_required
def updateUser(request):
    if request.method == 'POST':
        user_form = userForm(request.POST,instance=request.user)
        profile_form = profileForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = userForm(instance=request.user)
        profile_form = profileForm(instance=request.user.profile)
    context = {
            'user_form':user_form,
            'profile_form':profile_form
    }
    return render(request, 'userupdate.html', context)
