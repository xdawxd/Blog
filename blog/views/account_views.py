from blog.models import UserProfile
from blog.forms import UserForm, UserProfileForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View, CreateView
from django.shortcuts import render


class SignUp(CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('blog:login')
    form_class = UserForm


class LoginView(View):

    def post(self, request, *args, **kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse('blog:post_list'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:

            return HttpResponse('Invalid login detail supplied!')

    def get(self, request, *args, **kwargs):
        return render(request, 'blog:login')
