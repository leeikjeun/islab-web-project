from django.shortcuts import render, get_object_or_404
from .models import UnknowNameBoard, ProffessorData

# Create your views here.
def index(request):
    return render(request, 'mainWeb/index.html', {})

def Lab_intro(request):
    return render(request, 'mainWeb/Lab_intro/Lab_intro.html', {})

def Profe_intro(request):
    return render(request, 'mainWeb/Profe_intro/profe_intro.html', {})

def Unknown_post(request):
    posts = UnknowNameBoard.objects.all();
    return render(request, 'mainWeb/Unknown_post/Unknown_post.html', {'posts' : posts})

def Unknown_post_detail(request, pk):
    post = get_object_or_404(UnknowNameBoard, pk = pk)
    return render(request, 'mainWeb/Unknown_post/Unknown_post_detail.html', {'post' : post})

def Profe_info(request):
    posts = ProffessorData.objects.all();
    return render(request, 'mainWeb/Profe_info/Profe_info.html', {'posts' : posts})

def GGul_tip(request, pk):
    post =
    return render(request, 'mainWeb/Profe_info/GGul_tip/GGul_tip.html', {})

def jokbo(request):
    return render(request, 'mainWeb/Profe_info/jokbo/jokbo.html', {})

def report(request):
    return render(request, 'mainWeb/Profe_info/report/report.html',{})

def mypage(request):
    return render(request, 'mainWeb/mypage/mypage.html', {})

def test(request):
    return render(request, 'mainWeb/dfdf.html', {})
