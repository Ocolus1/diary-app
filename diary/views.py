from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as lg, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DiaryForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from .models import Diary


from .models import Diary


def home(request):
    return render(request, "diary/home.html")


@login_required
def index(request):
    diarys = Diary.objects.filter(user=request.user.id).order_by("-id")

    context = {"diarys": diarys}
    return render(request, "diary/index.html", context)


def register(request):
    registered = True
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():   
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.filter(username=username)
            if user is not None:
                User.objects.create_user(username=username,password=password)
                return redirect("login")
        else:
            registered = False

    context = {"registered": registered, "form": form}
    return render(request, "diary/register.html", context)


def login(request):
    valid = True
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    lg(request,user)
                    return redirect('index')
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                valid = False

    context = {"valid": valid, "form": form}
    return render(request, "diary/login.html", context)

@login_required
def add(request):
    form = DiaryForm()

    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            m = form.cleaned_data["message"]
            t = Diary(message=m)
            t.save()
            request.user.diary.add(t)
            return redirect("index")

    context = {"form": form}
    return render(request, "diary/add.html", context)


@login_required
def loging_out(request):
    logout(request)
    return redirect('home')
