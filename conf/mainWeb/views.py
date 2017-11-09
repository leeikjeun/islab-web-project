from django.shortcuts import render ,redirect
from .admin import UserCreationForm
from .forms import UnknownBoardCreationForm
from .models import UnknownBoard, GGulTipBoard, ReportBoard
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request, 'mainWeb/index.html', {})

def lab_intro(request):
    return render(request, 'mainWeb/Lab_intro/Lab_intro.html', {})

def profe_intro(request):
    return render(request, 'mainWeb/Profe_intro/profe_intro.html', {})

def unknown_post(request):
    unKnowBoard = UnknownBoard.objects.all()
    paginator = Paginator(unKnowBoard, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        unKnowBoard = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        unKnowBoard = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        unKnowBoard = paginator.page(paginator.num_pages)

    return render(request, 'mainWeb/Unknown_post/Unknown_post.html', {'boards' : unKnowBoard})

def unknown_post_create(request):
    if request.method == 'POST':
        form = UnknownBoardCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/unknownpost')
    else:
        form = UnknownBoardCreationForm()

    return render(request, 'mainWeb/Unknown_post/Unknown_post_create.html', {'form':form})

def unknown_post_detail(request, pk):
    board = UnknownBoard.objects.get(id=pk)
    return render(request, 'mainWeb/Unknown_post/Unknown_post_detail.html', {"board":board})

def profe_info(request):
    return render(request, 'mainWeb/Profe_info/Profe_info.html', {})

def ggul_tip(request, pr):
    boards = GGulTipBoard.objects.get(name=pr)
    return render(request, 'mainWeb/Profe_info/GGul_tip/GGul_tip.html', {'boards' : boards})

def jokbo(request):
    return render(request, 'mainWeb/Profe_info/jokbo/jokbo.html', {})

def report(request):
    return render(request, 'mainWeb/Profe_info/report/report.html',{})

def mypage(request):
    return render(request, 'mainWeb/mypage/mypage.html', {})

def lab_member(request):
    return render(request, 'mainWeb/lab_member/lab_member.html')

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'mainWeb/kind_of_sign/sign_up.html', {'form': form})
