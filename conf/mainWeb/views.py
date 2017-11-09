from django.shortcuts import render ,redirect
from .admin import UserCreationForm
from .forms import UnknownBoardCreationForm, MessageCreationFrom, GGulTipBoardCreationForm, ReportBoardCreationFrom
from .models import UnknownBoard, GGulTipBoard, ReportBoard, MyUser, Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
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
    board.hit_count += 1;


    board.save();
    return render(request, 'mainWeb/Unknown_post/Unknown_post_detail.html', {"board":board})

def profe_info(request):
    return render(request, 'mainWeb/Profe_intro/Profe_info.html', {})

def ggul_tip(request, pr):
    boards = GGulTipBoard.objects.all().filter(professor=pr)
    paginator = Paginator(boards, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        boards = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        boards = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        boards = paginator.page(paginator.num_pages)

    return render(request, 'mainWeb/Profe_info/' + str(pr) + '/ggul_tip/GGul_tip.html', {'boards' : boards})

def jokbo(request):
    return render(request, 'mainWeb/Profe_info/jokbo/jokbo.html', {})

def report(request, pr):
    boards = ReportBoard.objects.all().filter(professor=pr)
    paginator = Paginator(boards, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        boards = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        boards = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        boards = paginator.page(paginator.num_pages)

    return render(request, 'mainWeb/Profe_info/' + str(pr) + '/report/report.html',{'boards' : boards})

def ggulTipDetail(request,pr, pk):
    board = ReportBoard.objects.get(id=pk)
    return render(request, 'mainWeb/Profe_info/' + str(pr) + '/ggul_tip/GGul_tip_detail.html', {'board' : boards})

def reportDetail(request,pr, pk):
    board = ReportBoard.objects.get(id=pk)
    return render(request, 'mainWeb/Profe_info/' + str(pr) + '/report/GGul_tip_detail.html', {'board' : boards})

def ggulTipCreate(request,pr=None):

    if request.method == 'POST':
        GGulTipBoard.create(title=request.POST['title'],
                            user=request.user.user_name,
                            content=request.POST['content'],
                            fileContent=request.FILES['fileContent'],
                            professor=request.POST['professor']
                            )
        return redirect('/')
    else:
        form = GGulTipBoardCreationForm()
    return render(request, 'mainWeb/profe_info/'+ str(pr) +'/ggul_tip/ggul_tip_create.html', {'form': form})

def reportCreate(request):
    if request.method == 'POST':
        GGulTipBoard.create(title=request.POST['title'],
                        user=request.user.user_name,
                        content=request.POST['content'],
                        fileContent=request.FILES['fileContent'],
                        professor=request.POST['professor']
                        )
        return redirect('/')
    else:
        form = ReportBoardCreationFrom()

    return render(request, 'mainWeb/profe_info/'+ str(pr) +'/report/report_create.html', {'form': form})


def mypage(request):
    messages = Message.objects.all().filter(receiveUser=request.user.user_name)

    paginator = Paginator(messages, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        messages = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        messages = paginator.page(paginator.num_pages)

    return render(request, 'mainWeb/mypage/mypage.html', {'messages': messages})

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

def message(request):

    if request.method == 'POST':

        massage = Message(title = request.POST['title'],
                        content = request.POST['title'],
                        senderUser= request.user.user_name,
                        receiveUser=request.POST['receiveUser'])
        massage.save()
        return HttpResponse('<script type="text/javascript">window.close();</script>')

    else:
        form = MessageCreationFrom()
        userList = MyUser.objects.all()
    return render(request, 'mainWeb/message.html', {'form': form, 'users': userList})
