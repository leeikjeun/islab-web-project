from django.shortcuts import render ,redirect
from .admin import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'mainWeb/index.html', {})

def Lab_intro(request):
    return render(request, 'mainWeb/Lab_intro/Lab_intro.html', {})

def Profe_intro(request):
    return render(request, 'mainWeb/Profe_intro/profe_intro.html', {})

def Unknown_post(request):
    return render(request, 'mainWeb/Unknown_post/Unknown_post.html', {})

def Unknown_post_detail(request):
    return render(request, 'mainWeb/Unknown_post/Unknown_post_detail.html', {})

def Profe_info(request):
    return render(request, 'mainWeb/Profe_info/Profe_info.html', {})

def GGul_tip(request):
    return render(request, 'mainWeb/Profe_info/GGul_tip/GGul_tip.html', {})

def jokbo(request):
    return render(request, 'mainWeb/Profe_info/jokbo/jokbo.html', {})

def report(request):
    return render(request, 'mainWeb/Profe_info/report/report.html',{})

def mypage(request):
    return render(request, 'mainWeb/mypage/mypage.html', {})

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'mainWeb/kind_of_sign/sign_up.html', {'form': form})
