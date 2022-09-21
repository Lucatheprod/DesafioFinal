from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from UserThatBeer.forms import  AvatarChangeForm, UserRegisterForm, EditUserProfileForm
from django.contrib.auth.models import User

from UserThatBeer.models import Avatar



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = data.get('username')
            password = data.get('password')
            user = authenticate(username=user, password=password)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')
                return redirect('AppThatBeerInicio')

        else:
            messages.info(request, 'Inicio de sesion fallido!')
            return redirect('AppThatBeerInicio')

    contexto = {
        'form': AuthenticationForm(),
        'title': 'INICIO DE SESIÓN',
        'name_submit': 'Iniciar sesion',
    }
    return render(request, 'UserThatBeer/login.html', contexto)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()
            messages.info(request, 'Tu usuario fue registrado satisfactoriamente')
            return redirect('AppThatBeerInicio')
        else:
            messages.info(request, 'Tu usuario no pudo ser registrado')

    contexto = {
        'form': UserRegisterForm(),
        'title': 'NUEVO REGISTRO',
        'name_submit': 'Registrarse',
    }
    return render(request, 'UserThatBeer/register.html', contexto)


def changePasswordsuccess(request):        
            return render(request, 'UserThatBeer/password_change_done.html')


@login_required
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Perfil editado con éxito')
                fm.save()
        else:
            fm= EditUserProfileForm(instance=request.user)        
        fm = EditUserProfileForm(instance=request.user)
        return render(request, 'UserThatBeer/userprofile.html' , {'name': request.user, 'form':fm})
    else:
        return redirect('AppThatBeerInicio')


@login_required
def changeAvatar(request, user):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user=user)
        except: 
            avatar = Avatar.objects.create(user=request.user)
       
        if request.method == "POST":
            fm = AvatarChangeForm(request.POST, request.FILES)
            if fm.is_valid():
                info = fm.cleaned_data
                messages.success(request, 'Los datos han sido guardados')
                avatar.imagen = info['imagen']
                avatar.save()
                return redirect('AppThatBeerInicio')

        else:
            fm= AvatarChangeForm()        
        fm = AvatarChangeForm()
        return render(request, 'UserThatBeer/changeAvatar.html' , {'form':fm})
    else:
        return redirect('AppThatBeerInicio')

