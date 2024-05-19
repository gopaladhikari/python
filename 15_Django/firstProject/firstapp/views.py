from django.shortcuts import render


def all_chai(request):
    return render(request, "firstapp/all_chai.html")
