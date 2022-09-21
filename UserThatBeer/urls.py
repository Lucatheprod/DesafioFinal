
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView

from django.urls import path

from UserThatBeer.views import  changeAvatar, login_request, register, changePasswordsuccess, user_profile
urlpatterns = [
    path('login/', login_request, name='UserThatBeerLogin'),
    path('register/', register, name='UserThatBeerRegister'),
    path('logout/', LogoutView.as_view(template_name='UserThatBeer/logout.html'), name='UserThatBeerLogout'),
    path('password/', PasswordChangeView.as_view(template_name='UserThatBeer/changePassword.html'), name='UserThatBeerPassword'),
    path('password/changed/', changePasswordsuccess , name= 'password_change_done'),
    path('profile_edit/', user_profile , name='UserThatBeerProfileEdit'),
    path ('change_avatar/<int:user>/', changeAvatar, name= 'UserThatBeerChangeBio')
    
]