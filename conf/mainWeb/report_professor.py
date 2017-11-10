def leesangjun_reportCreate(request):

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
    return render(request, 'mainWeb/profe_info/'+ 'leesangjun' +'/report/report_create.html', {'form': form})

def angijung_reportCreate(request):

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
    return render(request, 'mainWeb/profe_info/'+ 'angijung' +'/report/report_create.html', {'form': form})

def byunsangyong_reportCreate(request):

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
    return render(request, 'mainWeb/profe_info/'+ 'byunsangyong' +'/report/report_create.html', {'form': form})

def byunyoungchul_reportCreate(request):

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
    return render(request, 'mainWeb/profe_info/'+ 'byunyoungchul' +'/report/report_create.html', {'form': form})

def gwakhoyoung_reportCreate(request):

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
    return render(request, 'mainWeb/profe_info/'+ 'gwakhoyoung' +'/report/report_create.html', {'form': form})

def kimdohyun_reportCreate(request):

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
    return render(request, 'mainWeb/profe_info/'+ 'kimdohyun' +'/report/report_create.html', {'form': form})

def kimjanghyung_reportCreate(request):

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
    return render(request, 'mainWeb/profe_info/'+ 'kimjanghyung' +'/report/report_create.html', {'form': form})

def songwangchul_reportCreate(request):

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
    return render(request, 'mainWeb/profe_info/'+ 'songwangchul' +'/report/report_create.html', {'form': form})
