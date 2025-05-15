from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: not u.is_authenticated) #Ограничение для отключения входа и регистрации авторизированным пользователян
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'users/register.html', {'form': form})



@user_passes_test(lambda u: not u.is_authenticated)
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # form.cleaned_data['username'] == введённый email
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:catalog')
            else:
                form.add_error(None, "Неверный email или пароль.")
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


@login_required # только авторизованные пользователи могут видеть страницу профиля.
def user_profile(request):
    user = request.user  # получаем текущего вошедшего пользователя
    return render(request, 'users/user_profile.html',{'user':user})



@login_required# только авторизованные пользователи могут видеть страницу
def user_logout(request):
    logout(request)
    return redirect('users:login')

