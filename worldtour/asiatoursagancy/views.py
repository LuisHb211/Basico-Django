from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from .forms import ContactForm, RegisterForm
from .models import Tour
# Create your views here.

def index(request):
  tours = Tour.objects.all()
  context = {'tours':tours}
  return render(request, 'tours\index.html', context)


def home_forms_view(request): 
  return render(request, 'tours\home_forms.html')

def contact_view(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.send_email()
      return redirect('contact-success')
  else:
    form = ContactForm()
    context = {'form':form}
  return render(request, 'tours/contact.html', context)


def contact_success_view(request):
  return render(request, 'tours/contact_success.html')

def register_view(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = User.objects.create_user(username=username, password=password)
      login(request, user)
      return redirect('home')
  else:
    form = RegisterForm()
  return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
  error_message = None
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      next_url = request.POST.get('next') or request.GET.get('next') or 'home'
      return redirect(next_url)
    else:
      error_message = "Invalid Credentials!"
  return render(request, 'accounts/login.html', {'error':error_message})

def logout_view(request):
  if request.method == "POST":
    logout(request)
    return redirect('login')
  else:
    return redirect ('home')


@login_required
def home_view(request):
  return render(request, 'auth1_app/home.html')


class ProtectedView(LoginRequiredMixin, View):
  login_url = '/login/'
  redirect_field_name = 'redirect_to'

  def get(self, request):
    return render(request, 'registration/protected.html')