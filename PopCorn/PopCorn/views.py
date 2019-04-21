from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth


@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'core/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})


# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         current_user = User.objects.get(pk=uid)
#         print(current_user)
#     except(TypeError, ValueError, OverflowError):
#         current_user = None
#     if current_user is not None and account_activation_token.check_token(current_user, token):
#         current_user.is_active = True
#         current_user.save()
#         login(request, current_user)
#         return redirect('/users/User_Home')
#
#     else:
#         return render(request,'users/invalid_activation_link.html')
#         # return HttpResponse('Activation link is invalid')

# def PasswordReset(request):
#     if request.method == 'POST':
#         forms = ResetForm(request.POST)
#         if forms.is_valid():
#             email = forms.cleaned_data.get('enter_email')
#             try:
#                 current_user = User.objects.get(email=email)
#             except:
#                 current_user = False
#             if current_user:
#                 socket.getaddrinfo('localhost', 8080)
#                 current_site = get_current_site(request)
#                 mail_subject = 'Reset Your Password'
#                 message = render_to_string('users/password_reset_email.html', {
#                     'current_user': current_user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(current_user.pk)).decode(),
#                     'token': account_activation_token.make_token(current_user),
#                 })
#                 to_email = forms.cleaned_data.get('enter_email')
#                 email = EmailMessage(
#                     mail_subject, message, to=[to_email]
#                 )
#                 email.send()
#                 return render(request, 'users/password_reset_done.html')
#             else:
#                 context = {
#                     'forms': forms,
#                     'message': "This e-mail does not exist",
#                 }
#                 return render(request, 'users/password_reset_form.html', context)
#                 # return HttpResponse('Email does not exist')
#         else:
#             context = {
#                 'forms': forms,
#             }
#             return render(request, 'users/password_reset_form.html', context)
#     else:
#         forms = ResetForm()
#         return render(request, 'users/password_reset_form.html', {'forms': forms})
#
#
# def reset(request, uidb64, token):
#     if request.method == 'POST':
#         forms = User_reset_form(request.POST)
#         if forms.is_valid():
#             password1 = forms.cleaned_data.get('Password')
#             password2 = forms.cleaned_data.get('Confirm_Password')
#             if password1 == password2:
#                 try:
#                     uid = urlsafe_base64_decode(uidb64).decode()
#                     current_user = User.objects.get(pk=uid)
#                     print(current_user)
#                 except(TypeError, ValueError, OverflowError):
#                     current_user = None
#                 if current_user is not None and account_activation_token.check_token(current_user, token):
#                     current_user.set_password(password1)
#                     current_user.save()
#                     return HttpResponse('Changed')
#                 else:
#                     context = {
#                         'forms': forms,
#                         'message': "This link is invalid now"
#                     }
#                     return render(request, 'users/Reset_done.html', context)
#                     # return HttpResponse('Invalid reset link')
#             else:
#                 context = {
#                     'forms': forms,
#                     'message': "Your password does't match"
#                 }
#                 return render(request, 'users/Reset_done.html', context)
#                 # return HttpResponse('Password does not match')
#         else:
#             return render(request, 'users/Reset_done.html', {'forms': forms})
#     else:
#         forms = User_reset_form()
#         return render(request, 'users/Reset_done.html', {'forms': forms})
#
#
# def reset2(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         current_user = User.objects.get(pk=uid)
#         print(current_user)
#     except(TypeError, ValueError, OverflowError):
#         current_user = None
#     if current_user is not None and account_activation_token.check_token(current_user, token):
#         if request.method == 'POST':
#             forms = ResetDoneForm(request.POST)
#             if forms.is_valid():
#                 password1 = forms.cleaned_data.get('Password')
#                 password2 = forms.cleaned_data.get('Confirm_Password')
#                 if password1 == password2:
#                     current_user.set_password(password1)
#                     current_user.save()
#                     login(request, current_user)
#                     return redirect('/users/User_Home')
#                     # return HttpResponse('Changed')
#                 else:
#                     context={
#                         'forms': forms,
#                         'message': "Your password does't match"
#                     }
#                     return render(request, 'users/Reset_done.html', context)
#             else:
#                 return render(request, 'users/Reset_done.html', {'forms': forms})
#         else:
#             forms = ResetDoneForm()
#             return render(request, 'users/Reset_done.html', {'forms': forms})
#         current_user.set_password(password1)
#         current_user.save()
#         return HttpResponse('Changed')
#     else:
#         return render(request, 'users/invalid_reset_link.html')
#         # return HttpResponse('Invalid reset link')
