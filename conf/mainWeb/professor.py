from django.shortcuts import render ,redirect

def lee_ggultip(request):
    return render(request, 'mainWeb/Profe_info/leesangjun/ggul_tip/GGul_tip.html',{})

def lee_report(request):
    return render(request, 'mainWeb/Profe_info/leesangjun/report/report.html',{})

def byun0_ggultip(request):
    return render(request, 'mainWeb/Profe_info/byunyoungchul/ggul_tip/GGul_tip.html',{})

def byun0_report(request):
    return render(request, 'mainWeb/Profe_info/byunyoungchul/report/report.html',{})

def byun1_ggultip(request):
    return render(request, 'mainWeb/Profe_info/byunsangyong/ggul_tip/GGul_tip.html',{})

def byun1_report(request):
    return render(request, 'mainWeb/Profe_info/byunsangyong/report/report.html',{})

def an_ggultip(request):
    return render(request, 'mainWeb/Profe_info/angijung/ggul_tip/GGul_tip.html',{})

def an_report(request):
    return render(request, 'mainWeb/Profe_info/angijung/report/report.html',{})

def gwak_ggultip(request):
    return render(request, 'mainWeb/Profe_info/gwakhoyoung/ggul_tip/GGul_tip.html',{})

def gwak_report(request):
    return render(request, 'mainWeb/Profe_info/gwakhoyoung/report/report.html',{})

def kim0_ggultip(request):
    return render(request, 'mainWeb/Profe_info/kimdohyun/ggul_tip/GGul_tip.html',{})

def kim0_report(request):
    return render(request, 'mainWeb/Profe_info/kimdohyun/report/report.html',{})

def kim1_ggultip(request):
    return render(request, 'mainWeb/Profe_info/kimjanghyung/ggul_tip/GGul_tip.html',{})

def kim1_report(request):
    return render(request, 'mainWeb/Profe_info/kimjanghyung/report/report.html',{})

def song_ggultip(request):
    return render(request, 'mainWeb/Profe_info/songwangchul/ggul_tip/GGul_tip.html',{})

def song_report(request):
    return render(request, 'mainWeb/Profe_info/songwangchul/report/report.html',{})
