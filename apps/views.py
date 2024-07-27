from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, View, CreateView

# from apps.forms import RegisterModelForm
from apps.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

class MainTemplateView( TemplateView):
    template_name = 'apps/sayt/mains.html'
    # login_url = reverse_lazy('logins')


class LogintListView(LoginRequiredMixin,TemplateView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    template_name = 'apps/sayt/logins.html'
    context_object_name = 'Logins'


class StudentDetailw(LoginRequiredMixin,DetailView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    template_name = 'apps/students/student-details.html'
    context_object_name = 'student'


class RegisterWiever(CreateView):
    template_name = 'apps/auth/register.html'
    form_class = UserCreationForm


class LoginWieve(View):
    def get(self, request):
        return render(request, 'apps/sayt/logins.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect('main_page')
        return redirect('logins')



class updates(LoginRequiredMixin,TemplateView):
    template_name = 'apps/sayt/update.html'