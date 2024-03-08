from django.shortcuts import render, redirect


def BASE(request):
    return render(request,'layout/base.html')
