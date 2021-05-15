from blog.models import UserProfile
from blog.forms import UserForm, UserProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView


class SignUp(CreateView):
    template_name = 'registration/register.html'
    #success_url = reverse_lazy('blog:login')
    form_class = UserForm

