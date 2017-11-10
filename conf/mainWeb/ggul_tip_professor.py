from django.shortcuts import render ,redirect
from .admin import UserCreationForm
from .forms import UnknownBoardCreationForm, MessageCreationFrom, GGulTipBoardCreationForm, ReportBoardCreationFrom
from .models import UnknownBoard, GGulTipBoard, ReportBoard, MyUser, Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

def angijung_ggulTipCreate(request):
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
    return render(request, 'mainWeb/profe_info/'+ 'angijung' +'/ggul_tip/ggul_tip_create.html', {'form': form})

def byunsangyong_ggulTipCreate(request):
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
    return render(request, 'mainWeb/profe_info/'+ 'byunsangyong' +'/ggul_tip/ggul_tip_create.html', {'form': form})

def byunyoungchul_ggulTipCreate(request):
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
    return render(request, 'mainWeb/profe_info/'+ 'byunyoungchul' +'/ggul_tip/ggul_tip_create.html', {'form': form})

def gwakhoyoung_ggulTipCreate(request):
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
    return render(request, 'mainWeb/profe_info/'+ 'gwakhoyoung' +'/ggul_tip/ggul_tip_create.html', {'form': form})

def kimdohyun_ggulTipCreate(request):
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
    return render(request, 'mainWeb/profe_info/'+ 'kimdohyun' +'/ggul_tip/ggul_tip_create.html', {'form': form})

def kimjanghyung_ggulTipCreate(request):
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
    return render(request, 'mainWeb/profe_info/'+ 'kimjanghyung' +'/ggul_tip/ggul_tip_create.html', {'form': form})

def leesangjun_ggulTipCreate(request):
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
    return render(request, 'mainWeb/profe_info/'+ 'leesangjun' +'/ggul_tip/ggul_tip_create.html', {'form': form})

def songwangchul_ggulTipCreate(request):
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
    return render(request, 'mainWeb/profe_info/'+ 'songwangchul' +'/ggul_tip/ggul_tip_create.html', {'form': form})
