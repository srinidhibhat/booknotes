from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    # validate the data coming from POST request
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # this will save the form data to User model. We can verify this in admin page
            form.save()
            # validated form data will be in cleaned_data dictionary by default
            username = form.cleaned_data.get('username')
            # display a flash message
            messages.success(request, f'Your account has been created! You can login now.')
            return redirect('login')
    # if the request is GET, don't validate
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

# adding the django provided login_required decorator to make the profile page
# accessible only if the user is logged in
@login_required
def profile(request):
    if request.method == 'POST':
        # since we're updating the info, we want the existing info to be pre-filled already
        # below 2 lines of code does that
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # flash a proper message, and redirect back to profile page
            messages.success(request, f'Your account has been updated!')
            # we don't want to fall to render return stmt. Because redirect will generate another GET request
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }

    return render(request, 'users/profile.html', context)
